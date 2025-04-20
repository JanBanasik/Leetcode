import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        Map<Integer, List<Integer>> m = new HashMap<>();

        for(int i = 0; i < groupSizes.length; i++) {
            int group = groupSizes[i];
            if(!m.containsKey(group)) {
                m.put(group, new ArrayList<>());
            }
            m.get(group).add(i);

        }
        List<List<Integer>> res = getLists(m);
        
        return res;
    }

    private static List<List<Integer>> getLists(Map<Integer, List<Integer>> m) {
        List<List<Integer>> res = new ArrayList<>();
        for(Map.Entry<Integer, List<Integer>> entry : m.entrySet()) {
            int groupLength = entry.getKey();
            List<Integer> list = entry.getValue();
            List<Integer> temp = new ArrayList<>();
            for (Integer integer : list) {
                temp.add(integer);

                if (temp.size() == groupLength) {
                    res.add(temp);
                    temp = new ArrayList<>();
                }
            }
        }
        return res;
    }
}
