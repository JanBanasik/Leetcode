class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        dots1 = version1.count(".")
        dots2 = version2.count(".")
        diff = abs(dots1 - dots2)
        if dots1 > dots2:
            for i in range(diff):
                version2 += f".0"
        else:
            for i in range(diff):
                version1 += f".0"
        #print(version1,version2)
        v1 = version1.split(".")
        v2 = version2.split(".")
        #print(v1,v2)
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1 
        return 0