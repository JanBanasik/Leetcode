class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        hashmap = {}
        stack = []
        for index, value in enumerate(expression):
            if value == '(':
                stack.append(index)
            else:
                hashmap[index] = stack.pop(-1)
        
        tab = {"|": self.parse_or, "&": self.parse_and, "!": self.parse_not}
        
        return self.helper(expression, index, hashmap, tab)
    
    def parse(self, expression, index, hashmap, tab):
        return tab[expression[index]](expression, index + 1, hashmap, tab)

    def parse_or(self, expression ,index, hashmap, tab):
        v = expression[index : hashmap[index] + 1].split(",")
        for val in v:
            if val


    def parse_and(self, expression ,index, hashmap, tab):
    

    def parse_not(self, expression ,index, hashmap, tab):

        