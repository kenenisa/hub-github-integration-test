# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.value = 0
        self.one = None
        self.zero = None
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2
        root = TrieNode()
        for num in nums:
            cur = root
            for i in range(max_len,-1,-1):
                if num & (1<<i):
                    if not cur.one:
                        cur.one = TrieNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero =  TrieNode()
                    cur = cur.zero
            cur.value = num
        result = 0
        for num in nums:
            cur = root
            for i in range(max_len,-1,-1):
                if num & (1 << i):
                    if cur.zero:
                        cur = cur.zero
                    else:
                        if cur.one:
                            cur = cur.one
                else:
                    if cur.one:
                        cur = cur.one
                    else:
                        if cur.zero:
                            cur = cur.zero
            result = max(result,num^cur.value)
        return result
        