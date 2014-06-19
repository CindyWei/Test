#coding=utf-8
import unittest
import counter

class Mytest(unittest.TestCase):
	def setUp(self):
		self.jsq=counter.Jisuanqi()

	def tearDown(self):
		pass

	def test_jia(self):
		self.assertEqual(self.jsq.jia(1,2), 3)
	def test_jian(self):
		self.assertEqual(self.jsq.jian(5,2), 3)
	def test_cheng(self):
		self.assertEqual(self.jsq.cheng(5,2), 10)
	def test_chu(self):
		self.assertEqual(self.jsq.chu(6,2), 3)

if __name__ == '__main__':
	unittest.main()