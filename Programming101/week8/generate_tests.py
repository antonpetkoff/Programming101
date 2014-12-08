from functools import reduce
import re


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

    def generate_imports(self):
        imports = filter(lambda x: x.startswith('from') or
                         x.startswith('import'), self.lines)
        return '\n'.join(imports)

    def generate_docstring(self):
        doc_str = filter(lambda x: x[0] == '\"' and x[-1] == '\"', self.lines)
        return '\"\"' + str(list(doc_str)[0]) + '\"\"'

    def generate_test_cases_all(self):
        quoted = filter(lambda x: x[0] == '\"', self.lines)
        test_cases = list(quoted)[1:]

        result = self.generate_test_case(test_cases[0], 1)
        print(result)

    def generate_boolean_test_case(self, id, lhs, rhs, comment):
        pattern = "    def testCase{}(self):\n        {}({}, {})"
        if rhs == 'True':
            return pattern.format(id, 'self.assertTrue', lhs, comment)
        else:
            return pattern.format(id, 'self.assertFalse', lhs, comment)

    def generate_equals_test_case(self, id, lhs, rhs, comment):
        pattern = "    def testCase{}(self):\n        {}({}, {}, {})"
        return pattern.format(id, 'self.assertEqual', rhs, lhs, comment)

    def generate_test_case(self, line, id):
        unquoted = line.split('\"')
        comment = '\"' + str(unquoted[1]) + '\"'

        assertion = unquoted[-1].split(' ')     # remove comment
        rhs = assertion[-1]

        assertion = assertion[:-1]              # remove rhs
        temp = filter(lambda x: x != '' and x[0].isalpha(), assertion)
        lhs = str(list(temp)[0])

        if rhs == 'True' or rhs == 'False':
            return self.generate_boolean_test_case(id, lhs, rhs, comment)
        else:
            return self.generate_equals_test_case(id, lhs, rhs, comment)

    def write_tests(self):
        template = "teststests tests"
        file_name = self.generate_file_name()
        self._write_file(file_name, template)


def main():
    tg = TestsGenerator('is_prime_test.dsl')
    print(tg.generate_test_cases_all())


if __name__ == '__main__':
    main()

"""
import unittest

{imports}

class {class_name}(unittest.TestCase):
    {docstring}

    {test_cases}

if __name__ == '__main__':
    unittest.main()


    def testCase1(self):
        self.assertTrue(is_prime(7), "7 should noot be prime")

    def testCase{}(self):
        {}({}, {})

"""
