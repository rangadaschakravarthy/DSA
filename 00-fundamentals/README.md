# 00-Fundamentals Module Curriculum & Problem Guide

---

## Level-1: Basic Math & Number Analysis

### Problem 1: Count Digits & Reverse Integer
- **Question**: Given an integer `n`, return the count of digits and its reverse 32-bit signed value.
- **Description / Explanation**: We need to extract digits one by one from right to left using arithmetic modulo `% 10` and division `// 10`.
- **Approach & Logic**:
  1. Initialize `reversed_num = 0`.
  2. While `n > 0`, extract `digit = n % 10`.
  3. Append to reversed integer: `reversed_num = reversed_num * 10 + digit`.
  4. Divide `n //= 10`. Handle 32-bit overflow boundaries $[-2^{31}, 2^{31}-1]$.
- **Sample Input**: `n = 12345`
- **Sample Output**: `Count = 5, Reversed = 54321`
- **Explanation**: 
  - Extraction: 5 -> 4 -> 3 -> 2 -> 1.
  - Reconstructed: `(((5*10 + 4)*10 + 3)*10 + 2)*10 + 1 = 54321`.
- **Python Implementation**: [`level_1_basic_math.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_1_basic_math.py)

### Problem 2: Euclidean GCD & LCM
- **Question**: Calculate the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two positive integers `a` and `b`.
- **Description / Explanation**: Find the largest positive integer that divides both `a` and `b` without remainder, and the smallest integer divisible by both.
- **Approach & Logic**:
  - **Euclidean Algorithm**: $\gcd(a, b) = \gcd(b, a \bmod b)$ until $b = 0$.
  - **LCM Formula**: $\text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$.
- **Sample Input**: `a = 48, b = 18`
- **Sample Output**: `GCD = 6, LCM = 144`
- **Explanation**: 
  - $48 \bmod 18 = 12 \implies \gcd(18, 12)$
  - $18 \bmod 12 = 6 \implies \gcd(12, 6)$
  - $12 \bmod 6 = 0 \implies \gcd = 6$.
  - $\text{LCM} = (48 \times 18) // 6 = 144$.
- **Python Implementation**: [`level_1_basic_math.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_1_basic_math.py)

---

## Level-2: Bitwise Operations Basics

### Problem 1: Power of Two Check
- **Question**: Determine if a given positive integer `n` is a power of two.
- **Description / Explanation**: A power of two in binary representation contains exactly one `1` bit (e.g., $16 = 10000_2$).
- **Approach & Logic**:
  - Property: If `n` is a power of two, `n & (n - 1)` clears the only set bit, resulting in `0`.
- **Sample Input**: `n = 16`
- **Sample Output**: `True`
- **Explanation**: `16` is $10000_2$, `15` is $01111_2$. `10000 & 01111 = 00000` ($0$).
- **Python Implementation**: [`level_2_bit_basics.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_2_bit_basics.py)

### Problem 2: Single Number I
- **Question**: Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single element.
- **Description / Explanation**: We need to find the unique element in $O(N)$ time and $O(1)$ extra space.
- **Approach & Logic**:
  - Use Bitwise XOR (`^`). Properties: $x \oplus x = 0$ and $x \oplus 0 = x$.
  - XORing all elements cancels out duplicates.
- **Sample Input**: `nums = [4, 1, 2, 1, 2]`
- **Sample Output**: `4`
- **Explanation**: $(1 \oplus 1) \oplus (2 \oplus 2) \oplus 4 = 0 \oplus 0 \oplus 4 = 4$.
- **Python Implementation**: [`level_2_bit_basics.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_2_bit_basics.py)

---

## Level-3: Prime Numbers & Sieve of Eratosthenes

### Problem 1: Sieve of Eratosthenes
- **Question**: Generate all prime numbers up to `N`.
- **Description / Explanation**: Efficiently identify all primes $\le N$ faster than checking each number individually.
- **Approach & Logic**:
  1. Create boolean array `is_prime` of size $N+1$ initialized to `True`.
  2. For $p = 2, 3, \dots, \sqrt{N}$: if `is_prime[p]` is True, mark all multiples $p^2, p^2+p, \dots$ as `False`.
  3. Collect all indices that remain `True`.
- **Sample Input**: `N = 30`
- **Sample Output**: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`
- **Explanation**: Multiples of 2 ($4, 6, \dots$), 3 ($9, 12, \dots$), and 5 ($25$) are eliminated.
- **Python Implementation**: [`level_3_prime_sieve.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_3_prime_sieve.py)

---

## Level-4: Fast Exponentiation & Modular Arithmetic

### Problem 1: Binary Exponentiation
- **Question**: Compute $\text{base}^{\text{exp}} \pmod{\text{mod}}$ in $O(\log \text{exp})$ time.
- **Description / Explanation**: Naive multiplication takes $O(\text{exp})$ operations. Binary exponentiation halves the exponent at each step.
- **Approach & Logic**:
  - If `exp` is odd: $\text{res} = (\text{res} \times \text{base}) \bmod \text{mod}$.
  - Square the base: $\text{base} = (\text{base} \times \text{base}) \bmod \text{mod}$.
  - Divide `exp //= 2`.
