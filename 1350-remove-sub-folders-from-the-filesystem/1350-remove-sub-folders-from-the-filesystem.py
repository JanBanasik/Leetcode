class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders = sorted(folders, key = lambda x: (len(x), x))
        result: set[str] = set()

        for folder in folders:
            temp: str = str()
            flag: bool = True
            for index, value in enumerate(folder):
                temp += value
                if value == "/" and temp[:-1] in result:
                    flag = False
                    break
            if flag:
                result.add(folder)
        
        return list(result)