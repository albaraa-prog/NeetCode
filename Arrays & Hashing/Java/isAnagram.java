import java.util.Arrays;

class isAnagram {
    public boolean isAnagraam(String s, String t) {
        // If the lengths are not equal, they can't be anagrams
        if (s.length() != t.length()) {
            return false;
        } else {
            // Convert both strings to character arrays
            char[] charS = s.toCharArray();
            char[] charT = t.toCharArray();

            // Sort both character arrays
            Arrays.sort(charS);
            Arrays.sort(charT);

            // Use Arrays.equals() to check if the sorted arrays are the same
            return Arrays.equals(charS, charT);
        }
    }

    public static void main(String[] args) {
        // Test case
        isAnagram solution = new isAnagram();
        String s1 = "listen";
        String s2 = "silent";

        System.out.println("Is Anagram: " + solution.isAnagraam(s1, s2));  // Should return true
    }
}
