"""Check connection configuration and safe route parameter binding without a DB."""
import os
from unittest.mock import MagicMock, patch
import unittest
from dbhelper import DB

class DatabaseContractTests(unittest.TestCase):
    def test_config_uses_process_environment(self):
        values = {'MYSQL_HOST': 'test-host', 'MYSQL_USER': 'test-user',
                  'MYSQL_PASSWORD': 'test-only', 'MYSQL_DATABASE': 'test-database'}
        with patch.dict(os.environ, values), patch('mysql.connector.connect') as connect:
            DB()
            self.assertEqual(connect.call_args.kwargs, {
                'host': 'test-host', 'user': 'test-user',
                'password': 'test-only', 'database': 'test-database'})

    def test_route_inputs_are_bound_separately_from_sql(self):
        with patch.dict(os.environ, {'MYSQL_PASSWORD': 'test-only'}), patch('mysql.connector.connect') as connect:
            cursor = connect.return_value.cursor.return_value
            cursor.fetchall.return_value = []
            database = DB()
            attack = "Delhi' OR 1=1 --"
            self.assertEqual(database.fetch_all_flights(attack, 'Mumbai'), [])
            sql, parameters = cursor.execute.call_args.args
            self.assertNotIn(attack, sql)
            self.assertEqual(parameters, (attack, 'Mumbai'))

if __name__ == '__main__':
    unittest.main()
