from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:

    def swap(self, s:str, i:int, j:int) -> str:
        r=list(s)
        (r[i],r[j])=(r[j],r[i])
        return "".join(r)

    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        # Step 1: Union connected indices
        for a, b in pairs:
            uf.union(a, b)

        # Step 2: Group indices by their root
        components = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            components[root].append(i)

        # Step 3: Sort characters within each component
        res = list(s)
        for indices in components.values():
            chars = sorted(res[i] for i in indices)
            for i, ch in zip(sorted(indices), chars):
                res[i] = ch

        return ''.join(res)
    
if __name__ == "__main__":
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    solution = Solution()
    print(solution.smallestStringWithSwaps(s, pairs))  # Output: "abcd"
    s= "vbjjxgdfnru"
    pairs = [[8,6],[3,4],[5,2],[5,5],[3,5],[7,10],[6,0],[10,0],[7,1],[4,8],[6,2]]
    print(solution.smallestStringWithSwaps(s, pairs))  # Output: "vbjjxgdfnru"
    