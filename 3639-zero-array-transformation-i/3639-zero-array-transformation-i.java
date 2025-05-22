class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int[] diffArray = new int[nums.length + 1];
        for(var query : queries) {
            int left = query[0];
            int right = query[1];
            ++diffArray[left];
            --diffArray[right + 1];
        }
        int[] operationCounts = new int[diffArray.length];
        int curr = 0;
        for(int i = 0; i < diffArray.length; i++) {
            curr += diffArray[i];
            operationCounts[i] = curr;
        }

        for(int i = 0; i < nums.length; i++) {
            if(operationCounts[i] < nums[i]) {
                return false;
            }
        }
        return true;
    }
}