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


    def test_assert_eq(self):
        a = 1
        b = 2
        c = 1
        message = 'test'

        self.assertIsNone(prod_assert.assert_eq(a, c))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_eq, a, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_eq, a, b, message=message)
