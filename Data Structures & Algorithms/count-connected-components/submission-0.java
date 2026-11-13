class Solution {
    class UFDS {
        private final int[] parents;
        private final int[] size;

        UFDS(int n) {
            parents = new int[n];
            size = new int[n];
            Arrays.fill(size, 1);

            for (int i = 0; i < n; i++) {
                parents[i] = i;
            }
        }

        private int find(int x) {
            if (parents[x] != x) {
                parents[x] = find(parents[x]); // Path compression
            }
            return parents[x];
        }

        private boolean union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);

            if (rootA == rootB) {
                return false;
            }

            // Attach the smaller tree to the larger tree.
            if (size[rootA] < size[rootB]) {
                int temp = rootA;
                rootA = rootB;
                rootB = temp;
            }

            parents[rootB] = rootA;
            size[rootA] += size[rootB];
            return true;
        }
    }
    
    public int countComponents(int n, int[][] edges) {
        UFDS ufds = new UFDS(n);
        int components = n;

        for (int[] edge : edges) {
            if (ufds.union(edge[0], edge[1])) {
                components--;
            }
        }

        return components;
    }
}
