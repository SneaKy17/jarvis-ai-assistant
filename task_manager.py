from database import JarvisDatabase
from datetime import datetime, timedelta

class TaskManager:
    def __init__(self):
        self.db = JarvisDatabase()
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        try:
            self.db.add_task(title, description, due_date, priority)
            return f"Task '{title}' has been added to your list."
        except Exception as e:
            return f"Error adding task: {str(e)}"
    
    def get_tasks(self):
        try:
            tasks = self.db.get_tasks("pending")
            if not tasks:
                return "You have no pending tasks, Sir. Enjoy your leisure time."
            
            task_list = "Your pending tasks:\n"
            for task in tasks:
                task_list += f"  • {task[1]}\n"
            return task_list
        except Exception as e:
            return f"Error retrieving tasks: {str(e)}"
    
    def complete_task(self, task_id):
        try:
            self.db.complete_task(task_id)
            return f"Task {task_id} has been marked as completed."
        except Exception as e:
            return f"Error completing task: {str(e)}"
    
    def add_event(self, title, start_time, description="", end_time=None, location=""):
        try:
            self.db.add_event(title, start_time, description, end_time, location)
            return f"Event '{title}' has been scheduled."
        except Exception as e:
            return f"Error adding event: {str(e)}"
    
    def get_events(self):
        try:
            events = self.db.get_events()
            if not events:
                return "You have no scheduled events."
            
            event_list = "Your upcoming events:\n"
            for event in events:
                event_list += f"  • {event[1]} at {event[3]}\n"
            return event_list
        except Exception as e:
            return f"Error retrieving events: {str(e)}"
    
    def add_reminder(self, title, reminder_time):
        try:
            self.db.add_reminder(title, reminder_time)
            return f"Reminder '{title}' has been set for {reminder_time}."
        except Exception as e:
            return f"Error adding reminder: {str(e)}"
    
    def get_reminders(self):
        try:
            reminders = self.db.get_reminders()
            if not reminders:
                return "You have no pending reminders."
            
            reminder_list = "Your reminders:\n"
            for reminder in reminders:
                reminder_list += f"  • {reminder[1]} at {reminder[2]}\n"
            return reminder_list
        except Exception as e:
            return f"Error retrieving reminders: {str(e)}"