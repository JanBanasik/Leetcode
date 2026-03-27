class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n
        for index, row in enumerate(mat):
            if not self.shift(row, index % 2 == 0, k):
                return False
        return True

    def shift(self, arr, rotate_arr, k):
        if rotate_arr:
            arr = arr[::-1]
        l: int = len(arr)
        new_arr = [0 for _ in range(l)]

        for i in range(l):
            new_arr[(i + k) % (l)] = arr[i]
            
        return new_arr == arr 