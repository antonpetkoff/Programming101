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

        result = self.generate_test_case(test_cases[1], 2)
        print(result)

    def choose_assertion(self, argument):
        if argument == 'True':
            return 'self.assertTrue'
        elif argument == 'False':
            return 'self.assertFalse'
        return 'self.assertEqual'

    def generate_test_case(self, line, id):
        pattern = "    def testCase{}(self):\n        {}({}, {})"
        unquoted = line.split('\"')
        comment = '\"' + str(unquoted[1]) + '\"'    # ok
        assertion = unquoted[-1].split(' ')     # remove comment
        rhs = assertion[-1]                     # ok
        assertion = assertion[:-1]              # remove assert_result
        temp = filter(lambda x: x != '' and x[0].isalpha(), assertion)
        lhs = str(list(temp)[0])                # ok
        assert_type = ''

        if rhs == 'True':
            assert_type = 'self.assertTrue'
            return pattern.format(id, assert_type, lhs, comment)
        elif rhs == 'False':
            assert_type = 'self.assertFalse'
            return pattern.format(id, assert_type, lhs, comment)
        else:
            assert_type = 'self.assertEqual'

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
