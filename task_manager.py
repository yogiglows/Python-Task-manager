import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
    except:
        print("Invalid choice.")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
    except:
        print("Invalid choice.")


def main():
    tasks = load_tasks()

    while True:
        print("""
1. Show tasks
2. Add task
3. Complete task
4. Delete task
5. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
