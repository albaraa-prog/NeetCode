class Solution:
    # Define a method that takes two strings s and t, and returns True if t is an anagram of s, otherwise False
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if the two strings have the same length; if not, they can't be anagrams
        if len(s) != len(t):
            return False
        # Sort both strings and compare them. If they are anagrams, their sorted forms will be identical
        return sorted(s) == sorted(t)

# Test the solution locally
if __name__ == "__main__":
    s = "listen"  # First string
    t = "silent"  # Second string, an anagram of "listen"
    solution = Solution()  # Create an instance of the Solution class
    result = solution.isAnagram(s, t)  # Call the isAnagram method with the two strings
    print(f"Are '{s}' and '{t}' anagrams? {result}")  # Print the result (True or False)
