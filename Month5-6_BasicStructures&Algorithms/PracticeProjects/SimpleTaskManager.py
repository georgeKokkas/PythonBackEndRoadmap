# Features

    # 1) Add Task: Add a task with a priority and a due date.
    # 2) Delete Task: Delete a task by name.
    # 3) View Tasks: View all tasks sorted by priority or due date.
    # 4) Search Task: Search for a task by name.
    # 5) Undo/Redo: Use stacks to implement undo and redo functionality.
    # 6) Shortest Path: Use a graph to find the shortest path between two tasks based on dependencies.
    # 7) Find Minimum/Maximum Priority Task: Use binary trees to find the minimum and maximum priority tasks.
    # 8) Task Frequency: Use a hash table to count the frequency of tasks by priority.

class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store tasks
        self.undo_stack = []  # Stack for undo
        self.redo_stack = []  # Stack for redo
        self.priority_freq = {}  # Hash table for priority frequency
        self.tasks_graph = Graph()  # Graph for task dependencies

    def add_task(self, name, priority, due_date):
        self.undo_stack.append(self.tasks.copy())  # Save the current state for undo
        task = {"name": name, "priority": priority, "due_date": due_date}
        self.tasks.append(task)  # Add task to the list
        self._update_priority_freq(priority)  # Update the priority frequency

    def delete_task(self, name):
        task_to_delete = next((task for task in self.tasks if task["name"] == name), None)
        if task_to_delete:
            self.undo_stack.append(self.tasks.copy())  # Save the current state for undo
            self.tasks.remove(task_to_delete)  # Remove the task from the list
            self.priority_freq[task_to_delete["priority"]] -= 1  # Decrease the priority frequency
            if self.priority_freq[task_to_delete["priority"]] == 0:
                del self.priority_freq[task_to_delete["priority"]]  # Remove the priority if frequency is zero

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.tasks.copy())  # Save the current state for redo
            self.tasks = self.undo_stack.pop()  # Restore the previous state

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.tasks.copy())  # Save the current state for undo
            self.tasks = self.redo_stack.pop()  # Restore the previous state

    def view_tasks(self, sort_by="priority"):
        if sort_by == "priority":
            return sorted(self.tasks, key=lambda x: x["priority"])  # Sort tasks by priority
        elif sort_by == "due_date":
            return sorted(self.tasks, key=lambda x: x["due_date"])  # Sort tasks by due date

    def search_task(self, name):
        return next((task for task in self.tasks if task["name"] == name), None)  # Search for the task by name

    def _update_priority_freq(self, priority):
        self.priority_freq[priority] = self.priority_freq.get(priority, 0) + 1  # Update the priority frequency

    def find_shortest_path(self, task1, task2):
        # Use Dijkstra's algorithm to find the shortest path between two tasks
        return self.tasks_graph.dijkstra(task1, task2)

    def find_min_priority_task(self):
        # Use a binary search tree to find the minimum priority task
        bst = BinarySearchTree()
        for task in self.tasks:
            bst.insert(task["priority"])
        min_priority = bst.find_min()
        return next((task for task in self.tasks if task["priority"] == min_priority), None)

    def find_max_priority_task(self):
        # Use a binary search tree to find the maximum priority task
        bst = BinarySearchTree()
        for task in self.tasks:
            bst.insert(task["priority"])
        max_priority = bst.find_max()
        return next((task for task in self.tasks if task["priority"] == max_priority), None)

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

# Test the TaskManager class
manager = TaskManager()
manager.add_task("Task 1", 1, "2024-07-01")
manager.add_task("Task 2", 2, "2024-07-02")
manager.add_task("Task 3", 3, "2024-07-03")
print("Tasks:", manager.view_tasks())
print("Search 'Task 2':", manager.search_task("Task 2"))
manager.delete_task("Task 2")
print("Tasks after deleting 'Task 2':", manager.view_tasks())
print("Undo operation")
manager.undo()
print("Tasks after undo:", manager.view_tasks())
print("Redo operation")
manager.redo()
print("Tasks after redo:", manager.view_tasks())
print("Sort tasks by due date")
print("Tasks sorted by due date:", manager.view_tasks(sort_by="due_date"))
print("Minimum priority task:", manager.find_min_priority_task())
print("Maximum priority task:", manager.find_max_priority_task())
