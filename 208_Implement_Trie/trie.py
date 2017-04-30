class TrieNode(object):
    children = None
    isWord = False
    def __init__(self):
        self.children = {} # {c: node}
        self.isWord = False
    
class Trie(object):

    root = None
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return False
        return node.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if node is None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
