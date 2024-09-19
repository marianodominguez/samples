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
            
    def autocomplete(self,prefix):
        r=self.root
        sw=''
        cw=''
        stack=[]
        result=[]
        for next in r.children.values():
                stack.append(next)
        i=0
        
        while stack:
            c=stack.pop()
            #print(stack)
            if i>=len(prefix):
                sw+=c.value
                for next in c.children.values():
                    stack.append(next)
            if i<len(prefix) and c.value==prefix[i]:
                i+=1
                sw+=c.value
                for next in c.children.values():
                    stack.append(next)
            if c.endWord:
                result.append(sw)
                sw=''
        return result
                 
search_words=["Hello World", "Hello there", "some other word"]
trie=Tree()
for word in search_words:
    trie.add_word(word)
trie.printTree(trie.root)
print(trie.autocomplete('Hell'))
