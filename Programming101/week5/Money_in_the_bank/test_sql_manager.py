import unittest
import sql_manager


class SQLManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()

    def test_sql_injection(self):
        if sql_manager.login("test", "test") is False:
            sql_manager.register("test", "test")
        self.assertFalse(sql_manager.login("\' OR 1 = 1 --", "random"))

if __name__ == '__main__':
    unittest.main()
