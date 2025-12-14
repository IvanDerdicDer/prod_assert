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
        self.assertIsNone(prod_assert.prod_assert(condition_true, message, AssertionError))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.prod_assert, condition_false, message)
        self.assertRaises(AssertionError, prod_assert.prod_assert, condition_false, message, AssertionError)
        self.assertRaises(ValueError, prod_assert.prod_assert, condition_fail, message)
        self.assertRaises(ValueError, prod_assert.prod_assert, condition_true, message_fail)
        self.assertRaises(ValueError, prod_assert.prod_assert, condition_true, message_fail, ValueError)


    def test_assert_eq(self):
        a = 1
        b = 2
        c = 1
        message = 'test'

        self.assertIsNone(prod_assert.assert_eq(a, c))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_eq, a, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_eq, a, b, message=message)


    def test_assert_not_eq(self):
        a = 1
        b = 1
        c = 2
        message = 'test'

        self.assertIsNone(prod_assert.assert_not_eq(a, c))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_not_eq, a, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_not_eq, a, b, message=message)


    def test_assert_true(self):
        a = True
        b = False
        c = 2
        message = 'test'

        self.assertIsNone(prod_assert.assert_true(a))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_true, b)
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_true, c)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_true, b, message=message)


    def test_assert_false(self):
        a = False
        b = True
        c = 2
        message = 'test'

        self.assertIsNone(prod_assert.assert_false(a))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_false, b)
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_false, c)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_false, b, message=message)


    def test_assert_is(self):
        a = 1
        b = 2
        c = a
        message = 'test'

        self.assertIsNone(prod_assert.assert_is(a, c))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_is, a, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_is, a, b, message=message)


    def test_assert_is_not(self):
        a = 1
        b = a
        c = 2
        message = 'test'

        self.assertIsNone(prod_assert.assert_is_not(a, c))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_is_not, a, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_is_not, a, b, message=message)


    def test_assert_is_none(self):
        a = None
        b = 2
        message = 'test'

        self.assertIsNone(prod_assert.assert_is_none(a))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_is_none, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_is_none, b, message=message)


    def test_assert_is_not(self):
        a = 1
        b = None
        message = 'test'

        self.assertIsNone(prod_assert.assert_is_not_none(a))
        self.assertRaises(prod_assert.AssertionFailed, prod_assert.assert_is_not_none, b)
        self.assertRaisesRegex(prod_assert.AssertionFailed, message, prod_assert.assert_is_not_none, b, message=message)

