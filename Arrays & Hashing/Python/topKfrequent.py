# Import necessary libraries
from collections import \
    Counter  # Counter helps to count the frequency of elements
from typing import List  # For type hinting


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element in the nums list
        # 'Counter(nums)' will return a dictionary-like object where keys are elements,
        # and values are their respective frequencies
        mostf = Counter(nums)
        
        # Step 2: Find the k most common elements
        # 'most_common(k)' returns a list of tuples, where each tuple consists of
        # an element and its frequency, sorted in descending order by frequency.
        # Example: most_common(2) might return [(1, 3), (2, 2)] if '1' appears 3 times
        # and '2' appears 2 times.
        m = mostf.most_common(k)
    
        # Step 3: Extract only the elements (ignoring their frequencies)
        # Use a list comprehension to iterate over the list of tuples (i, frequency),
        # where 'i' is the element and 'frequency' is the count. We only care about 'i'.
        result = [i for i, frequency in m]

        # Return the result, which is a list of the top k most frequent elements
        return result

# Example usage to test the solution
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    
    # Define the input list and k value
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    
    # Call the topKFrequent function and print the result
    print(sol.topKFrequent(nums, k))  # Expected output: [1, 2]
