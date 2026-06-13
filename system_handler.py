import os
import platform
import subprocess
from pathlib import Path

class SystemHandler:
    @staticmethod
    def get_system_info():
        try:
            system = platform.system()
            release = platform.release()
            machine = platform.machine()
            processor = platform.processor()
            
            return (f"System: {system} {release}\n"
                    f"Machine: {machine}\n"
                    f"Processor: {processor}")
        except Exception as e:
            return f"Error retrieving system info: {str(e)}"
    
    @staticmethod
    def open_application(app_name):
        try:
            system = platform.system()
            
            app_paths = {
                "vscode": {
                    "Windows": "code",
                    "Darwin": "open -a 'Visual Studio Code'",
                    "Linux": "code"
                },
                "notepad": {
                    "Windows": "notepad",
                    "Darwin": "open -a TextEdit",
                    "Linux": "gedit"
                },
                "chrome": {
                    "Windows": "start chrome",
                    "Darwin": "open -a 'Google Chrome'",
                    "Linux": "google-chrome"
                },
                "firefox": {
                    "Windows": "start firefox",
                    "Darwin": "open -a Firefox",
                    "Linux": "firefox"
                },
                "youtube": {
                    "Windows": "start https://youtube.com",
                    "Darwin": "open https://youtube.com",
                    "Linux": "xdg-open https://youtube.com"
                }
            }
            
            if app_name.lower() in app_paths:
                command = app_paths[app_name.lower()][system]
                os.system(command)
                return f"Opening {app_name}..."
            else:
                return f"I'm unable to open {app_name}. Perhaps you could specify the full path?"
        except Exception as e:
            return f"Error opening application: {str(e)}"
    
    @staticmethod
    def get_disk_space():
        try:
            import shutil
            total, used, free = shutil.disk_usage("/")
            
            return (f"Total: {total // (1024**3)} GB\n"
                    f"Used: {used // (1024**3)} GB\n"
                    f"Free: {free // (1024**3)} GB")
        except Exception as e:
            return f"Error retrieving disk space: {str(e)}"