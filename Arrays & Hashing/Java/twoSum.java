import java.util.HashMap;

public class twoSum {
    public static int[] twooSum(int[] nums, int target) {
        // Create a HashMap to store the number and its index
        HashMap<Integer, Integer> m = new HashMap<>();
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            int x = target - v;
            
            // Check if the complement is already in the HashMap
            if (m.containsKey(x)) {
                return new int[] { m.get(x), i }; // Return the indices of the two numbers
            }
            // Add the current number and its index to the HashMap
            m.put(v, i);
        }
        // Return an empty array if no solution is found
        return new int[0];
    }
    
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twooSum(nums, target);
        
        if (result.length > 0) {
            System.out.println("Indices: " + result[0] + ", " + result[1]);
        } else {
            System.out.println("No solution found.");
        }
    }
}
