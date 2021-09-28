#Non-recursive definition, right?
#Developer 1
class Node:
    def __init__(self, key, children = []):
        self.key = key
        self.chidlren = children
class Tree:
    def __init__(self):
        self.root = Node("United Kingdom")
        self.root.children = [Node("Wales"), Node("North Ireland"), \
            Node("Scotland"), Node("England")]
    def height_of(u):
        if u is None:
            return 0
        ans = 0
        for v in u.children:
            ans = max(ans, height_of(v) + 1)
        return ans
#haha
#hihi
