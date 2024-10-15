import java.util.HashSet;

class hasDuplicate {
    // Method to check for duplicates
    public boolean hasDuplicaate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for (int i : nums) {
            if (set.contains(i)) {
                return true; // Duplicate found
            } else {
                set.add(i);
            }
        }
        return false; // No duplicates
    }

    public static void main(String[] args) {
        // Create an instance of hasDuplicate
        hasDuplicate checker = new hasDuplicate();

        // Sample arrays to test
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {1, 2, 3, 4, 4};

        // Check for duplicates
        System.out.println("Array 1 has duplicates: " + checker.hasDuplicaate(array1)); // Should return false
        System.out.println("Array 2 has duplicates: " + checker.hasDuplicaate(array2)); // Should return true
    }
}
