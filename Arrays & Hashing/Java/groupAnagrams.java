import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class groupAnagrams {
    public List<List<String>> groupAnsagrams(String[] strs) {
        // Create a map to store the sorted version of the word as the key and list of anagrams as values
        Map<String, List<String>> groupAnagram = new HashMap<>();
        
        // Loop through each word in the input array
        for (String word : strs) {
            // Convert the word to a char array, sort it, and convert it back to a string
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);
            
            // If the sorted version of the word is not in the map, create a new entry
            if (!groupAnagram.containsKey(sortedWord)) {
                groupAnagram.put(sortedWord, new ArrayList<>());
            }
            
            // Add the original word to the corresponding anagram list
            groupAnagram.get(sortedWord).add(word);
        }

        // Return the values of the map as a list of lists
        return new ArrayList<>(groupAnagram.values());
    }



    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example input
        String[] input = {"eat", "tea", "tan", "ate", "nat", "bat"};

        // Call the groupAnagrams method
        List<List<String>> result = solution.groupAnagrams(input);

        // Print the result
        for (List<String> group : result) {
            System.out.println(group);
        }
    }
}
