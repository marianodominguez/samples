from collections import defaultdict
class Node:
    def __init__(self):
        self.endWord=False
        self.children=defaultdict(Node)
        self.value=''
    def __str__(self):
        self.value
    def __repr__(self):
        if self:
            return self.value
        return ''
class Tree:
    def __init__(self):
        self.root=Node()

    def add_word(self,word):
        n=self.root
        for ch in word:
            n = n.children[ch]
            n.value=ch
        n.endWord=True

    def print_tree(self,n):
        print(n.value, end=',')
        if n.endWord:
            print('')
        for ch in n.children:
            v=n.children[ch]
            self.print_tree(v)

    def collect_words(self,c, word):
        result = []
        stack = [(c, word)]
        while stack:
            c, word = stack.pop()
            if c.endWord:
                result.append(word)
            for a,n in c.children.items():
                stack.append((n,word+a))
        return result

    def collect_words_rec(self,c, word, result):
        #get max prefix
        if c.endWord:
            result.append(word)
        for a,n in c.children.items():
            self.collect_words_rec(n,word+a, result)
        return result

    def autocomplete(self,key):
        result = []
        c=self.root
        for a in key:
            if a not in c.children:
                return []
            c = c.children[a]
        result = self.collect_words(c, key)
        return result


search_words=["Hello World", "Hello there", "some other word", "Hell yeah!", "Hel, this should not show"]
trie=Tree()
for word in search_words:
    trie.add_word(word)
trie.print_tree(trie.root)
print(trie.autocomplete('Hell'))
print(trie.autocomplete('some'))
print(trie.autocomplete('kwyjibo'))
print(trie.autocomplete('Hello'))