class Solution:
    @staticmethod
    def find_index(inlist, target):
        for i in range(len(inlist)):
            for j in range(len(inlist)):
                if inlist[i] + inlist[j] == target and inlist[i] != inlist[j]:
                    print(f"[{i}, {j}]")
                    return [i, j]

        return None


if __name__ == "__main__":
    obj = Solution()
    obj.find_index([4, 5, 7, 9, 2], 18)
