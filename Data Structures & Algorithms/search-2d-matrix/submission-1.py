class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)

        row = rows // 2

        ziel = []

        k1 = 0
        k2 = 0

        while row >= 0 and row < rows:
            l = matrix[row]
            if l[0] <= target and l[-1] >= target:
                ziel = l
                break
            elif l[0] > target:
                row -= 1
                k1 += 1
            elif l[-1] < target:
                row += 1
                k2 += 1
            if k1 > 0 and k2 > 0:
                return False
            
        count = len(ziel) // 2

        t1 = 0
        t2 = 0

        while count >= 0 and count < len(ziel):
            if ziel[count] == target:
                return True
            elif ziel[count] < target:
                count +=1
                t1 += 1
            elif ziel[count] > target:
                count -=1
                t2 += 1
            if t1 > 0 and t2 > 0:
                break

        return False
        




