# TSAI_EPAi3.0

# Project Description:

	This repository contains the session 7 assignment on Scopes and Closures. This assignment consists of solution for following four problem statements:

		-  a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable 
		- a closure that gives the next fibonacci number
		- a new closure that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts
		- Modify above such that now we can pass in different dictionary variables to update different dictionaries

	Test cases are written accordignly for every problem statement in test_session7.py file.

# Closures : 
	A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 

# Table of contents :
-TSAI_EPAi3.0-main
	- .github
		- workflow
			- ci.yml
	-.gitignore
	-requirements.txt
	-session7.py
	-test_session7.py

# Installation : 
	
**$ git clone https://github.com/aarushikankanmeli97/TSAI_EPAi3.0.git**
**$ cd TSAI_EPAi3.0**
**$ pip3 install requirements.txt**

# To run the Program :

**$ python session7.py**

# To run the test cases : 

**$ python3 py.test**