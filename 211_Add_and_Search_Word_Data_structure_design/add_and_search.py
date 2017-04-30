class TrieNode(object):
    children = None
    isWord = None
    def __init__(self):
        self.children = {} # {char : node}
        self.isWord = False
    

class WordDictionary(object):
    root = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            child = node.children.get(c)
            if child is None:
                child = TrieNode()
                node.children[c] = child
            node = child
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)
    
    def find(self, node, word):
        if word == '': return node.isWord
        if word[0] == '.':
            for child in node.children:
                if self.find( node.children[child], word[1:]):
                    return True
        else:
            child = node.children.get(word[0])
            if child is not None:
                return self.find( child, word[1:])
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
