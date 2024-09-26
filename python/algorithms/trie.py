class Node:
    def __init__(self):
        self.value=''
        self.endWord=False
        self.children={}
    def __str__(self):
        self.value
    def __repr__(self):
        if self:
            return self.value
        return ''
class Tree:
    def __init__(self):
        self.root=Node()
        self.root.value=''

    def add_word(self,word):
        r=self.root
        for ch in word:
            if ch not in r.children:
                n = Node()
                n.value=ch
                r.children[ch]=n
                r=n
            else:
                r=r.children[ch]
        r.endWord=True

    def printTree(self,n):
        print(n.value, end=',')
        if n.endWord:
            print('')
        for ch in n.children:
            v=n.children[ch]
            self.printTree(v)

    def getPrefix(self,c, word, result):
        #get max prefix
        if c.endWord:
            result.append(word)
        for a,n in c.children.items():
            self.getPrefix(n,word+a, result)
        return result

    def autocomplete(self,key):
        result = []
        c=self.root
        for a in key:
            if a not in c.children:
                return []
            c = c.children[a]
        if not c.children:
            return []
        self.getPrefix(c, key, result)
        return result


search_words=["Hello World", "Hello there", "some other word", "Hell yeah!", "Hel, this should not show"]
trie=Tree()
for word in search_words:
    trie.add_word(word)
#trie.printTree(trie.root)
print(trie.autocomplete('Hell'))
print(trie.autocomplete('some'))
print(trie.autocomplete('kwyjibo'))
print(trie.autocomplete('Hello'))