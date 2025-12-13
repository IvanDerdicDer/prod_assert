import unittest
import prod_assert


class TestProdAssert(unittest.TestCase):

    def test_prod_assert(self):
        condition_true = True
        condition_false = False
        condition_fail = 1
        message = "Condition is false."
        message_fail = 1
        
        self.assertIsNone(prod_assert.prod_assert(condition_true, message))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.prod_assert, condition_false, message)
        self.assertRaises(ValueError, prod_assert.prod_assert, condition_fail, message)
        self.assertRaises(ValueError, prod_assert.prod_assert, condition_true, message_fail)
