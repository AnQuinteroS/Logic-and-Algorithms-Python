import ast
import os
import sys


def run_linter(directory):
    """
    Walks a directory and reports style issues in every .py file.
    Returns the total number of issues found.
    """
    base_dir = os.path.abspath(directory)
    issues_found = 0

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.py'):
                continue

            filepath = os.path.join(root, file)

            # Skip the linter itself to avoid self-validation loops
            if os.path.abspath(filepath) == os.path.abspath(__file__):
                continue

            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                print(f"[{filepath}] Could not be read as UTF-8, skipped.")
                issues_found += 1
                continue

            # 1. Line length validation
            for i, line in enumerate(content.split('\n')):
                if len(line) > 79:
                    print(f"[{filepath}:{i+1}] Line exceeds 79 characters.")
                    issues_found += 1

            # 2. AST parsing for both standard and async functions
            try:
                tree = ast.parse(content)
            except SyntaxError as e:
                print(f"[{filepath}:{e.lineno}] Syntax error: {e.msg}")
                issues_found += 1
                continue

            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Rule: function names should be lowercase (snake_case)
                    if node.name != node.name.lower():
                        print(f"[{filepath}:{node.lineno}] "
                              f"Function '{node.name}' should be lowercase.")
                        issues_found += 1

                # Rule: functions and classes should have a docstring
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                     ast.ClassDef)):
                    if ast.get_docstring(node) is None:
                        print(f"[{filepath}:{node.lineno}] "
                              f"'{node.name}' is missing a docstring.")
                        issues_found += 1

    if issues_found == 0:
        print("Linter passed: 0 issues found.")
    else:
        print(f"Linter finished with {issues_found} issue(s).")

    return issues_found


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    total_issues = run_linter(target_dir)
    sys.exit(1 if total_issues else 0)
