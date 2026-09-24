# Python Static Style Analyzer (Mini-Linter)

## Overview
This repository contains a custom Python static code analyzer. It was built to demonstrate an understanding of Python's Abstract Syntax Tree (`ast` module) and the importance of code readability, maintainability, and PEP 8 compliance.

In the context of AI evaluation and Large Language Model (LLM) training, ensuring that generated code is not only functionally correct but also stylistically sound is critical. This script automates the detection of common human and AI formatting errors.

## Features
1. **Line Length Validation:** Iterates through the raw text to flag lines exceeding the PEP 8 recommended 79-character limit.
2. **AST-Based Docstring Detection:** Instead of relying on fragile Regular Expressions, this tool safely parses the code into an Abstract Syntax Tree to accurately detect classes and functions that lack proper documentation strings.

## How to Run
Ensure you have Python 3.x installed. No external libraries are required as it uses native Python modules.

```bash
python mini_linter.py