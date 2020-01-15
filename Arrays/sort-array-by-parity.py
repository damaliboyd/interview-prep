# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        newList = []

        for i in A:
            if (i % 2 == 0):
                newList.insert(0,i)
            else:
                newList.append(i)

        return newList
