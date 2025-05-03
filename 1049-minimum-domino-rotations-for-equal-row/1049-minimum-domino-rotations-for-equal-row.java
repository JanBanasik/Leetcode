import java.util.*;

class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        Map<Integer,Integer> topsMap = new HashMap<>();
        Map<Integer,Integer> bottomsMap = new HashMap<>();
        for(int top: tops) topsMap.put(top, topsMap.getOrDefault(top, 0) + 1);
        for(int bot: bottoms) bottomsMap.put(bot, bottomsMap.getOrDefault(bot, 0) + 1);

        List<Integer> candidates = new ArrayList<>();

        for(int dominoValue = 1; dominoValue <= 6; dominoValue++) {
            int v1 = topsMap.getOrDefault(dominoValue, 0);
            int v2 = bottomsMap.getOrDefault(dominoValue, 0);
            System.out.println(STR."\{dominoValue} \{v1} \{v2}");
            if (v1 + v2 >=  tops.length) {
                candidates.add(dominoValue);
            }
        }
        System.out.println(candidates);
        return getAns(tops, bottoms, candidates);
    }

    private static int getAns(int[] tops, int[] bottoms, List<Integer> candidates) {
        int ans = Integer.MAX_VALUE;
        boolean goodFit = true;
        for(int candidate: candidates) {
            int swapsTop = 0;
            int swapsBottom = 0;
            for(int i = 0; i < tops.length; ++i) {
                if(tops[i] != candidate && bottoms[i] != candidate) {
                    goodFit = false;
                    break;
                }
                if(tops[i] == candidate && tops[i] != bottoms[i]) {
                    swapsTop++;
                }
                if(bottoms[i] == candidate && bottoms[i] != tops[i]) {
                    swapsBottom++;
                }
            }
            if(goodFit)
                ans = Math.min(ans, Math.min(swapsTop,
                    swapsBottom));
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}