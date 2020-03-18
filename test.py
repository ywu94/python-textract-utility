import unittest
import textractutil

class parametrizedTestCase(unittest.TestCase):
	def __init__(self, methodName="runTest", **kwargs):
		"""
		Any parameterized tests should inherit this class
		"""
		super(parametrizedTestCase, self).__init__(methodName)
		self.kwargs = kwargs

	@staticmethod
	def parametrize(testcase_class, **kwargs):
		"""
		Create a suite containing all tests taken from the given subclass, passing them the parameter "param".
		"""
		test_names = unittest.TestLoader().getTestCaseNames(testcase_class)
		suite = unittest.TestSuite()
		for name in test_names:
			suite.addTest(testcase_class(methodName=name, **kwargs))
		return suite

class textractutil_test(parametrizedTestCase):
	def test_get_text(self):
		# Bypass test for now, will add later.
		self.assertEqual(1,1)

test_cases = [{}]

if __name__ == "__main__":
	for test_case in test_cases:
		suite = unittest.TestSuite()
		suite.addTest(parametrizedTestCase.parametrize(textractutil_test, **test_case))
		unittest.TextTestRunner().run(suite)