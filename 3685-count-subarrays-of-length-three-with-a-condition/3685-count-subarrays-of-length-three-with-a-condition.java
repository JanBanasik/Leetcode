class Solution {
    public int countSubarrays(int[] nums) {
        int n = nums.length;
        int result = 0;

        for(int i = 0; i < n - 2; i ++) {
            double r1 = nums[i] + nums[i + 2];
            double r2 = (double)nums[i + 1] / 2;
            if(r1 == r2) {
                result ++;
                System.out.println(i);
            }
        }
        return result;
    }
}