"""Example Python file with various code quality issues for testing."""

import os
import pickle
import sqlite3

# Security issue: hardcoded secret
API_KEY = "skskkskkskkskkkskkskkskksksksksk"

# Performance issue: inefficient loop
def slow_function(data):
    result = []
    for i in range(len(data)):  # Should use enumerate
        for j in range(len(data)):  # Nested loop - O(n²)
            if data[i] == data[j]:
                result.append(data[i])
    return result

# Complexity issue: high cyclomatic complexity
def complex_function(x, y, z, a, b, c):
    if x > 0:
        if y > 0:
            if z > 0:
                if a > 0:
                    if b > 0:
                        if c > 0:
                            return "all positive"
                        else:
                            return "c not positive"
                    else:
                        return "b not positive"
                else:
                    return "a not positive"
            else:
                return "z not positive"
        else:
            return "y not positive"
    else:
        return "x not positive"

# Security issue: SQL injection vulnerability
def get_user_data(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchall()

# Security issue: unsafe deserialization
def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)  # Unsafe!

# Documentation issue: missing docstring
def undocumented_function(param1, param2):
    return param1 + param2

# Code duplication
def calculate_area_rectangle(length, width):
    if length <= 0:
        raise ValueError("Length must be positive")
    if width <= 0:
        raise ValueError("Width must be positive")
    return length * width

def calculate_area_square(side):
    if side <= 0:
        raise ValueError("Side must be positive")  # Duplicated validation logic
    return side * side

# Performance issue: string concatenation in loop
def build_string(items):
    result = ""
    for item in items:
        result += str(item) + ", "  # Inefficient string concatenation
    return result

# Best practice issue: bare except
def risky_function():
    try:
        # Some risky operation
        result = 10 / 0
        return result
    except:  # Bare except is bad practice
        return None

# Missing error handling
def divide_numbers(a, b):
    return a / b  # No check for division by zero

# Long function (maintainability issue)
def very_long_function():
    # This function is too long and does too many things
    data = []
    for i in range(100):
        data.append(i)
    
    processed = []
    for item in data:
        if item % 2 == 0:
            processed.append(item * 2)
        else:
            processed.append(item * 3)
    
    filtered = []
    for item in processed:
        if item > 50:
            filtered.append(item)
    
    sorted_data = sorted(filtered)
    
    final_result = []
    for item in sorted_data:
        final_result.append(str(item))
    
    return ", ".join(final_result)

# Class without docstring
class UndocumentedClass:
    def __init__(self, value):
        self.value = value
    
    def method_without_docstring(self):
        return self.value * 2

if __name__ == "__main__":
    # Example usage with potential issues
    print(slow_function([1, 2, 3, 2, 1]))
    print(complex_function(1, 2, 3, 4, 5, 6))
    print(undocumented_function(5, 10))
