import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    Map<Integer, String> m = new HashMap<>() {{
        put(1, "equilateral");
        put(2, "isosceles");
        put(3, "scalene");
    }};
    public String triangleType(int[] nums) {
        return canConstructTriangle(nums) ? m.getOrDefault((int) Arrays.stream(nums).distinct().count(), null) : "none";
    }

    private boolean canConstructTriangle(int[] nums) {
        return (nums[0] + nums[1] > nums[2])
                && (nums[1] + nums[2] > nums[0])
                && (nums[2] + nums[0] > nums[1]);
    }
}