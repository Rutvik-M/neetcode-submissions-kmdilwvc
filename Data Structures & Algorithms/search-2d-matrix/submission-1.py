class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=(rows*cols)-1
        while left <= right:
            mid=(left+right)//2
            r=mid//cols
            c=mid%cols
            mid_val=matrix[r][c]
            if mid_val==target:
                return True
            elif mid_val<target:
                left=mid+1
            else:
                right=mid-1
        return False

        