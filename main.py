import test_data_creator
import subprocess

if __name__ == "__main__":
    test_data_creator.create_test_data()
    subprocess.run(["pytest", "tests/"])
