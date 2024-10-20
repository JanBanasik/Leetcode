class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operands: list[int] = []
        values: list[int] = []
        functions = {"&": self.parseAnd, "|": self.parseOr, "!": self.parseNot}
        for value in expression:
            if value in ["!", "&", "|"]:
                operands.append(value)
            elif value in ["t", "f"]:
                values.append(True if value == "t" else False)
            elif value == "(":
                values.append("(")
            elif value == ")":
                functions[operands.pop(-1)](values)
        return values[0]
        
    def parseAnd(self, values):
        expr = True
        while (curr := values.pop(-1)) != "(":
            expr = expr and curr
        values.append(expr)
    
    def parseOr(self, values):
        expr = False
        while (curr := values.pop(-1)) != "(":
            expr = expr or curr
        values.append(expr)
    
    def parseNot(self, values):
        values.append(not values.pop(-1))
        values.pop(-2)
    

    

