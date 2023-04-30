import sys
sys.path.append("SUKHRAJAI")
import re
import sympy

def perform_calculation(calculation):
    result = None
    try:
        result = sympy.sympify(calculation)
    except:
        result = "Invalid calculation"
    return result

def parse_expression(message):
    
    match = re.search("\d+\.?\d*[+\-\/\*\^]\d+\.?\d*", message)
    if match:
        
        return match.group()
    else:
        return None