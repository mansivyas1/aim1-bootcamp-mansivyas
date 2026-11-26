# Student Management Module

## Description 
A simple python module to manage student details and marks using Object-Oriented Programming.

## Features
- Store student name and roll number 
- Add marks
- calculate average marks
- Find the highest mark
- Find the lowest mark
- Handle students without marks

## Files
- student_utils.py: Contains the Student class
- test_student_utils.py: Contains pytest test cases

## Requirements 
- python3
- pytest 
- black
- ruff 
- mypy

## Run Tests
'''bash
python -m pytest day5/test_student_utils.py -v'''

## Code Auality Checks
'''bash
python -m black day5/student_utils.py day5/trst_student_utils.py
python -m ruff checks day5/student_utils.py day5/test_student_utils.py
python -m mypy day5/student_utils.py'''
