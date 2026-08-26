from sortedcontainers import SortedList


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left: int = 0
        beautiful_substrings = SortedList()
        counter: int = 0

        for right in range(len(s)):
            counter += s[right] == "1"

            while counter > k:
                counter -= s[left] == "1"
                left += 1

            if counter == k:
                # leading zeros tylko wydłużają substring
                while s[left] == "0":
                    left += 1

                substring = s[left:right + 1]

                beautiful_substrings.add(
                    (len(substring), substring)
                )

        if not beautiful_substrings:
            return ""

        return beautiful_substrings[0][1]