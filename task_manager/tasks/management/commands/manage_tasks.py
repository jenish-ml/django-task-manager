from django.core.management.base import BaseCommand
from tasks.models import Task

class Command(BaseCommand):
    help = 'Manage tasks from the command line'

    def handle(self, *args, **kwargs):
        while True:
            print("Task Manager")
            print("1. Add Task")
            print("2. Edit Task")
            print("3. Delete Task")
            print("4. View All Tasks")
            print("5. Filter Tasks by Priority")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter title: ")
                description = input("Enter description: ")
                priority = input("Enter priority (High/Medium/Low): ")
                status = input("Enter status (Pending/In Progress/Completed): ")
                Task.objects.create(title=title, description=description, priority=priority, status=status)
                print("Task added successfully.")
            elif choice == '2':
                task_id = int(input("Enter task ID: "))
                task = Task.objects.get(id=task_id)
                task.title = input(f"Enter title ({task.title}): ") or task.title
                task.description = input(f"Enter description ({task.description}): ") or task.description
                task.priority = input(f"Enter priority (High/Medium/Low) ({task.priority}): ") or task.priority
                task.status = input(f"Enter status (Pending/In Progress/Completed) ({task.status}): ") or task.status
                task.save()
                print("Task updated successfully.")
            elif choice == '3':
                task_id = int(input("Enter task ID: "))
                Task.objects.filter(id=task_id).delete()
                print("Task deleted successfully.")
            elif choice == '4':
                tasks = Task.objects.all()
                for task in tasks:
                    print(f"{task.id}: {task.title} - {task.description} - {task.priority} - {task.status}")
            elif choice == '5':
                priority = input("Enter priority (High/Medium/Low): ")
                tasks = Task.objects.filter(priority=priority)
                for task in tasks:
                    print(f"{task.id}: {task.title} - {task.description} - {task.priority} - {task.status}")
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
