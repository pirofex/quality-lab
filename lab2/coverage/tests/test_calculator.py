import unittest
from calculator import parser
import calculator.converter as converter
import calculator.evaluator as evaluator

class TestEvaluate(unittest.TestCase):
    def setUp(self):
        self.parser = parser.Parser()
        self.converter = converter.Converter()
        self.evaluator = evaluator.Evaluator()

    def evaluate(self, iExpr):
        parsedExpr = self.parser.parse(iExpr)
        convertedExpr = self.converter.convert(parsedExpr)
        evaluatedExpr = self.evaluator.evaluate(convertedExpr)
        return evaluatedExpr

    def testArithmetical(self):
        self.assertEqual(self.evaluate("3+2"), 5)
        self.assertEqual(self.evaluate("3-2"), 1)
        self.assertEqual(self.evaluate("3*2"), 6)
        self.assertEqual(self.evaluate("3/2"), 1.5)
        self.assertEqual(self.evaluate("3//2"), 1)
        self.assertEqual(self.evaluate("3%2"), 1)
        self.assertEqual(self.evaluate("3^2"), 9)

if __name__ == '__main__':
    unittest.main()
