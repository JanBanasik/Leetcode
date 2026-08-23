class Solution:
    def sumGame(self, num: str) -> bool:
        mid = len(num) // 2

        left_sum = sum(int(c) for c in num[:mid] if c != "?")
        right_sum = sum(int(c) for c in num[mid:] if c != "?")

        left_jokers = num[:mid].count("?")
        right_jokers = num[mid:].count("?")

        # Alice wykonuje ostatni ruch => zawsze może zepsuć równość
        if (left_jokers + right_jokers) % 2 == 1:
            return True

        return 2 * (left_sum - right_sum) != 9 * (right_jokers - left_jokers)