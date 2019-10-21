import logging
import unittest
import calculator.calculator as calculator

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def testExampleStrings(self):
        iExpr = "1*4+3.3/(3+.3)*3(sqrt(4))/(sin(0)+1)"
        self.assertEqual(self.calculator.calculate(iExpr), 10)
        iExpr = "10*e^0*log10(.4*-5/-0.1-10)--abs(-53//10)+-5"
        self.assertEqual(self.calculator.calculate(iExpr), 11) # exactly!

    def testMathErrors(self):
        iExpr = "1/0"
        self.assertRaises(ZeroDivisionError, self.calculator.calculate, iExpr)

        iExpr = "1/sqrt(-1)"
        self.assertRaises(ValueError, self.calculator.calculate, iExpr)

    def testSingleton(self):
        anotherCalculator = calculator.Calculator()
        self.assertIs(self.calculator, anotherCalculator)

if __name__ == '__main__':
    logging.basicConfig(filename='./calculator_test.log', level=logging.DEBUG)
    unittest.main()
