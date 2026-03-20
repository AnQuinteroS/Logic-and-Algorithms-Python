# Algorithmic Complexity Analyzer

## Overview
This repository contains a Python script designed to empirically evaluate and compare the time complexity of different search algorithms. As an engineering student transitioning into Computer Science, I built this tool to visualize the mathematical concepts behind algorithm efficiency, specifically comparing $O(n)$ vs $O(\log n)$ performance.

## The Experiment: Linear Search vs. Binary Search
The core script (`search_analyzer.py`) generates a sorted array of 1,000,000 integers. It then executes a worst-case scenario search (looking for the very last element) using two different methods:

1. **Linear Search $O(n)$:** Iterates through every single element. Simple to implement, but highly inefficient for large datasets.
2. **Binary Search $O(\log n)$:** Repeatedly divides the search space in half. Requires a sorted array but offers exponential performance improvements as the dataset grows.

## How to Run
Ensure you have Python 3.x installed. Run the following command in your terminal:

```bash
python search_analyzer.py