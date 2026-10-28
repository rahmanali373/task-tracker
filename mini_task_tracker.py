
# Student: Rahman Ali
# Roll no.: TRN-2026-000293
# Assignment: Build a Task Tracker (Mini Project - Week 1, Day 2)

import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with an empty task list.")
            return []
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Ask for a task title and store it as Pending."""
    title = input("Task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    
    new_task = {
        "title": title,
        "done": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added.")

def view_tasks(tasks):
    """Show a numbered task list with Pending or Done status."""
    if not tasks:
        print("No tasks found.")
        return
    
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(tasks):
    """Select a task number and mark its done field True."""
    if not tasks:
        print("No tasks available to complete.")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Task number: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task completed.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_task(tasks):
    """Select a task number and remove that task."""
    if not tasks:
        print("No tasks available to delete.")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Error: Invalid menu choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()