- **Sample Input**: `base = 2, exp = 10, mod = 1000`
- **Sample Output**: `24`
- **Explanation**: $2^{10} = 1024$. $1024 \bmod 1000 = 24$.
- **Python Implementation**: [`level_4_fast_power.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_4_fast_power.py)

---

## Level-5: Bit Manipulation Tricks

### Problem 1: Single Number II
- **Question**: Every element appears 3 times except for one unique element which appears once. Find that element.
- **Description / Explanation**: Cancel out elements appearing 3 times using bitwise state transitions.
- **Approach & Logic**:
  - Maintain two bitmasks: `ones` and `twos`.
  - `ones = (ones ^ num) & ~twos`
  - `twos = (twos ^ num) & ~ones`
- **Sample Input**: `nums = [2, 2, 3, 2]`
- **Sample Output**: `3`
- **Explanation**: Bit counts for 2 ($10_2$) sum to 3 at bit position 1, resetting `ones` and `twos` to 0 for bit 1. Bit position 0 remains set for 3.
- **Python Implementation**: [`level_5_bit_tricks.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_5_bit_tricks.py)

---

## Level-6: Advanced Combinatorics & Modular Inverses

### Problem 1: Combinations nCr % MOD
- **Question**: Calculate $\binom{n}{r} \pmod{10^9+7}$ efficiently.
- **Description / Explanation**: Compute combination count without large integer overflow using Fermat's Little Theorem for division under modulo.
- **Approach & Logic**:
  - $\binom{n}{r} = \frac{n!}{r!(n-r)!}$.
  - Division by $D \bmod M$ is multiplication by $D^{M-2} \bmod M$ (since $M = 10^9+7$ is prime).
- **Sample Input**: `n = 5, r = 2, mod = 1000000007`
- **Sample Output**: `10`
- **Explanation**: $\frac{5 \times 4}{2 \times 1} = 10$.
- **Python Implementation**: [`level_6_combinatorics.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_6_combinatorics.py)

---

## Level-7: Matrix Exponentiation

### Problem 1: Fast N-th Fibonacci via Matrix Exponentiation
- **Question**: Compute the $N$-th Fibonacci number $F(N) \pmod{10^9+7}$ in $O(\log N)$ time.
- **Description / Explanation**: Use 2x2 matrix recurrence transformation to compute Fibonacci values for $N$ up to $10^{18}$.
- **Approach & Logic**:
  - Matrix Equation: $\begin{pmatrix} F(n+1) & F(n) \\ F(n) & F(n-1) \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n$.
  - Use Binary Exponentiation on 2x2 matrices.
- **Sample Input**: `N = 10`
- **Sample Output**: `55`
- **Explanation**: $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^9 = \begin{pmatrix} 55 & 34 \\ 34 & 21 \end{pmatrix}$.
- **Python Implementation**: [`level_7_matrix_exponentiation.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_7_matrix_exponentiation.py)

---

## Level-8: Advanced Number Theory

### Problem 1: Euler's Totient Function $\phi(N)$
- **Question**: Count the number of positive integers up to $N$ that are coprime to $N$.
- **Description / Explanation**: Find count of $k \in [1, N]$ such that $\gcd(k, N) = 1$.
- **Approach & Logic**:
  - Euler's Product Formula: $\phi(N) = N \prod_{p | N} \left(1 - \frac{1}{p}\right)$ for all distinct prime factors $p$.
- **Sample Input**: `N = 10`
- **Sample Output**: `4`
- **Explanation**: Integers coprime to 10 are $\{1, 3, 7, 9\}$ (count = 4).
- **Python Implementation**: [`level_8_number_theory.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_8_number_theory.py)

---

## Level-9: Extended Euclidean Algorithm & Chinese Remainder Theorem (CRT)

### Problem 1: Extended GCD & Chinese Remainder Theorem
- **Question**: Given moduli $m_1, m_2, \dots, m_k$ (pairwise coprime) and remainders $r_1, r_2, \dots, r_k$, find the smallest non-negative integer $x$ satisfying $x \equiv r_i \pmod{m_i}$.
- **Description / Explanation**: Use Extended Euclidean Algorithm to compute modular inverses and combine modular congruences using CRT.
- **Approach & Logic**:
  - Extended GCD finds $x, y$ such that $a \cdot x + b \cdot y = \gcd(a, b)$.
  - For $x \equiv r_i \pmod{m_i}$, compute total product $M = \prod m_i$, partial product $M_i = M / m_i$, and modular inverse $M_i^{-1} \pmod{m_i}$.
  - $x = \left(\sum r_i \cdot M_i \cdot M_i^{-1}\right) \pmod M$.
- **Sample Input**: 
  - `num = [3, 5, 7]`
  - `rem = [2, 3, 2]`
- **Sample Output**: `23`
- **Explanation**: $23 \equiv 2 \pmod 3$, $23 \equiv 3 \pmod 5$, $23 \equiv 2 \pmod 7$. Smallest positive integer solution is 23.
- **Python Implementation**: [`level_9_chinese_remainder_theorem.py`](file:///c:/Users/chakr/Downloads/DSA/00-fundamentals/level_9_chinese_remainder_theorem.py)

