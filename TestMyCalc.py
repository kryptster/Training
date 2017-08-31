import unittest
from MyCalc import *

class TestMyCalcClass(unittest.TestCase):

	def test_sum(self):
		obj = MyCalc()
		self.assertEqual(obj.sum(10,20),30)
		
	def test_sub(self):
		obj = MyCalc()
		self.assertEqual(obj.sub(100,20),80)
		
	def test_mul(self):
		obj = MyCalc()
		self.assertEqual(obj.mul(10,20),200)
		
	def test_div(self):
		obj = MyCalc()
		self.assertEqual(obj.div(20,10),2)

if __name__ == '__main__':
	unittest.main()