from collections import \
    defaultdict  # Import defaultdict from collections for easier handling of lists
from typing import List  # Import List from typing for type hinting

# Problem: Group Anagrams
# Given an array of strings 'strs', group the anagrams together. 
# You can return the answer in any order.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

class Solution:
    # Define a method that takes a list of strings and returns a list of lists of anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Initialize a dictionary to store lists of anagrams
        
        for word in strs:  # Loop through each word in the input list
            # Sort the word to use as a key; anagrams will have the same sorted representation
            sorted_word = ''.join(sorted(word))  
            # Append the original word to the list in the dictionary corresponding to the sorted key
            anagram_map[sorted_word].append(word)
        
        # Return the values of the dictionary as a list of lists (the grouped anagrams)
        return list(anagram_map.values())
      






# Example usage:
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]  # Example input list of strings
    solution = Solution()  # Create an instance of the Solution class
    result = solution.groupAnagrams(strs)  # Call the groupAnagrams method with the input list
    print(result)  # Print the grouped anagrams
