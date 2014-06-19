#coding=utf-8
from widget import Widget
import unittest

class WidgetTestCase(unittest.TestCase):
	
	def setUp(self):
		self.widget=Widget()
	
	def testSize(self):
		self.assertEqual(self.widget.getSize(), (40,40))

	def testresize(self):
		self.widget.resize(100, 100)
		self.assertEqual(self.widget.getSize(), (100, 100))

    
	def tearDown(self):
		self.widget.dispose()
		self.widget=None
"""
#构造用例集（2种方法）
方法1：
def suite():
	suite = unittest.TestSuite()
	suite.addTest(WidgetTestCase("testSize"))
	suite.addTest(WidgetTestCase("testresize"))
	return suite

方法2：前提是测试用例以test开头
def suite():
	return unittest.makeSuite(WidgetTestCase, "test")

#执行用例集（2种方法）
方法1：
if __name__ == "__main__":
	unittest.main(defaultTest='suite')
方法2：前提是测试用例以test开头
if __name__ == "__main__":
	unittest.main()
"""

if __name__ == "__main__":
	#构造测试用例集
	suite=unittest.TestSuite()
	suite.addTest(WidgetTestCase("testSize"))
	suite.addTest(WidgetTestCase("testresize"))
	#执行用例集合
	runner = unittest.TextTestRunner()
	runner.run(suite)


