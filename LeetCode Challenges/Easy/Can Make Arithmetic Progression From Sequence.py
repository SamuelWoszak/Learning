"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false."""

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]):
        arr = sorted(arr)
        q = arr[1] - arr[0]
        for c in range(1, len(arr)):
            if arr[c] - arr[c - 1] != q:
                return False
        return True
