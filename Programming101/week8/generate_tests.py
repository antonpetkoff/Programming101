
class TestsGenerator:
    def __init__(self, dsl_file_name):
        self.dsl_file_name = dsl_file_name
        self.dsl_text = self._read_file(dsl_file_name)

    def _read_file(self, file_name):
        contents = ""
        with open(file_name) as read_file:
            contents = read_file.readlines()
        return contents

    def _write_file(self, file_name, text):
        with open(file_name) as write_file:
            write_file.write(text)

    def generate_file_name(self):
        words = self.dsl_file_name[:-4].split("_")
        print(words)
        # work in progress

    def write_tests(self):
        template = "teststests tests"
        file_name = self.generate_file_name()
        self._write_file(file_name, template)

"""
import unittest

{imports}

class {class_name}(unittest.TestCase):
    \"\"\"{test_doc}\"\"\"

    {test_cases}

if __name__ == '__main__':
    unittest.main()


    def testCase1(self):
        self.assertTrue(is_prime(7), "7 should noot be prime")

    def testCase2(self):
        self.assertFalse(is_prime(8), "8 should be prime")

"""


def main():
    tg = TestsGenerator('is_prime_test.dsl')
    tg.generate_file_name()


if __name__ == '__main__':
    main()
