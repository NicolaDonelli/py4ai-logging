import os
import random

test_path = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(test_path, "resources", "data")
os.environ["TMP_LOG_FOLDER"] = os.path.join("/tmp", "%032x" % random.getrandbits(128), "logs")

if not os.path.exists(os.environ["TMP_LOG_FOLDER"]):
    os.makedirs(os.environ["TMP_LOG_FOLDER"])


def clean():
    os.system(f"rm -rf {os.environ['TMP_LOG_FOLDER']}/..")
    del os.environ["TMP_LOG_FOLDER"]
