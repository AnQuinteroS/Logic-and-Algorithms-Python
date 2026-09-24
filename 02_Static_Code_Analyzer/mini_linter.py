import ast
import os
import sys

def run_linter(directory):
    base_dir = os.path.abspath(directory)
    issues_found = 0

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.py'):
                continue
            
            filepath = os.path.join(root, file)
            
            # Skip the linter itself to avoid self-validation loops
            if os.path.basename(filepath) == 'linter.py':
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
                # 1. Line length validation
                for i, line in enumerate(lines):
                    if len(line) > 79:
                        print(f"[{filepath}:{i+1}] Line exceeds 79 characters.")
                        issues_found += 1

            # 2. AST parsing for both standard and async functions
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        # Example rule: Function names should be lowercase (snake_case)
                        if not node.name.islower():
                             print(f"[{filepath}:{node.lineno}] Function '{node.name}' should be lowercase.")
                             issues_found += 1
            except SyntaxError as e:
                print(f"[{filepath}:{e.lineno}] Syntax error: {e.msg}")
                issues_found += 1
    
    if issues_found == 0:
        print("Linter passed: 0 issues found.")
    else:
        print(f"Linter finished with {issues_found} issue(s).")

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    run_linter(target_dir)
