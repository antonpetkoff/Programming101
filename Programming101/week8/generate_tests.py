from functools import reduce


class TestsGenerator:
    def __init__(self, dsl_file_name):
        self.dsl_file_name = dsl_file_name
        self.lines = self._read_file_lines(dsl_file_name)

    def _read_file_lines(self, file_name):
        contents = ""
        with open(file_name, 'r') as read_file:
            contents = read_file.read().strip().split('\n')
            contents = list(filter(lambda x: x != '', contents))
        return contents

    def _write_file(self, file_name, text):
        with open(file_name, 'w') as write_file:
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
        assertions = list(quoted)[1:]

        test_cases = ''
        for i in range(len(assertions)):
            test_cases += self.generate_test_case(assertions[i], i + 1) + '\n'

        return test_cases[:-1]

    def generate_boolean_test_case(self, id, lhs, rhs, comment):
        pattern = "    def testCase{}(self):\n        {}({}, {})\n"
        if rhs == 'True':
            return pattern.format(id, 'self.assertTrue', lhs, comment)
        else:
            return pattern.format(id, 'self.assertFalse', lhs, comment)

    def generate_equals_test_case(self, id, lhs, rhs, comment):
        pattern = "    def testCase{}(self):\n        {}({}, {}, {})\n"
        return pattern.format(id, 'self.assertEqual', rhs, lhs, comment)

    def generate_test_case(self, line, id):
        unquoted = line.replace(', ', ',').split('\"')
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

    def generate_script_source(self):
        template = "import unittest\n\n{}\n\n\nclass {}(unittest.TestCase):\n"
        template += "    {}\n\n{}\nif __name__ == '__main__':\n"
        template += "    unittest.main()\n"

        imports = self.generate_imports()
        docstring = self.generate_docstring()
        class_name = self.generate_class_name()
        test_cases = self.generate_test_cases_all()

        return template.format(imports, class_name, docstring, test_cases)

    def create_tests_script(self):
        file_name = self.generate_file_name()
        source = self.generate_script_source()
        self._write_file(file_name, source)


def main():
    tg = TestsGenerator('is_prime_test.dsl')
    tg.create_tests_script()

if __name__ == '__main__':
    main()
