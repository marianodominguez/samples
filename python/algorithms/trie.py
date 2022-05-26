class Node:
    def __init__(self):
        self.value=''
        self.endWord=False
        self.children={}
              
class Tree:
    def __init__(self):
        self.root=Node()
        self.root.value=''
        
    def add_word(self,word):
        r=self.root
        for ch in word:
            n = Node()
            n.value=ch
            r.children[ch]=n
            r=n
        n.endWord=True
        
    def printTree(self,n):
        print(n.value, end=',')
        for ch in n.children:
            v=n.children[ch]
            self.printTree(v)
            
    def autocomplete(self,prefix):
        r=self.root
        sw=''
        for ch in prefix:
            if r.children[ch]: 
                r=r.children[ch]
                sw+=ch
        sw=sw[:-1]
        stack=[r]
        result=[]
        
        while stack:
            c=stack.pop()
            sw+=c.value
            if c.endWord: 
                result.append(sw)
            for next in c.children.values():
                stack.append(next)
        return result
                 
search_words=["Hello World", "Hello there", "some other word"]
trie=Tree()
for word in search_words:
    trie.add_word(word)

print(trie.autocomplete('Hell'))
