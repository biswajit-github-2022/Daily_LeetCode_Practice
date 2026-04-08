# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            nums.insert(0,nums.pop(-1))
        