import sqlite3
import json
from datetime import datetime
from config import DB_PATH

class JarvisDatabase:
    def __init__(self):
        self.db_path = DB_PATH
        self.init_database()
    
    def init_database(self):
        """Initialize database with required tables"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Tasks table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'pending',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    due_date TIMESTAMP,
                    priority TEXT DEFAULT 'medium'
                )
            ''')
            
            # Calendar events table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    start_time TIMESTAMP NOT NULL,
                    end_time TIMESTAMP,
                    location TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Reminders table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reminders (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    reminder_time TIMESTAMP NOT NULL,
                    is_completed BOOLEAN DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Conversation history
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY,
                    user_input TEXT NOT NULL,
                    jarvis_response TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            print("✓ Database initialized successfully")
        except Exception as e:
            print(f"Database init error: {e}")
    
    def add_task(self, title, description="", due_date=None, priority="medium"):
        """Add a new task"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (title, description, due_date, priority)
                VALUES (?, ?, ?, ?)
            ''', (title, description, due_date, priority))
            conn.commit()
            task_id = cursor.lastrowid
            conn.close()
            return task_id
        except Exception as e:
            print(f"Error adding task: {e}")
            return None
    
    def get_tasks(self, status="pending"):
        """Get tasks by status"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks WHERE status = ?', (status,))
            tasks = cursor.fetchall()
            conn.close()
            return tasks
        except Exception as e:
            print(f"Error getting tasks: {e}")
            return []
    
    def complete_task(self, task_id):
        """Mark task as completed"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', ('completed', task_id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error completing task: {e}")
    
    def add_event(self, title, start_time, description="", end_time=None, location=""):
        """Add calendar event"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO events (title, description, start_time, end_time, location)
                VALUES (?, ?, ?, ?, ?)
            ''', (title, description, start_time, end_time, location))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error adding event: {e}")
    
    def get_events(self):
        """Get all upcoming events"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM events ORDER BY start_time')
            events = cursor.fetchall()
            conn.close()
            return events
        except Exception as e:
            print(f"Error getting events: {e}")
            return []
    
    def add_reminder(self, title, reminder_time):
        """Add reminder"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO reminders (title, reminder_time)
                VALUES (?, ?)
            ''', (title, reminder_time))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error adding reminder: {e}")
    
    def get_reminders(self):
        """Get pending reminders"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM reminders WHERE is_completed = 0 ORDER BY reminder_time')
            reminders = cursor.fetchall()
            conn.close()
            return reminders
        except Exception as e:
            print(f"Error getting reminders: {e}")
            return []
    
    def save_conversation(self, user_input, jarvis_response):
        """Save conversation history"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO conversations (user_input, jarvis_response)
                VALUES (?, ?)
            ''', (user_input, jarvis_response))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error saving conversation: {e}")
    
    def get_conversation_history(self, limit=10):
        """Get recent conversation history"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                SELECT user_input, jarvis_response FROM conversations
                ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            history = cursor.fetchall()
            conn.close()
            return history
        except Exception as e:
            print(f"Error getting conversation history: {e}")
            return []