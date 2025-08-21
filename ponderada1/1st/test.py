import unittest
import mean

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean.calculate([31,46,80,24,11,55,60,90,101])
        expected = {'mean': [[38.333333333333336, 49.0, 78.66666666666667], [52.333333333333336, 30.0, 83.66666666666667], 55.333333333333336], 'variance': [[242.8888888888889, 1044.6666666666667, 353.5555555555555], [420.22222222222223, 340.6666666666667, 300.22222222222223], 838.2222222222222], 'standard deviation': [[15.584892970081281, 32.321303604073066, 18.803073034893938], [20.499322482029065, 18.457157599876172, 17.326921891156037], 28.95206766747795], 'max': [[60, 90, 101], [80, 55, 101], 101], 'min': [[24, 11, 55], [31, 11, 60], 11], 'sum': [[115, 147, 236], [157, 90, 251], 498]}
        self.assertAlmostEqual(actual, expected, "A função 'calculate()' deveria ter retornado '[31,46,80,24,11,55,60,90,101]'")

    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(ValueError, "A lista esta pequena, deve conter nove números.", mean.calculate, [2,6,2,8,4,0,1,])

if __name__ == "__main__":
    unittest.main()
