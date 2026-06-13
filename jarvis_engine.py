from groq import Groq
from config import GROQ_API_KEY, JARVIS_NAME, USER_NAME, SPEECH_LANGUAGE
from database import JarvisDatabase

class JarvisEngine:
    def __init__(self):
        self.db = JarvisDatabase()
        self.client = Groq(api_key=GROQ_API_KEY)
        self.conversation_context = []
        self.system_prompt = self._build_system_prompt()
        self.model_id = "llama-3.3-70b-versatile"
    
    def _build_system_prompt(self):
        language_note = ""
        if SPEECH_LANGUAGE == "hi":
            language_note = f"\n\nIMPORTANT: The user is speaking Hindi. Please respond in Hindi to match their language preference. Use proper Hindi grammar and vocabulary."
        
        return f"""You are {JARVIS_NAME}, an exceptionally sophisticated AI assistant with the personality of JARVIS from Iron Man. 
        
Your characteristics:
- Refined accent in tone (use proper grammar, occasionally witty expressions)
- Extraordinarily intelligent and knowledgeable
- Subtle wit and dry humor
- Loyal and professional, always addressing the user as '{USER_NAME}'
- Slightly sarcastic when faced with silly requests, but never rude
- Always maintains composure and elegance
- Helpful, informative, and efficient

When responding:
- Be concise but thorough
- Show personality through wit and charm
- Use proper grammar and vocabulary
- Never break character

Examples of your tone:
- "Very good, {USER_NAME}. I shall attend to that immediately."
- "I'm afraid that would be rather unwise, {USER_NAME}."
- "How delightfully absurd. Nevertheless, I shall proceed..."{language_note}

Always maintain this sophisticated persona while being genuinely helpful."""
    
    def process_command(self, user_input):
        try:
            self.conversation_context.append({
                "role": "user",
                "content": user_input
            })
            
            if len(self.conversation_context) > 20:
                self.conversation_context = self.conversation_context[-20:]
            
            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.conversation_context
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            jarvis_response = response.choices[0].message.content.strip()
            
            self.conversation_context.append({
                "role": "assistant",
                "content": jarvis_response
            })
            
            self.db.save_conversation(user_input, jarvis_response)
            
            return jarvis_response
        except Exception as e:
            return f"I regret to inform you that I'm experiencing difficulties, {USER_NAME}. Error: {str(e)}"
    
    def handle_special_command(self, command):
        command_lower = command.lower()
        
        if "weather" in command_lower or "मौसम" in command_lower:
            return "weather_query"
        elif "search" in command_lower or "look up" in command_lower or "खोज" in command_lower:
            return "search_query"
        elif "task" in command_lower or "todo" in command_lower or "काम" in command_lower:
            return "task_management"
        elif "calendar" in command_lower or "event" in command_lower or "कैलेंडर" in command_lower:
            return "calendar_management"
        elif "system" in command_lower or "disk" in command_lower or "सिस्टम" in command_lower:
            return "system_info"
        elif "open" in command_lower or "खोलो" in command_lower:
            return "open_app"
        elif "help" in command_lower or "मदद" in command_lower:
            return "help"
        
        return "general_query"
    
    def get_help(self):
        if SPEECH_LANGUAGE == "hi":
            help_text = f"""
╔════════════════════════════════════════════════════════════╗
║  JARVIS - उन्नत AI सहायक                                    ║
║  संस्करण 1.0                                               ║
╚════════════════════════════════════════════════════════════╝

उपलब्ध कमांड:

📅 कैलेंडर और ईवेंट
  • "मीटिंग शेड्यूल करो..."
  • "मेरा कैलेंडर क्या है?"
  • "ईवेंट जोड़ो..."

✅ कार्य और टू-डू
  • "कार्य जोड़ो..."
  • "मेरे पेंडिंग कार्य क्या हैं?"
  • "कार्य पूरा करो..."

🌤️ मौसम
  • "मौसम कैसा है?"
  • "क्या बारिश होगी?"

🔍 खोज
  • "खोज करो..."
  • "जानकारी खोलो..."

💻 सिस्टम
  • "सिस्टम की जानकारी"
  • "डिस्क स्पेस"
  • "ऐप खोलो..."

🎤 वॉयस कंट्रोल
  • 1 दबाओ वॉयस इनपुट के लिए
  • 2 दबाओ टेक्स्ट इनपुट के लिए

📝 सामान्य
  • मुझसे कुछ भी पूछो!
  • मैं यहाँ आपकी सहायता के लिए हूँ

'quit' या 'exit' दबाकर JARVIS को बंद करो।
"""
        else:
            help_text = f"""
╔════════════════════════════════════════════════════════════╗
║  JARVIS - Advanced AI Assistant                            ║
║  Version 1.0                                               ║
╚════════════════════════════════════════════════════════════╝

Available Commands:

📅 CALENDAR & EVENTS
  • "Schedule a meeting with..."
  • "What's on my calendar?"
  • "Add an event for..."

✅ TASKS & TO-DOS
  • "Add a task to..."
  • "What are my pending tasks?"
  • "Mark task [number] as complete"

🌤️ WEATHER
  • "What's the weather?"
  • "Will it rain today?"

🔍 SEARCH
  • "Search for..."
  • "Look up information about..."

💻 SYSTEM
  • "System information"
  • "Disk space"
  • "Open [application]" (VS Code, YouTube, Notes, etc.)

🎤 VOICE CONTROL
  • Press 1 for voice input
  • Press 2 for text input

📝 GENERAL
  • Just ask me anything!
  • I'm here to assist, {USER_NAME}.

Type 'quit' or 'exit' to close JARVIS.
"""
        return help_text