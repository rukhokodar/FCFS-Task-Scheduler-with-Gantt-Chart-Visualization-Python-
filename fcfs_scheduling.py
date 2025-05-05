import matplotlib.pyplot as plt  # Gantt chart library

# Get number of tasks
n = int(input("Enter number of tasks: "))

# Input each task
tasks = []
for i in range(n):
    tname = input(f"Enter Task Name for task {i+1}: ")
    arrival = int(input(f"Enter arrival time for task {i+1}: "))
    burst = int(input(f"Enter burst time for task {i+1}: "))
    tasks.append({
        "name": tname,
        "arrival_time": arrival,
        "burst_time": burst,
        "start_time": 0,
        "completion_time": 0,
        "turnaround_time": 0,
        "waiting_time": 0
    })

# Sort tasks by arrival time
tasks.sort(key=lambda x: x["arrival_time"])

# Initialize current time
current_time = 0

# Scheduling logic
for t in tasks:
    if current_time < t["arrival_time"]:
        current_time = t["arrival_time"]
    
    t["start_time"] = current_time
    t["completion_time"] = current_time + t["burst_time"]
    t["turnaround_time"] = t["completion_time"] - t["arrival_time"]
    t["waiting_time"] = t["start_time"] - t["arrival_time"]
    
    current_time = t["completion_time"]

# Sort back by task name
tasks.sort(key=lambda x: x["name"])

# Print the table
print("\n" + "-"*80)
print("Task | Arrival | Burst | Start | Completion | Turnaround | Waiting")
print("-"*80)

for t in tasks:
    print(f"{t['name']:>4} |"
          f"{t['arrival_time']:>8} |"
          f"{t['burst_time']:>5} |"
          f"{t['start_time']:>6} |"
          f"{t['completion_time']:>10} |"
          f"{t['turnaround_time']:>10} |"
          f"{t['waiting_time']:>7}")

print("-"*80)

# Calculate and display averages
avg_tat = sum(t["turnaround_time"] for t in tasks) / n
avg_wt = sum(t["waiting_time"] for t in tasks) / n

print("\nAverage Turnaround Time: {:.2f}".format(avg_tat))
print("Average Waiting Time: {:.2f}".format(avg_wt))

# Draw Gantt Chart
fig, ax = plt.subplots()

for i, t in enumerate(tasks):
    ax.broken_barh([(t["start_time"], t["burst_time"])], (10 * i, 9), facecolors='tab:blue')
    ax.text(t["start_time"] + t["burst_time"] / 2, 10 * i + 4.5, t["name"],
            ha='center', va='center', color='white', fontsize=9, fontweight='bold')
    ax.text(t["start_time"], 10 * i + 1, str(t["start_time"]),
            ha='left', va='bottom', fontsize=7, color='black')
    ax.text(t["completion_time"], 10 * i + 1, str(t["completion_time"]),
            ha='right', va='bottom', fontsize=7, color='black')

ax.set_ylim(0, 10 * len(tasks))
ax.set_xlim(0, max(t["completion_time"] for t in tasks) + 2)
ax.set_xlabel('Time')
ax.set_yticks([10 * i + 4.5 for i in range(len(tasks))])
ax.set_yticklabels([t["name"] for t in tasks])
ax.set_title('FCFS Task Scheduling Gantt Chart')
ax.grid(True)
plt.tight_layout()
plt.show()