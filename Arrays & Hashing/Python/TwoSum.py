from typing import List  # Importing List from typing for type annotations


class Solution:
    # Define a method that takes a list of integers and a target integer, and returns the indices of two numbers that add up to the target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numlist = {}  # Initialize an empty dictionary to store the value and its corresponding index
        for index, value in enumerate(nums):  # Iterate over the list with both index and value
            # Check if the complement (target - current value) exists in the dictionary
            if target - value in numlist:
                # If found, return the indices: the index of the complement and the current index
                return [numlist[target - value], index]
            # Otherwise, store the current value and its index in the dictionary
            numlist[value] = index

# Test the solution locally
if __name__ == "__main__":
    nums = [2, 7, 11, 15]  # Example list of numbers
    target = 9  # The target sum we're looking for
    solution = Solution()  # Create an instance of the Solution class
    result = solution.twoSum(nums, target)  # Call the twoSum method with the list and target
    print(f"Indices of numbers that add up to {target}: {result}")  # Print the result (indices of two numbers)
