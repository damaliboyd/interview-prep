#https://leetcode.com/problems/transpose-matrix/submissions/
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transposed = []
        for i in range(len(A[0])):
            transposed_row = []

            for row in A:
                transposed_row.append(row[i])
            transposed.append(transposed_row)
        return transposed
