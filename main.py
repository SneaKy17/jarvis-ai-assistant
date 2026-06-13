from jarvis_engine import JarvisEngine
from input_handler import InputHandler
from task_manager import TaskManager
from weather_handler import WeatherHandler
from web_search_handler import WebSearchHandler
from system_handler import SystemHandler

def main():
    print("\n" + "="*60)
    print("🤖 JARVIS - Advanced AI Assistant")
    print("="*60)
    print("\n🌐 Select Language:")
    print("1. English 🇬🇧")
    print("2. Hindi 🇮🇳")
    
    lang_choice = input("Enter choice (1 or 2): ").strip()
    
    if lang_choice == "2":
        import config
        config.SPEECH_LANGUAGE = "hi"
        print("✓ Language set to Hindi")
    else:
        import config
        config.SPEECH_LANGUAGE = "en"
        print("✓ Language set to English")
    
    print("Type 'help' for commands or 'quit' to exit\n")
    
    jarvis = JarvisEngine()
    input_handler = InputHandler()
    # ... rest of code
    task_manager = TaskManager()
    weather_handler = WeatherHandler()
    web_search = WebSearchHandler()
    
    while True:
        try:
            # Get user input
            user_input = input_handler.listen_for_command()
            
            if not user_input:
                continue
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                input_handler.speak("Goodbye, Sir. It has been a pleasure serving you.")
                print("\n👋 JARVIS shutting down...")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                help_text = jarvis.get_help()
                print(help_text)
                input_handler.speak("Here are your available commands, Sir.")
                continue
            
            # Determine command type
            command_type = jarvis.handle_special_command(user_input)
            
            # Handle special commands
            if command_type == "weather_query":
                weather = weather_handler.get_weather()
                response = weather_handler.format_weather_response(weather)
            elif command_type == "search_query":
                search_term = user_input.replace("search", "").replace("look up", "").strip()
                result = web_search.search_duckduckgo(search_term)
                response = web_search.format_search_response(result)
            elif command_type == "system_info":
                response = SystemHandler.get_system_info()
            else:
                # General query - use JARVIS
                response = jarvis.process_command(user_input)
            
            # Speak the response
            input_handler.speak(response)
            
        except KeyboardInterrupt:
            input_handler.speak("Shutting down, Sir.")
            print("\n👋 JARVIS shutting down...")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            input_handler.speak(f"An error has occurred: {str(e)}")

if __name__ == "__main__":
    main()