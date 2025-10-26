# RTU_Programming_Languages_Python_Fall_2025
Python portion of Programming Languages Course at RTU Fall 2025

## 🐍 Python Programming – 5-Week Continuation Course (Revised)

This 5-week course introduces Python to students who have completed the C Programming course and already know C++ and/or Java.  
It emphasizes *translating structured C-style programming into idiomatic Python* and prepares students for data-oriented and scripting tasks.  
Each week includes one **lecture (2×45 min)** and one **lab (2×45 min)**.

## 🧑‍🎓 Student Instructions

1. **Fork** this repository to your own GitHub account.  
2. **Open in GitHub Codespaces** (use “Code → Open with Codespaces”).  
3. Navigate to `src/week1/`. (and other weeks later on) 
4. Complete each task file (`python_lab1_task1.py` … `task4.py`) by replacing TODOs.  
5. Run tests or examples using the terminal (`python src/week1/python_lab1_task1.py`).  
6. **Commit and push** your completed work.  
7. Submit your repository URL and/or source .py files in Moodle (ORTUS on RTU)

---

## 📅 Weekly Overview

| **Week** | **Topic** | **Focus Keywords** |
|-----------|------------|--------------------|
| **1** | Python Basics, Branching & Iteration | syntax, variables, input/output, `if`, `for`, `while`, basic functions |
| **2** | Functions, Strings & Iteration Patterns | parameters, return values, scope, string operations, slicing |
| **3** | Core Data Structures & Functional Tools | lists, tuples, sets, dicts, comprehensions, `map`, `filter`, `zip`, `apply` |
| **4** | File I/O, Modules & Exceptions | reading/writing files, modularity, error handling |
| **5** | Object-Oriented Python & Project Integration | classes, testing, integration with C parser project |

---

## Week 1 – Python Basics, Branching & Iteration

**Lecture**
- Python syntax vs C syntax: indentation, comments, dynamic typing  
- Variables, literals, and basic data types (`int`, `float`, `bool`, `str`)  
- Input/output using `input()` and formatted `print()` (f-strings)  
- Arithmetic and comparison operators  
- Conditional statements (`if`, `elif`, `else`)  
- Loops: `for` and `while` (no nested data structures yet)  
- Basic function definition and calling (`def`, `return`)  

**Lab**
- Convert C arithmetic and looping examples into Python  
- Write a small calculator using user input and branching  
- Create a simple menu-driven program using loops and functions  
- Explore Python’s `range()` and indentation rules  

---

## Week 2 – Functions, Strings & Iteration Patterns

**Lecture**
- Function parameters, return values, and default arguments  
- Local vs global variables; scoping rules  
- String basics and operations: concatenation, repetition, indexing, slicing  
- String methods: `split()`, `join()`, `strip()`, `replace()`, `find()`  
- Iterating through strings and sequences (`for char in string`)  
- Reusable code style: docstrings and comments  

**Lab**
- Implement text-based arithmetic analyzer using functions  
- Write helper functions for counting characters and words  
- Explore string slicing and iteration patterns  
- Practice writing functions that transform and return text results  

---

## Week 3 – Core Data Structures & Functional Tools

**Lecture**
- Lists, tuples, sets, and dictionaries: creation, indexing, iteration  
- Mutability and immutability concepts  
- List methods and slicing  
- Dictionary key–value operations and nested structures  
- Set operations: union, intersection, difference  
- Comprehensions (`list`, `dict`, `set`)  
- Functional programming tools: `map()`, `filter()`, `zip()`, `apply()` (from Pandas preview)  
- When to use loops vs comprehensions vs functional style  

**Lab**
- Build simple datasets (lists/dicts) and compute aggregates  
- Practice comprehensions and transformations  
- Implement frequency counter for arithmetic operators and operands  
- Experiment with `map()` and `filter()` to process lists  

---

## Week 4 – File I/O, Modules & Exceptions

**Lecture**
- Reading/writing text files with `open()` and `with`  
- Basic CSV and JSON handling  
- Organizing code into modules; `import`, `from`, `as`  
- Exception handling: `try`, `except`, `finally`  
- Reusing modular design concepts from C  

**Lab**
- Read/write structured data from files  
- Create helper module `arithutils.py`  
- Handle division-by-zero and invalid inputs gracefully  
- Log program output to file  

---

## Week 5 – Object-Oriented Python & Project Integration

**Lecture**
- Classes and objects; defining `__init__` and instance methods  
- Encapsulation and inheritance basics  
- Magic methods (`__str__`, `__repr__`)  
- Unit testing with `unittest` and `pytest`  
- Integrating C and Python components conceptually (data types, APIs)  

**Lab**
- Implement `Expression` class with evaluation method  
- Write and run unit tests  
- Package project as a module with documentation  
- Bonus: visualize expression tree recursively  

---

## 🧩 Course Outcomes

By the end of the course, students will be able to:

- Write readable, modular Python code using branching, iteration, and functions  
- Work fluently with strings, lists, tuples, sets, and dictionaries  
- Employ comprehensions and functional programming tools for data transformation  
- Handle files and exceptions safely  
- Organize code into reusable modules and classes  
- Integrate and test Python programs effectively  
- Transition smoothly from C-style logic to expressive, idiomatic Python  

