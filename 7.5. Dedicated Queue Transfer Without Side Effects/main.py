def process_queue(tasks, preserve_original=False):
    cp_task = tasks[:] if preserve_original else tasks
    completed = []
    while cp_task:
        completed.append(cp_task.pop(0))
    return completed
    
def sol():
    in_flag = int(input())
    flag = in_flag == 1
    task = input().split()
    Completed = process_queue(task, flag)
    print(f"Original: {' '.join(task) if task else "EMPTY"}")
    print(f"Completed: {' '.join(Completed) if Completed else "EMPTY"}")

def main():
    t = int(input())
    for _ in range(t):
        sol()
        

if __name__ == "__main__":
    main()
