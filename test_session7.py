import pytest
from session7 import *

def test_fifty_docstring1():
	assert fifty_docstring(fifty_docstring) == True #This docstring has 50 characters.

def test_fifty_docstring2():
	assert fifty_docstring(outer_fibo) == True #This docstring has 50 characters.

def test_fifty_docstring3():
	assert fifty_docstring(counter) == False #This docstring does not has 50 characters.

def test_fifty_docstring4():
	assert fifty_docstring(seperate_counter) == False #This docstring does not has 50 characters.

def test_outer_fibo1():
	nextFibonacci1 = outer_fibo()
	assert nextFibonacci1(2,3) == 5 #The number after 3 should be 5 in fibonacci series

def test_outer_fibo2():
	nextFibonacci2 = outer_fibo()
	assert nextFibonacci2(0,0) == 1 #Since b is 0, it's value is made 1 and and 0 + 1 = 1 is returned in the series

def test_counter1():
	c_add = counter(add)
	x = c_add(4,7)
	assert counters['add'] == 1 #Since add is called just once

def test_counter2():
	c_mul = counter(mul)
	x = c_mul(2,8)
	assert counters['mul'] == 1 #Since mul is called once

def test_counter3():
	c_div = counter(div)
	x = c_div(6,7)
	assert counters['div'] == 1 #Since div is called just once

def test_counter4():
	c_add = counter(add)
	for i in range(2):
		x = c_add(4,6)
	assert counters['add'] == 2 #Since add is called twice

def test_counter5():
	c_mul = counter(mul)
	for i in range(5):
		x = c_mul(3,9)
	assert counters['mul'] == 5 #Since mul is called 5 times

def test_counter6():
	c_div = counter(div)
	for i in range(11):
		x = c_div(4,2)
	assert counters['div'] == 11 #Since div is called 11 times

def test_seperate_counter1():
	c_add = seperate_counter(add)
	x = c_add(4,6)
	assert add_counter['add'] == 1 #Since add is called just once

def test_seperate_counter2():
	c_mul = seperate_counter(mul)
	x = c_mul(11,5)
	assert mul_counter['mul'] == 1 #Since mul is called once

def test_seperate_counter3():
	c_div = seperate_counter(div)
	x = c_div(65,5)
	assert div_counter['div'] == 1 #Since div is called just once

def test_seperate_counter4():
	c_add = seperate_counter(add)
	for i in range(3):
		x = c_add(23,9)
	assert add_counter['add'] == 3 #Since add is called thrice

def test_seperate_counter5():
	c_mul = seperate_counter(mul)
	for i in range(7):
		x = c_mul(23,9)
	assert mul_counter['mul'] == 7 #Since mul is called seven times


def test_seperate_counter6():
	c_div = seperate_counter(div)
	for i in range(30):
		x = c_div(100,2)
	assert div_counter['div'] == 30 #Since div is called 30 times
