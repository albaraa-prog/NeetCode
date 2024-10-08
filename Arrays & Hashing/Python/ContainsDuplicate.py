from typing import \
    List  # Importing the List type from the typing module to specify the type of list argument


class Solution:
    # Define a method that takes a list of integers and returns True if there are duplicates, otherwise False
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Initialize an empty set to store the unique elements from the list
        for num in nums:  # Loop through each number in the list
            if num in seen:  # If the number is already in the set, it means it's a duplicate
                return True  # Return True immediately when a duplicate is found
            seen.add(num)  # If the number is not in the set, add it to the set
        return False  # After checking all numbers, if no duplicates were found, return False

# Test the solution locally
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 3]  # Example input list with a duplicate (3)
    solution = Solution()  # Create an instance of the Solution class
    result = solution.hasDuplicate(nums)  # Call the hasDuplicate method with the input list
    print(f"Does the list have duplicates? {result}")  # Print the result (True or False)
