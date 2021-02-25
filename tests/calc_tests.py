import unittest
from unittest.mock import patch

import calc


class CalcBasicTests(unittest.TestCase):
    @patch('calc.some')
    def test_add(self, mock_obj):
        mock_obj.return_value = 1
        assert mock_obj() == 1

    def test_sub(self):
        assert calc.some() == 1

    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)


@unittest.skip('Skip with decorator')
class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)
