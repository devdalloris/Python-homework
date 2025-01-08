import json

# Load
with open("tasks.json", "r") as file:
    data = json.load(file)
    print("Original data:")
    print(data)

# Modify
for i in data:
    i["ID"] = i.pop("id")
    i["Task Name"]=i.pop("task")
    i["Completed status"]=i.pop("completed")
    i["Priority"]=i.pop("priority")

# Save 
with open("tasks.json", "w") as file:
    json.dump(data, file, indent=4)
    print("\nModified data:")
    print(data)

#Calculate Task Completion Stats
def total_tasks():
    k=0
    for i in data:
        if(i["Task Name"]):
            k=k+1
    return f"Total number of tasks: {k}"
print(total_tasks())
def completed_tasks():
    c=0
    for i in data:
        if(i["Completed status"]==True):
            c=c+1
    return f"The number of completed tasks: {c}" 
print(completed_tasks())
def pending_tasks():
    c=0
    for i in data:
        if(i["Completed status"]==False):
            c=c+1
    return f"The number of pending tasks: {c}" 
print(pending_tasks())
def average_priority():
    c=0
    for i in data:
        c=c+i.get("Priority")
    return f"The number of average priority: {c/len(data)}" 
print(average_priority())