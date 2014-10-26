import unittest
import os
from uuid import uuid4
from concat_files import concat_files


class ConcatFilesTests(unittest.TestCase):

    def test_with_existing_files(self):
        TEST_FILES = 20
        initial_state = ""
        megatron_exists = False

        if "MEGATRON.txt" in os.listdir(os.getcwd()):
            with open("MEGATRON.txt", "r") as readFile:
                initial_state = readFile.read()
                megatron_exists = True
        else:
            with open("MEGATRON.txt", "w") as writeFile:
                pass

        file_names = [str(uuid4()) for i in range(TEST_FILES)]
        contents = [str(uuid4()) for i in range(TEST_FILES)]

        expected_result = initial_state
        for i in range(TEST_FILES):
            expected_result += contents[i]
            with open(file_names[i], "w") as writeFile:
                writeFile.write(contents[i])

        concat_files(file_names)

        call_result = ""
        with open("MEGATRON.txt", "r") as readFile:
            call_result = readFile.read()

        print(call_result)
        print(expected_result)
        self.assertEqual(call_result, expected_result)

        for i in range(TEST_FILES):
            os.remove(file_names[i])

        if megatron_exists:
            with open("MEGATRON.txt", "w") as writeFile:
                writeFile.write(initial_state)
        else:
            os.remove("MEGATRON.txt")


if __name__ == '__main__':
    unittest.main()
