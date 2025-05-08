class Solution {
    private static final int[][] DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.offer(new int[]{0, 0, 0, 0});

        boolean[][] visited = new boolean[n][m];

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int x = current[0], y = current[1], time = current[2], parity = current[3];

            if (x == n - 1 && y == m - 1) return time;
            if (visited[x][y]) continue;

            visited[x][y] = true;

            for (int[] dir : DIRECTIONS) {
                int nx = x + dir[0], ny = y + dir[1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    int nextTime = Math.max(time, moveTime[nx][ny]) + (parity == 0 ? 1 : 2);
                    int nextParity = 1 - parity;
                    pq.offer(new int[]{nx, ny, nextTime, nextParity});
                }
            }
        }
        return -1;
    }
}