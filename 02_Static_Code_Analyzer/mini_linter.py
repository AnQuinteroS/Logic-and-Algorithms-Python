import ast

def check_line_lengths(code_lines, max_length=79):
    """
    Evaluates each line of code to ensure it complies with PEP 8 length limits.
    Time Complexity: O(n) where n is the number of lines.
    """
    issues = []
    for i, line in enumerate(code_lines):
        # PEP 8 recommends a maximum line length of 79 characters for optimal readability
        if len(line) > max_length:
            issues.append(f"Line {i + 1} is too long ({len(line)} > {max_length} characters).")
    return issues

def check_docstrings(code_string):
    """
    Parses the code using an Abstract Syntax Tree (AST) to identify missing docstrings 
    in functions and classes. This is much safer and more accurate than using Regex.
    """
    issues = []
    try:
        # Parse the code into an AST node
        tree = ast.parse(code_string)
        
        # Iterate through all nodes in the parsed tree
        for node in ast.walk(tree):
            # Check if the node is a Function or a Class
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                # If there's no docstring (the first statement isn't a string literal)
                if not ast.get_docstring(node):
                    node_type = "Function" if isinstance(node, ast.FunctionDef) else "Class"
                    issues.append(f"Missing docstring in {node_type} '{node.name}'.")
    except SyntaxError as e:
        issues.append(f"Critical Error: Code contains invalid Python syntax -> {e}")
        
    return issues

def analyze_code(file_path):
    """
    Main function acting as the 'evaluator'. It reads a target Python file
    and runs the analytical checks, outputting a review report.
    """
    print(f"--- Starting Static Code Analysis for: {file_path} ---\n")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            code_string = file.read()
            code_lines = code_string.splitlines()
            
            # 1. Run length checks
            length_issues = check_line_lengths(code_lines)
            
            # 2. Run AST docstring checks
            docstring_issues = check_docstrings(code_string)
            
            # Compile and print the report
            total_issues = len(length_issues) + len(docstring_issues)
            
            if total_issues == 0:
                print("✅ Perfect! The code strictly follows our targeted PEP 8 guidelines.")
            else:
                print(f"⚠️ Found {total_issues} style/logic issue(s) to fix:\n")
                for issue in length_issues + docstring_issues:
                    print(f" - [Style Warning]: {issue}")
                    
    except FileNotFoundError:
        print(f"Error: Could not locate the file '{file_path}'. Please check the path.")

if __name__ == "__main__":
    # For demonstration purposes, we will instruct the linter to analyze its own code.
    # A perfectly compliant script should output 0 issues.
    target_file = "mini_linter.py" 
    analyze_code(target_file)
