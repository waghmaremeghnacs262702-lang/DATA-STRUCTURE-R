import tkinter as tk
from tkinter import scrolledtext
import heapq
from collections import Counter


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Output text
output_text = ""


def build_huffman_tree(frequencies):
    global output_text

    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        output_text += f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})\n"

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook=None):
    global output_text

    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            if prefix == "":
                prefix = "0"

            codebook[node.char] = prefix
            output_text += f"Assigning code to character {node.char}: {prefix}\n"

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook


def huffman_encoding(data):
    global output_text

    frequencies = Counter(data)

    output_text += "Character Frequencies:\n"
    output_text += str(dict(frequencies)) + "\n\n"

    root = build_huffman_tree(frequencies)

    codebook = generate_codes(root)

    encoded_data = "".join(codebook[ch] for ch in data)

    output_text += "\nEncoded Data:\n"
    output_text += encoded_data + "\n\n"

    return encoded_data, codebook


def huffman_decoding(encoded_data, codebook):
    global output_text

    reverse_codebook = {v: k for k, v in codebook.items()}

    decoded_data = ""
    current_code = ""

    output_text += "Decoding:\n"

    for bit in encoded_data:
        current_code += bit

        if current_code in reverse_codebook:
            output_text += f"{current_code} -> {reverse_codebook[current_code]}\n"
            decoded_data += reverse_codebook[current_code]
            current_code = ""

    return decoded_data


def run_huffman():
    global output_text

    output_text = ""

    data = entry.get()

    if data == "":
        return

    encoded_data, codebook = huffman_encoding(data)

    output_text += "\nCodebook:\n"
    output_text += str(codebook) + "\n\n"

    decoded_data = huffman_decoding(encoded_data, codebook)

    output_text += "\nOriginal Data: " + data + "\n"
    output_text += "Decoded Data: " + decoded_data + "\n"

    if data == decoded_data:
        output_text += "\nSuccess: Original and decoded data match."
    else:
        output_text += "\nError: Original and decoded data do not match."

    result.delete("1.0", tk.END)
    result.insert(tk.END, output_text)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Huffman Coding")
root.geometry("700x500")

label = tk.Label(root, text="Enter Text:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Encode & Decode", command=run_huffman)
button.pack(pady=10)

result = scrolledtext.ScrolledText(root, width=80, height=22)
result.pack(pady=10)

root.mainloop()
