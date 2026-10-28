# Task Tracker - Mini Project (Week 1, Day 2)

A menu-based Python Task Tracker application that manages daily tasks with persistent JSON storage.

## Features
- **Add Task**: Add new tasks with automatic "Pending" status.
- **View Tasks**: Display a numbered list of all tasks with their current status (`[Pending]` or `[Done]`).
- **Complete Task**: Mark specific tasks as completed.
- **Delete Task**: Remove tasks from the list.
- **JSON Persistence**: Automatically saves data to `tasks.json` and reloads it on program startup.
- **Error Handling**: Gracefully handles empty titles, invalid menu inputs, invalid task numbers, and missing JSON files.

## How to Run
1. Ensure Python is installed on your system.
2. Run the program using your terminal:
   ```bash
   python mini_task_tracker.py
