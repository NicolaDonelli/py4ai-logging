import os
import unittest
from logging import FileHandler, StreamHandler, getLogger
from unittest import TestCase

from py4ai.logging import configFromFiles
from tests import DATA_FOLDER, clean

configFromFiles(
    config_files=[os.path.join(DATA_FOLDER, "logging.yml")],
    capture_warnings=True,
    catch_exceptions="except",
)


class TestSetupLogger(TestCase):
    root_logger = getLogger()
    py4ai_logger = getLogger("py4ai")

    def test_console_logger(self):
        self.root_logger.info("Example of logging with root logger!")
        self.assertEqual(self.root_logger.name, "root")
        self.assertEqual(self.root_logger.level, 20)
        self.assertTrue(
            all([isinstance(h, StreamHandler) for h in self.root_logger.handlers])
        )

    def test_file_logger_name(self):
        self.assertEqual(self.py4ai_logger.name, "py4ai")

    def test_file_logger_handlers(self):
        self.assertTrue(
            all([isinstance(h, FileHandler) for h in self.py4ai_logger.handlers])
        )

    def test_file_logger_path_creation(self):
        self.assertTrue(os.path.exists(os.environ["TMP_LOG_FOLDER"]))
        self.assertTrue(
            all([os.path.exists(h.baseFilename) for h in self.py4ai_logger.handlers])
        )

    def test_file_logger_overwrite_level(self):
        self.assertEqual(self.py4ai_logger.level, 20)

    def test_file_logger_dest_file(self):
        res = {"regular.log": 10, "errors.log": 40}
        self.assertTrue(
            all(
                [
                    h.level == res[os.path.basename(h.baseFilename)]
                    for h in self.py4ai_logger.handlers
                ]
            )
        )

    def test_file_logger_info_message(self):
        msg = "Example of logging with py4ai logger!"
        self.py4ai_logger.info(msg)
        self.py4ai_logger.handlers[0].flush()
        with open(self.py4ai_logger.handlers[0].baseFilename, "r") as fil:
            lines = fil.readlines()
        lin = lines[-1]
        self.assertEqual(lin.split(" - ")[-1], f"{msg}\n")
        self.assertEqual(lin.split(" - ")[-2], "INFO")

    def test_file_logger_warning_message(self):
        warning_msg = "Example of logging a warning with py4ai logger!"
        self.py4ai_logger.warning(warning_msg)
        self.py4ai_logger.handlers[0].flush()
        with open(self.py4ai_logger.handlers[0].baseFilename, "r") as fil:
            lines = fil.readlines()
        lin = lines[-1]
        self.assertEqual(lin.split(" - ")[-1], f"{warning_msg}\n")
        self.assertEqual(lin.split(" - ")[-2], "WARNING")

    def test_file_logger_error_message(self):
        error_msg = "Example of logging an error with py4ai logger!"
        self.py4ai_logger.error(error_msg)
        self.py4ai_logger.handlers[1].flush()
        with open(self.py4ai_logger.handlers[1].baseFilename, "r") as fil:
            lines = fil.readlines()
        lin = lines[-1]
        self.assertEqual(lin.split(" - ")[-1], f"{error_msg}\n")
        self.assertEqual(lin.split(" - ")[-2], "ERROR")

    # TODO: [ND] Find a way to test except_logger: I know it works fine but I cannot find a way to raise exceptions
    #  without sopping the execution (and failing the test)
    # @logTest
    # def test_file_logger_catch_exceptions(self):
    #     except_logger = getLogger(name="except")
    #
    #     raise TypeError('Tipo Sbagliato')
    #
    #     with open(except_logger.handlers[1].baseFilename, 'r') as fil:
    #         lines = fil.readlines()
    #     lin = lines[-4:]
    #     self.assertEqual(lin[0].split(" - ")[-2], 'ERROR')
    #     self.assertEqual(lin[0].split(" - ")[-1], 'TypeError: Tipo Sbagliato\n')
    #     self.assertEqual(lin[-1], 'TypeError: Tipo Sbagliato\n')


if __name__ == "__main__":
    unittest.main()
    clean()
