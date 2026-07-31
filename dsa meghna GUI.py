root = tk.Tk()
root.title("Priority Queue GUI")
root.geometry("500x500")

tk.Label(root, text="Maximum Capacity").pack()
capacity_entry = tk.Entry(root)
capacity_entry.pack()

pq = None

def create_queue():
    global pq
    try:
        cap = int(capacity_entry.get())
        pq = PriorityQueue(cap)
        messagebox.showinfo("Success", "Priority Queue Created!")
    except:
        messagebox.showerror("Error", "Enter a valid capacity.")

tk.Button(root, text="Create Queue", command=create_queue).pack(pady=5)

tk.Label(root, text="Item").pack()
item_entry = tk.Entry(root)
item_entry.pack()

tk.Label(root, text="Priority").pack()
priority_entry = tk.Entry(root)
priority_entry.pack()

output = tk.Text(root, height=12, width=50)
output.pack(pady=10)

def show(msg):
    output.delete(1.0, tk.END)
    output.insert(tk.END, msg)

def enqueue():
    if pq is None:
        show("Create Queue First!")
        return
    try:
        item = item_entry.get()
        priority = int(priority_entry.get())
        show(pq.enqueue(item, priority))
    except:
        show("Invalid Priority!")

def dequeue():
    if pq:
        show(pq.dequeue())

def traverse():
    if pq:
        show(pq.traverse())

def empty():
    if pq:
        show("Queue is Empty" if pq.is_empty() else "Queue is Not Empty")

def full():
    if pq:
        show("Queue is Full" if pq.is_full() else "Queue is Not Full")

def ascending():
    if pq:
        show(pq.ascending())

def descending():
    if pq:
        show(pq.descending())

tk.Button(root, text="Enqueue", width=15, command=enqueue).pack()
tk.Button(root, text="Dequeue", width=15, command=dequeue).pack()
tk.Button(root, text="Traverse", width=15, command=traverse).pack()
tk.Button(root, text="Check Empty", width=15, command=empty).pack()
tk.Button(root, text="Check Full", width=15, command=full).pack()
tk.Button(root, text="Ascending Order", width=15, command=ascending).pack()
tk.Button(root, text="Descending Order", width=15, command=descending).pack()
tk.Button(root, text="Exit", width=15, command=root.destroy).pack(pady=10)

root.mainloop()
