import unittest
from unittest.mock import patch

from package.classes_2 import TableFormatter, Table


class TestClassesRenderer(unittest.TestCase):
    def test_to_csv(self):
        with patch.object(Table, 'get_table',
                          return_value=[[1, 2, 3], [4, 5, 6]]):
            renderer = TableFormatter(Table(3))
            result = renderer.to_csv()
        self.assertEqual(result, "1,2,3\n4,5,6")
