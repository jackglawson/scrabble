filename = 'lexicon.txt'
lexicon_file = open(filename, 'r')
lexicon = [line.rstrip() for line in lexicon_file.readlines()]


class TrieNode:
    def __init__(self, eow: bool = False):
        self.eow = eow  # end of word
        self.children = {}

    def add(self, char, final_char: bool = False):
        assert char not in self.children.keys()
        self.children[char] = TrieNode(final_char)

    def __repr__(self):
        return '{} {}'.format('eow' if self.eow else '', self.children, )


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.search_candidate = ''

    def add_word(self, word: str):
        if word in self:
            return

        word = list(word)
        node = self.root
        while word[0] in node.children.keys():
            node = node.children[word.pop(0)]
        while word:
            char = word.pop(0)
            node.add(char, True if not word else False)
            node = node.children[char]

    def add_words(self, words: list):
        for word in words:
            self.add_word(word)

    def find_words(self, letters: list):
        valid_words = set()
        search_candidate = []
        letters_remaining = letters

        def search(v):
            if v.eow and ''.join(search_candidate) not in valid_words:
                valid_words.add(''.join(search_candidate))
            for l in letters_remaining:
                if l in v.children:
                    search_candidate.append(l)
                    letters_remaining.remove(l)
                    search(v.children[l])
                    del search_candidate[-1]
                    letters_remaining.append(l)

        search(self.root)
        return valid_words

    def __contains__(self, word: str):
        word = list(word)
        node = self.root
        while word:
            char = word.pop(0)
            try:
                node = node.children[char]
            except KeyError:
                return False
        return True if node.eow else False

    def __repr__(self):
        return str(self.root)


trie = Trie()
trie.add_words(lexicon)

letters = ['A', 'B', 'C']
words = trie.find_words(letters)
print(words)

# I have changed something!