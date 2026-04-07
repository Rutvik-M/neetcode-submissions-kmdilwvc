class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                popped_index,popped_height=stack.pop()
                curr_area=popped_height*(i-popped_index)
                max_area=max(curr_area,max_area)
                start=popped_index
            stack.append((start,h))
        for i,h in stack:
            curr_area=h*(len(heights)-i)
            max_area=max(curr_area,max_area)
        return max_area
        