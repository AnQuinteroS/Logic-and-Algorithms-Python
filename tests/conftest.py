"""Makes the project folders importable from the tests.

The folders start with a number (01_, 02_), so they cannot be imported
as regular packages. Adding them to sys.path solves it.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for folder in ("01_Algorithmic_Complexity", "02_Static_Code_Analyzer"):
    sys.path.insert(0, os.path.join(ROOT, folder))
