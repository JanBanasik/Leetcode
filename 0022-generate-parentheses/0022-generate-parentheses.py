class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        def func(arr,left,right,sequence):
            if left > 0:
                func(arr,left-1,right, sequence + "(")
            
            if right > left:
                func(arr,left,right-1,sequence + ")")
            
            if left == 0 and right == 0:
                arr.append(sequence)
        func(arr,n,n,'')
        return arr