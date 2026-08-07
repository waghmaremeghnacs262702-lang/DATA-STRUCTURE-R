import tkinter as tk
from tkinter import ttk
import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y

    def get_height(self, root):
        return root.height if root else 0

    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right) if root else 0

    def pre_order(self, root):
        result = []
        self._pre_order(root, result)
        return result

    def _pre_order(self, root, result):
        if root:
            result.append(root.key)
            self._pre_order(root.left, result)
            self._pre_order(root.right, result)


def min_heap_example(data):
    heapq.heapify(data)
    return data


def max_heap_example(data):
    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    return [-x for x in max_heap]


class TaskManager:
    def __init__(self):
        self.pq = []

    def add_task(self, priority, description):
        heapq.heappush(self.pq, (priority, description))

    def run_tasks(self):
        tasks = []
        while self.pq:
            priority, task = heapq.heappop(self.pq)
            tasks.append(f"Priority {priority} -> Task: {task}")
        return tasks


def run_program():
    output.delete("1.0", tk.END)

    avl = AVLTree()
    root = None
    avl_inputs = [20, 4, 15, 70, 50, 100, 80]

    output.insert(tk.END, "=== AVL Tree Insertion and Balancing ===\n")
    for value in avl_inputs:
        root = avl.insert(root, value)

    output.insert(tk.END, "Pre-Order Traversal:\n")
    output.insert(tk.END, " ".join(map(str, avl.pre_order(root))) + "\n\n")

    data = [9, 5, 6, 2, 3]
    output.insert(tk.END, "=== Heap Examples ===\n")
    output.insert(tk.END, f"Min-Heap: {min_heap_example(data.copy())}\n")
    output.insert(tk.END, f"Max-Heap: {max_heap_example(data.copy())}\n\n")

    output.insert(tk.END, "=== Task Manager ===\n")
    manager = TaskManager()
    manager.add_task(2, "Low priority: Backup database")
    manager.add_task(1, "High priority: Handle emergency patient")
    manager.add_task(3, "Medium priority: Run diagnostics")

    for task in manager.run_tasks():
        output.insert(tk.END, task + "\n")


root = tk.Tk()
root.title("AVL Tree, Heap and Priority Queue")
root.geometry("700x500")

title = ttk.Label(root, text="AVL Tree, Heap and Priority Queue", font=("Arial", 16, "bold"))
title.pack(pady=10)

run_btn = ttk.Button(root, text="Run Program", command=run_program)
run_btn.pack(pady=5)

output = tk.Text(root, width=80, height=25)
output.pack(padx=10, pady=10)

root.mainloop()
