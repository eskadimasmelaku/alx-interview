# 0x0A. Prime Game

## Description
This project involves solving a competitive game scenario using Python. The game is played between two players, Maria and Ben, who take turns choosing prime numbers and removing those primes along with their multiples from a set of consecutive integers. The project focuses on leveraging knowledge of **prime numbers**, **game theory**, and **algorithm optimization**.

The goal is to determine the winner of multiple rounds of the game and return the name of the player who won the most rounds.

---

## Learning Objectives
- Understanding and implementing algorithms to identify prime numbers.
- Utilizing the **Sieve of Eratosthenes** for efficient prime number calculation.
- Applying basic principles of **game theory** for optimal decision-making.
- Using **dynamic programming/memoization** to optimize the solution.
- Writing Python code adhering to **PEP 8** style guidelines.

---

## Requirements
- **Language**: Python 3.4.3
- **OS**: Ubuntu 20.04 LTS
- **Editor**: `vi`, `vim`, or `emacs`
- **Code style**: PEP 8 (version 1.7.x)
- **File**: Each file must be executable and end with a new line.
- **Shebang**: The first line of all files should be `#!/usr/bin/python3`.

---

## Tasks

### Task 0: Prime Game
#### Description:
Maria and Ben play `x` rounds of the game, where `n` (the size of the set) may vary for each round. Assuming Maria always goes first, and both players play optimally:
- Return the name of the player that won the most rounds.
- If no winner can be determined, return `None`.

#### Function Prototype:
```python
def isWinner(x, nums):

