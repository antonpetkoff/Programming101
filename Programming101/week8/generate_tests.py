from functools import reduce


class TestsGenerator:
    def __init__(self, dsl_file_name):
        self.dsl_file_name = dsl_file_name
        self.lines = self._read_file_lines(dsl_file_name)

    def _read_file_lines(self, file_name):
        contents = ""
        with open(file_name) as read_file:
            contents = read_file.read().strip().split('\n')
            contents = list(filter(lambda x: x != '', contents))
        return contents

    def _write_file(self, file_name, text):
        with open(file_name) as write_file:
            write_file.write(text)

    def generate_file_name(self):
        return self.dsl_file_name.replace('dsl', 'py')

    def generate_class_name(self):
        words = self.dsl_file_name[:-4].split("_")
        capital = map(lambda w: w.title(), words)
        class_name = str(reduce(lambda a, b: a + b, capital)) + 's'
        return class_name

    def write_tests(self):
        template = "teststests tests"
        file_name = self.generate_file_name()
        self._write_file(file_name, template)


def main():
    tg = TestsGenerator('is_prime_test.dsl')
    print(tg.generate_class_name())


if __name__ == '__main__':
    main()

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
