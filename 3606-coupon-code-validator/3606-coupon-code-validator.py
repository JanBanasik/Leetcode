from dataclasses import dataclass

class Coupon:
    def __init__(self, code: str, business_line: str, is_active: bool):
        self.code = code
        self.business_line = business_line
        self.is_active = is_active
    
    def is_coupon_valid(self):
        code_valid = self.is_code_valid() 
        business_line_valid = self.is_business_line_valid()
        return code_valid and business_line_valid and self.is_active
    
    def is_code_valid(self):
        if not self.code:
            return False

        for c in self.code:
            if not (c.isalpha() or c.isdigit() or c == "_"):
                return False
        return True
    
    def is_business_line_valid(self):
        return self.business_line in ["electronics", "grocery", "pharmacy", "restaurant"]
    
    def __lt__(self, other):
        scores = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        if scores[self.business_line] != scores[other.business_line]:
            return scores[self.business_line] < scores[other.business_line]
        return self.code < other.code

    def __repr__(self):
        return f"{self.code=} {self.business_line=} {self.is_active=}\n"

class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        coupons = [Coupon(code, business_line, is_active) for code, business_line, is_active in zip(codes, businessLine, isActive)]
        coupons = [coupon for coupon in coupons if coupon.is_coupon_valid()]

        coupons.sort()
        return [coupon.code for coupon in coupons]