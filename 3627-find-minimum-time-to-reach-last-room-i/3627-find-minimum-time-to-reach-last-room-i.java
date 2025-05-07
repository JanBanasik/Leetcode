import java.util.*;

class Solution {

    public int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;

        // Dijkstra: min-heap – mniejsze czasy mają wyższy priorytet
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.add(new int[]{0, 0, 0});

        boolean[][] visited = new boolean[n][m];

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int x = cur[0], y = cur[1], time = cur[2];

            if (x == n - 1 && y == m - 1) return time;
            if (visited[x][y]) continue;
            visited[x][y] = true;

            for (int[] d : directions) {
                int nx = x + d[0];
                int ny = y + d[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    int newTime = Math.max(time + 1, moveTime[nx][ny] + 1);
                    pq.add(new int[]{nx, ny, newTime});
                }
            }
        }

        return -1;
    }
}
