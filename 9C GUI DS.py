import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def dfs_tree(self, start):
        visited = set()
        dfs_tree = defaultdict(list)

        def dfs(v):
            visited.add(v)

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_tree[v].append(neighbor)
                    dfs(neighbor)

        dfs(start)
        return dfs_tree

    def display(self):
        result = ""

        for vertex, edges in self.graph.items():
            result += f"{vertex}: {edges}\n"

        return result

    def visualize(self, dfs_tree=None):
        G = nx.Graph()

        for vertex in self.graph:
            G.add_node(vertex)

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                G.add_edge(vertex, neighbor)

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)

        pos = nx.spring_layout(G, seed=10)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            node_size=1200,
            font_size=15,
            font_weight="bold"
        )

        plt.title("Original Graph")

        if dfs_tree:

            T = nx.DiGraph()

            for vertex in dfs_tree:
                for neighbor in dfs_tree[vertex]:
                    T.add_edge(vertex, neighbor)

            if len(T.nodes) == 0:
                T.add_node(start_entry.get().strip())

            plt.subplot(1, 2, 2)

            pos_tree = nx.spring_layout(T, seed=10)

            nx.draw(
                T,
                pos_tree,
                with_labels=True,
                node_color="lightgreen",
                edge_color="blue",
                node_size=1200,
                font_size=15,
                font_weight="bold",
                arrows=True
            )

            plt.title("DFS Tree")

        plt.tight_layout()
        plt.show()

g = Graph()

def add_vertex():
    vertex = vertex_entry.get().strip()

    if vertex == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a vertex!"
        )
        return

    g.add_vertex(vertex)

    vertex_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)
    output.insert(
        tk.END,
        "Vertex added successfully!\n\n"
    )
    output.insert(
        tk.END,
        g.display()
    )


def add_edge():
    vertex1 = vertex1_entry.get().strip()
    vertex2 = vertex2_entry.get().strip()

    if vertex1 == "" or vertex2 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter both vertices!"
        )
        return

    g.add_edge(vertex1, vertex2)

    vertex1_entry.delete(0, tk.END)
    vertex2_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        "Edge added successfully!\n\n"
    )

    output.insert(
        tk.END,
        g.display()
    )


def show_graph():
    output.delete("1.0", tk.END)

    if not g.graph:
        output.insert(
            tk.END,
            "Graph is empty!"
        )
        return

    output.insert(
        tk.END,
        "GRAPH:\n"
    )

    output.insert(
        tk.END,
        "--------------------\n"
    )

    output.insert(
        tk.END,
        g.display()
    )


def perform_dfs():
    start = start_entry.get().strip()

    if start == "":
        messagebox.showwarning(
            "Warning",
            "Please enter starting vertex!"
        )
        return

    if start not in g.graph:
        messagebox.showerror(
            "Error",
            "Starting vertex does not exist!"
        )
        return

    dfs_tree = g.dfs_tree(start)

    output.delete("1.0", tk.END)

    output.insert(
        tk.END,
        f"Depth-First Tree starting from {start}:\n"
    )

    output.insert(
        tk.END,
        "-----------------------------------\n"
    )

    for vertex, children in dfs_tree.items():
        output.insert(
            tk.END,
            f"{vertex} -> {children}\n"
        )

    g.visualize(dfs_tree)


def clear_all():
    g.graph.clear()

    vertex_entry.delete(0, tk.END)
    vertex1_entry.delete(0, tk.END)
    vertex2_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)

    output.delete("1.0", tk.END)

root = tk.Tk()

root.title("DFS Graph - Depth First Search")
root.geometry("700x650")

root.resizable(False, False)

title = tk.Label(
    root,
    text="DEPTH FIRST SEARCH (DFS)",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Graph and Depth-First Tree",
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

vertex_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


vertex_entry = tk.Entry(
    vertex_frame,
    width=30,
    font=("Arial", 12)
)

vertex_entry.pack(
    side="left",
    padx=10
)


add_vertex_button = tk.Button(
    vertex_frame,
    text="Add Vertex",
    command=add_vertex,
    width=15
)

add_vertex_button.pack(
    side="left"
)

edge_frame = tk.LabelFrame(
    root,
    text="Add Edge",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

edge_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


tk.Label(
    edge_frame,
    text="Vertex 1:"
).pack(side="left")


vertex1_entry = tk.Entry(
    edge_frame,
    width=10
)

vertex1_entry.pack(
    side="left",
    padx=5
)


tk.Label(
    edge_frame,
    text="Vertex 2:"
).pack(side="left")


vertex2_entry = tk.Entry(
    edge_frame,
    width=10
)

vertex2_entry.pack(
    side="left",
    padx=5
)


add_edge_button = tk.Button(
    edge_frame,
    text="Add Edge",
    command=add_edge,
    width=15
)

add_edge_button.pack(
    side="left",
    padx=10
)

dfs_frame = tk.LabelFrame(
    root,
    text="Depth First Search",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

dfs_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


tk.Label(
    dfs_frame,
    text="Starting Vertex:"
).pack(side="left")


start_entry = tk.Entry(
    dfs_frame,
    width=10
)

start_entry.pack(
    side="left",
    padx=10
)


dfs_button = tk.Button(
    dfs_frame,
    text="Perform DFS",
    command=perform_dfs,
    width=15
)

dfs_button.pack(
    side="left"
)

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


show_button = tk.Button(
    button_frame,
    text="Show Graph",
    command=show_graph,
    width=15
)

show_button.pack(
    side="left",
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    width=15
)

clear_button.pack(
    side="left",
    padx=5
)


output_frame = tk.LabelFrame(
    root,
    text="Output",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

output_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


output = tk.Text(
    output_frame,
    height=12,
    width=70,
    font=("Courier New", 12)
)

output.pack(
    fill="both",
    expand=True
)

root.mainloop()
