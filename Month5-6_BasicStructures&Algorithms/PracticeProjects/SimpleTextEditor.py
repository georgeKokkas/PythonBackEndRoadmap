# This project will help practice arrays, linked lists, stacks, queues, hash tables,
# trees, graphs, sorting, searching, recursion, dynamic programming, and greedy algorithms.

# Features:

    # 1) Insert Text: Add text to the editor.
    # 2) Delete Text: Delete text from the editor.
    # 3) Undo/Redo: Use stacks to implement undo and redo functionality.
    # 4) Search: Search for a word using linear and binary search.
    # 5) Sort: Sort the words in the text alphabetically.
    # 6) Word Frequency: Use a hash table to count the frequency of each word.
    # 7) Spell Check: Use a trie to implement a simple spell checker.
    # 8) Shortest Path: Use a graph to find the shortest path between two words in the text.
    # 9) Find Minimum/Maximum: Use binary trees to find the minimum and maximum words.
    # 10) Dynamic Programming: Implement a feature to find the longest common subsequence between two texts.


class TextEditor:
    def __init__(self):
        self.text = []  # Use a list to store text
        self.undo_stack = []  # Stack for undo
        self.redo_stack = []  # Stack for redo
        self.word_freq = {}  # Hash table for word frequency
        self.trie = Trie()  # Trie for spell check
        self.words_graph = Graph()  # Graph for shortest path

    def insert_text(self, new_text):
        self.undo_stack.append(self.text.copy())  # Save the current state for undo
        self.text.extend(new_text.split())  # Split the new text into words and add to the list
        self._update_word_freq(new_text)  # Update the word frequency
        self._update_trie(new_text)  # Update the trie

    def delete_text(self, word):
        if word in self.text:
            self.undo_stack.append(self.text.copy())  # Save the current state for undo
            self.text.remove(word)  # Remove the word from the list
            self.word_freq[word] -= 1  # Decrease the word frequency
            if self.word_freq[word] == 0:
                del self.word_freq[word]  # Remove the word from the hash table if frequency is zero

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text.copy())  # Save the current state for redo
            self.text = self.undo_stack.pop()  # Restore the previous state

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text.copy())  # Save the current state for undo
            self.text = self.redo_stack.pop()  # Restore the previous state

    def search_word(self, word):
        # Linear search
        if word in self.text:
            return True
        # Binary search (requires sorted text)
        sorted_text = sorted(self.text)
        return self._binary_search(sorted_text, word)

    def _binary_search(self, arr, x):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def sort_text(self):
        self.text.sort()  # Sort the words alphabetically

    def get_word_frequency(self, word):
        return self.word_freq.get(word, 0)  # Return the frequency of the word

    def _update_word_freq(self, text):
        for word in text.split():
            self.word_freq[word] = self.word_freq.get(word, 0) + 1  # Update the frequency in the hash table

    def _update_trie(self, text):
        for word in text.split():
            self.trie.insert(word)  # Insert the word into the trie

    def find_shortest_path(self, word1, word2):
        # Use Dijkstra's algorithm to find the shortest path between two words
        return self.words_graph.dijkstra(word1, word2)

    def find_min_word(self):
        # Use a binary search tree to find the minimum word
        bst = BinarySearchTree()
        for word in self.text:
            bst.insert(word)
        return bst.find_min()

    def find_max_word(self):
        # Use a binary search tree to find the maximum word
        bst = BinarySearchTree()
        for word in self.text:
            bst.insert(word)
        return bst.find_max()

    def longest_common_subsequence(self, text1, text2):
        # Use dynamic programming to find the longest common subsequence
        return self._longest_common_subsequence_dp(text1, text2)

    def _longest_common_subsequence_dp(self, X, Y):
        m = len(X)
        n = len(Y)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

# Helper classes and functions
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))

    def dijkstra(self, start, end):
        import heapq
        queue = [(0, start)]
        distances = {start: 0}
        while queue:
            (dist, current_vertex) = heapq.heappop(queue)
            if current_vertex == end:
                return distances[current_vertex]
            for neighbor, weight in self.graph[current_vertex]:
                distance = dist + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return float('inf')

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

# Test the TextEditor class
editor = TextEditor()
editor.insert_text("Hello world this is a simple text editor")
print("Text:", editor.text)
print("Search 'world':", editor.search_word("world"))
print("Word frequency of 'text':", editor.get_word_frequency("text"))
editor.delete_text("text")
print("Text after deleting 'text':", editor.text)
print("Undo operation")
editor.undo()
print("Text after undo:", editor.text)
print("Redo operation")
editor.redo()
print("Text after redo:", editor.text)
print("Sort text")
editor.sort_text()
print("Text after sorting:", editor.text)
print("Minimum word:", editor.find_min_word())
print("Maximum word:", editor.find_max_word())
print("Longest common subsequence:", editor.longest_common_subsequence("abcde", "ace"))
