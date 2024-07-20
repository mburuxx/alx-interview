# 0x02. Minimum Operations

## Algorithm | Python

### Project Details

**Project Duration:** May 6, 2024, 6:00 AM to May 10, 2024, 6:00 AM  
**Auto Review:** An auto review will be launched at the deadline

For this project, you need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only "Copy All" and "Paste" operations.

### Concepts Needed:

1. **Dynamic Programming**:
    - Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
    - [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)

2. **Prime Factorization**:
    - Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number `n`.
    - [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:polynomial-factorization/x2f8bb11595b61c86:prime-factorization/v/prime-factorization)

3. **Code Optimization**:
    - Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
    - [How to optimize Python code](https://realpython.com/python-performance/)

4. **Greedy Algorithms**:
    - The problem can also be approached with greedy algorithms, choosing the best option at each step.
    - [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)

5. **Basic Python Programming**:
    - Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
    - [Python Functions (Python Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

### Additional Resources

- Mock Technical Interview

### Requirements

- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should be documented
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

### Tasks

#### 0. Minimum Operations

**Mandatory**

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

- **Prototype:** `def minOperations(n)`
- **Returns:** an integer
- **If `n` is impossible to achieve, return 0**

**Example:**

```python
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
