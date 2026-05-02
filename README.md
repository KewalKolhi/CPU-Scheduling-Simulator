# CPU-Scheduling-Simulator
1.	Introduction:
Multi-programming consists of multiple programs running simultaneously on a computer. In such an operating system, many jobs run concurrently. In multi-programming systems, the OS must select a program to execute from those waiting in main memory. This selection is made through CPU scheduling algorithms.

2.	Project Description:
This project is a Python Desktop Application which is basically an emulation of three major scheduling algorithms, namely First Come First Serve, Shortest Job First, and Round Robin. The application has a graphical user interface through which data is entered.

3.	Objectives:
	To show the functionality of OS scheduling algorithms.
	To find and analyze critical parameters such as Waiting Time (WT), Turnaround Time (TAT), and Completion Time (CT).
	To create a user-friendly GUI using the tkinter module.

4.Key Terms and Formulas:
	To calculate the efficiency of the algorithms, the following         equations have been programmed.
	Arrival Time (AT): The time when the process arrives in the ready queue
	Burst Time (BT): The time needed by a process to execute in the CPU
	Completion Time (CT): The time when the process completes its execution.
	Turnaround Time (TAT): The time that the process stays in the system
TAT = CT – AT
	Waiting Time (WT): Total time the process waits in the ready queue.
WT = TAT -BT
4.	Algorithms Implemented:

A). First-Come, First-Served (FCFS)
	Principle: The first process to make the request for the processor will be served first.
	Type: Non-Preemptive
	Technique: Processes are prioritized by their arrival time and are processed accordingly.

      B). Shortest Job First (SJF)
	Principle: Linked to every process is its next CPU burst length.
	 The CPU goes to the process having the least burst time.
	Type: Non-preemptive (for this particular simulation).
	Algorithm: At any instant T, the algorithm checks all processes available and chooses the one with the least Burst Time.

     C). Round Robin (RR)
	Principle: Created for time-sharing systems. A small amount of CPU time is allocated to each process, called a Time Quantum.
	Type: Preemptive.
	Operation: Uses a Circular Queue structure (using collections. Deque) until all processes are completed.

5.Tools & Technologies Employed:

	Programming Language: Python 3.x
	GUI Framework: Tkinter (used for windows, buttons, and display components)
	Data Structures:
	Lists (used for managing processes)
	Deque (used for optimizing round-robin queue operations)
	Operating System: Kali Linux



5.	Software Architecture:
	The application is developed following the Object-Oriented Programming (OOP) methodology.
	__init__: Performs initializations such as window initialization and creating data structures.
	setup_ui: Creates the UI structure, the colors (black and neon theme), and the input fields.
	add_process: Validates user input and creates a list of processes.
	fcfs() / sjf() / round_robin(): Logical functions representing the algorithms.
	print_results: Helps in formatting the output table.

6.	User Manual:
	Process ID Enter: A unique ID for the process.
	Arrival Time Enter: When the process arrives in the queue (e.g., 0, 1, 2).
	Burst Time Enter: Execution time needed.
	Process Add: Click to add the process to the existing list.
	Time Quantum: Needed only for Round Robin scheduling.
	Simulate: Click on FCFS, SJF, or RR to see the results.
                   
