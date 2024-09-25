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

    def getPrefix(self,c, word):
        #get max prefix
        if c.endWord:
            print(word)
        for a,n in c.children.items():
            self.getPrefix(n,word+a)

    def autocomplete(self,key):
        r=self.root
        c=r
        sw=''
        cw=''
        stack=[]
        result=[]

        for a in key:
            if a not in c.children:
                return []
            c = c.children[a]
        if not c.children:
            return [] 
        self.getPrefix(c, key)
        #TODO: Add to list
        return ["Done"]


search_words=["Hello World", "Hello there", "some other word", "Hell yeah!", "Hel, this should not show"]
trie=Tree()
for word in search_words:
    trie.add_word(word)
#trie.printTree(trie.root)
print(trie.autocomplete('Hell'))
