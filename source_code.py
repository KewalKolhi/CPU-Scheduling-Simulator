import tkinter as tk

root = tk.Tk()
root.title("OS CPU Scheduling Simulator")
root.geometry("900x750")
root.configure(bg="black")

processes = []

# ---------------- TITLE ----------------
tk.Label(
    root,
    text="CPU Scheduling Simulator (FCFS, SJF & Round Robin)",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="black"
).pack(pady=10)

# ---------------- INPUT FRAME ----------------
input_frame = tk.Frame(root, bg="black")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Process ID", fg="white", bg="black").grid(row=0, column=0)
pid = tk.Entry(input_frame)
pid.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Arrival Time", fg="white", bg="black").grid(row=1, column=0)
at = tk.Entry(input_frame)
at.grid(row=1, column=1, padx=5)

tk.Label(input_frame, text="Burst Time", fg="white", bg="black").grid(row=2, column=0)
bt = tk.Entry(input_frame)
bt.grid(row=2, column=1, padx=5)

# Added Field for Round Robin
tk.Label(input_frame, text="Time Quantum", fg="white", bg="black").grid(row=3, column=0)
tq = tk.Entry(input_frame)
tq.grid(row=3, column=1, padx=5)

# ---------------- LISTBOX ----------------
listbox = tk.Listbox(root, width=70, bg="#1a1a1a", fg="white")
listbox.pack(pady=10)

# ---------------- OUTPUT ----------------
output = tk.Text(root, height=15, width=100, bg="#111111", fg="white")
output.pack(pady=10)

# ---------------- FUNCTIONS ----------------
def add_process():
    if not pid.get() or not at.get() or not bt.get():
        return

    processes.append([pid.get(), int(at.get()), int(bt.get())])
    listbox.insert(tk.END, f"{pid.get()} | AT={at.get()} | BT={bt.get()}")

    pid.delete(0, tk.END)
    at.delete(0, tk.END)
    bt.delete(0, tk.END)

def clear_all():
    processes.clear()
    listbox.delete(0, tk.END)
    output.delete("1.0", tk.END)

def fcfs():
    output.delete("1.0", tk.END)
    data = sorted(processes, key=lambda x: x[1])
    time = 0
    total_wt = 0
    total_tat = 0
    output.insert(tk.END, "FCFS Results\n\n")

    for name, atime, burst in data:
        if time < atime: time = atime
        start = time
        finish = start + burst
        wt = start - atime
        tat = finish - atime
        time = finish
        total_wt += wt
        total_tat += tat
        output.insert(tk.END, f"{name}: CT={finish}, WT={wt}, TAT={tat}\n")

    n = len(data)
    if n: output.insert(tk.END, f"\nAvg WT: {total_wt/n:.2f}\nAvg TAT: {total_tat/n:.2f}")

def sjf():
    output.delete("1.0", tk.END)
    data = [p[:] for p in processes] # Copy list
    time = 0
    total_wt, total_tat = 0, 0
    output.insert(tk.END, "SJF Results\n\n")

    while data:
        available = [p for p in data if p[1] <= time]
        if not available:
            time += 1
            continue
        shortest = min(available, key=lambda x: x[2])
        data.remove(shortest)
        name, atime, burst = shortest
        start = time
        finish = start + burst
        wt = start - atime
        tat = finish - atime
        time = finish
        total_wt += wt
        total_tat += tat
        output.insert(tk.END, f"{name}: CT={finish}, WT={wt}, TAT={tat}\n")

    n = len(processes)
    if n: output.insert(tk.END, f"\nAvg WT: {total_wt/n:.2f}\nAvg TAT: {total_tat/n:.2f}")

def round_robin():
    output.delete("1.0", tk.END)
    if not tq.get(): 
        output.insert(tk.END, "Please enter Time Quantum!")
        return
        
    quantum = int(tq.get())
    data = [[p[0], p[1], p[2], p[2]] for p in processes] # [name, at, bt, rem_bt]
    time = 0
    n = len(data)
    queue = []
    completed = 0
    output.insert(tk.END, "Round Robin Results\n\n")

    while completed < n:
        # Add arrived processes to queue
        for p in data:
            if p[1] <= time and p not in queue and p[3] > 0:
                queue.append(p)
        
        if not queue:
            time += 1
            continue
            
        curr = queue.pop(0)
        
        # Execute
        if curr[3] > quantum:
            time += quantum
            curr[3] -= quantum
            # Check arrivals during execution
            for p in data:
                if p[1] <= time and p not in queue and p[3] > 0 and p != curr:
                    queue.append(p)
            queue.append(curr)
        else:
            time += curr[3]
            curr[3] = 0
            completed += 1
            # Calculate metrics
            tat = time - curr[1]
            wt = tat - curr[2]
            output.insert(tk.END, f"{curr[0]}: CT={time}, WT={wt}, TAT={tat}\n")
    
    # Optional: Calculate averages here if needed

# ---------------- BUTTON FRAME ----------------
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="Add Process", command=add_process, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Run FCFS", command=fcfs, bg="orange").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Run SJF", command=sjf, bg="purple", fg="white").grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Run RR", command=round_robin, bg="blue", fg="white").grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_all, bg="red", fg="white").grid(row=0, column=4, padx=5)

root.mainloop()
