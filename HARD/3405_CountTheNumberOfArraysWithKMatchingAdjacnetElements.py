"""
You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 109 + 7.
"""

MOD = 10**9 + 7
MX = 10**5

fact = [0] * MX
inv_fact = [0] * MX


def qpow(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    for i in range(MX - 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD

"""
the problem requires us to construct an array of length n, where each number is in the range [1,m], 
and exactly k pairs of adjacent elements are the same. We need to find how many such arrays can be constructed.
in an array of length n, there are n−1 pairs of adjacent elements. 
among these, k pairs must consist of equal adjacent elements, and the remaining n−1−k pairs must consist of different adjacent elements. 
we can treat these n−1−k differing adjacent positions as partitions, which divide the array into n−k contiguous segments, 
where each segment contains identical values.
"""