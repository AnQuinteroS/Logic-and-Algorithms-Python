# Python Logic, Algorithms, and Code Quality

[![Tests](https://github.com/AnQuinteroS/Logic-and-Algorithms-Python/actions/workflows/tests.yml/badge.svg)](https://github.com/AnQuinteroS/Logic-and-Algorithms-Python/actions/workflows/tests.yml)

## Introduction
This repository serves as a professional portfolio demonstrating my core competencies in Python programming, algorithmic efficiency, and software best practices. As a student at Universidad Nacional de Colombia transitioning into Computer Science, I focus on building tools that are not only functional but also optimized and well-documented.

## Repository Structure

### 1. [Algorithmic Complexity Analyzer](./01_Algorithmic_Complexity/)
A performance-testing suite that compares **Linear Search $O(n)$** vs. **Binary Search $O(\log n)$**. 
* **Key Concept:** Empirical proof of algorithmic scalability using Large Datasets (1,000,000+ elements).

### 2. [Static Code Analyzer (Mini-Linter)](./02_Static_Code_Analyzer/)
A tool built using Python's **Abstract Syntax Tree (AST)** module to automate code reviews.
* **Key Concept:** Static analysis for PEP 8 compliance and documentation standards.

## Running the Tests
The project is covered by a `pytest` suite that runs automatically on every push through GitHub Actions (Python 3.10, 3.11 and 3.12).

```bash
pip install -r requirements-dev.txt
pytest
```

---
**Contact:** Andres Quintero - anquinteros@unal.edu.co
