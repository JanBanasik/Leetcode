import java.util.Arrays;

class Solution {
    public int lengthAfterTransformations(String s, int t) {
        int mod = 1_000_000_007;
        long[] counter = new long[26];
        for (char c : s.toCharArray()) {
            counter[c - 'a']++;
        }
        long[] temp;
        for (int i = 0; i < t; i++) {
            temp = new long[26];

            for (int j = 0; j < 25; j++) {
                temp[j + 1] = (temp[j + 1] + counter[j]) % mod;
            }
            temp[0] = (temp[0] + counter[25]) % mod;
            temp[1] = (temp[1] + counter[25]) % mod;

            System.arraycopy(temp, 0, counter, 0, 26);
        }

        long ans = 0;
        for (long el : counter) {
            ans = (ans + el) % mod;
        }
        return (int) ans;
    }
}