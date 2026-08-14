import tkinter as tk
from tkinter import messagebox
from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs_tree(self, start):
        visited = set()
        bfs_tree = defaultdict(list)

        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_tree[current].append(neighbor)
                    queue.append(neighbor)

        return bfs_tree

    def display(self):
        result = ""
        for vertex, edges in self.graph.items():
            result += f"{vertex}: {edges}\n"
        return result

g = Graph()

def add_vertex():
    vertex = vertex_entry.get().strip()

    if vertex == "":
        messagebox.showwarning("Warning", "Enter a vertex!")
        return

    g.add_vertex(vertex)
    vertex_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Vertex added successfully!\n")
    output.insert(tk.END, g.display())


def add_edge():
    v1 = vertex1_entry.get().strip()
    v2 = vertex2_entry.get().strip()

    if v1 == "" or v2 == "":
        messagebox.showwarning("Warning", "Enter both vertices!")
        return

    if v1 not in g.graph or v2 not in g.graph:
        messagebox.showerror(
            "Error",
            "Both vertices must be added before adding an edge!"
        )
        return

    g.add_edge(v1, v2)

    vertex1_entry.delete(0, tk.END)
    vertex2_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)
    output.insert(tk.END, "Edge added successfully!\n\n")
    output.insert(tk.END, g.display())


def show_graph():
    output.delete("1.0", tk.END)

    if not g.graph:
        output.insert(tk.END, "Graph is empty!")
        return

    output.insert(tk.END, "GRAPH:\n")
    output.insert(tk.END, "--------------------\n")
    output.insert(tk.END, g.display())


def perform_bfs():
    start = start_entry.get().strip()

    if start == "":
        messagebox.showwarning("Warning", "Enter starting vertex!")
        return

    if start not in g.graph:
        messagebox.showerror("Error", "Starting vertex does not exist!")
        return

    tree = g.bfs_tree(start)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        f"Breadth-First Tree starting from {start}:\n"
    )
    output.insert(tk.END, "------------------------------\n")

    for vertex, children in tree.items():
        output.insert(tk.END, f"{vertex} -> {children}\n")


def clear_all():
    g.graph.clear()

    vertex_entry.delete(0, tk.END)
    vertex1_entry.delete(0, tk.END)
    vertex2_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)

root = tk.Tk()
root.title("BFS Graph - Breadth First Tree")
root.geometry("700x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="BREADTH FIRST SEARCH (BFS)",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Graph and Breadth-First Tree",
    font=("Arial", 12)
)
subtitle.pack()


vertex_frame = tk.LabelFrame(
    root,
    text="Add Vertex",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)
vertex_frame.pack(fill="x", padx=30, pady=10)

vertex_entry = tk.Entry(vertex_frame, width=30, font=("Arial", 12))
vertex_entry.pack(side="left", padx=10)

add_vertex_button = tk.Button(
    vertex_frame,
    text="Add Vertex",
    command=add_vertex,
    width=15
)
add_vertex_button.pack(side="left")

edge_frame = tk.LabelFrame(
    root,
    text="Add Edge",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)
edge_frame.pack(fill="x", padx=30, pady=10)

tk.Label(edge_frame, text="Vertex 1:").pack(side="left")

vertex1_entry = tk.Entry(edge_frame, width=10)
vertex1_entry.pack(side="left", padx=5)

tk.Label(edge_frame, text="Vertex 2:").pack(side="left")

vertex2_entry = tk.Entry(edge_frame, width=10)
vertex2_entry.pack(side="left", padx=5)

add_edge_button = tk.Button(
    edge_frame,
    text="Add Edge",
    command=add_edge,
    width=15
)
add_edge_button.pack(side="left", padx=10)

bfs_frame = tk.LabelFrame(
    root,
    text="Breadth First Search",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)
bfs_frame.pack(fill="x", padx=30, pady=10)

tk.Label(
    bfs_frame,
    text="Starting Vertex:"
).pack(side="left")

start_entry = tk.Entry(
    bfs_frame,
    width=10
)
start_entry.pack(side="left", padx=10)

bfs_button = tk.Button(
    bfs_frame,
    text="Perform BFS",
    command=perform_bfs,
    width=15
)
bfs_button.pack(side="left")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

show_button = tk.Button(
    button_frame,
    text="Show Graph",
    command=show_graph,
    width=15
)
show_button.pack(side="left", padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    width=15
)
clear_button.pack(side="left", padx=5)


output_frame = tk.LabelFrame(
    root,
    text="Output",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)
output_frame.pack(fill="both", expand=True, padx=30, pady=10)

output = tk.Text(
    output_frame,
    height=12,
    width=70,
    font=("Courier New", 12)
)
output.pack(fill="both", expand=True)

root.mainloop()
