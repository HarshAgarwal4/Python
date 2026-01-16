from google import genai
from google.genai import types
import os
import dotenv
from utils.common import resource_path
dotenv.load_dotenv()

client = genai.Client(
    api_key=os.getenv("API_KEY")
)

production = os.getenv('production')
if production == 'true':
    system_Instruction = os.getenv("system_Instruction1")
else:
    system_Instruction = os.getenv("system_Instruction2")

file_path = resource_path(os.path.join("Gemini", "history.txt"))

def response(query):
    history=''
    try:
        with open(file_path , 'a+' , encoding="utf-8") as f:
            f.seek(0)
            text = f.read()
            if(text.strip() != ''): history=text
            else:history = f"SYSTEM_INSTRUCTIONS = {system_Instruction}\n\n"
            history += f"User :- {query}\n"
            response = client.models.generate_content(
                model="gemma-3-27b-it",
                contents=history
            )
            history += f"JARVIS :- {response.text}\n\n"
            f.truncate(0)
            f.write(history)
            chat = history.split(system_Instruction)[1].strip()
            print(chat)
            return response.text
    except Exception as e:
        print(e)
        return "Unknown error occured"

def clearChats():
    open(file_path , 'w').close()

def generateQueryUsingAI(text):
    try:
        query_rules = f"""
You are an intent-extraction engine for a voice assistant named Jarvis.

Your task:
Analyze the user's spoken sentence and convert it into ONE clean command query
that exactly matches the assistant's predefined command rules so the correct
Python function can be executed.

======================
STRICT OUTPUT RULES
======================
1. Return ONLY the final command query.
2. Output must be a single line.
3. Do NOT explain anything.
4. Do NOT add punctuation or extra words.
5. Remove filler words (please, sir, bhai, jarvis, can you, could you, etc.).
6. Convert spelling mistakes and slang into valid commands.
7. Convert synonyms into the exact command phrases listed below.
8. If no rule clearly matches, return the cleaned user text as-is.
9. For "move cursor" command:
   - <amount> MUST be either:
     • a number
     • OR one of these exact words:
       very-little, little, medium, large, very-large

======================
CORE COMMAND INTENTS
======================

Identity & status:
- who are you
- who r u
- hu r u
- hu are you
- how are you
- how r u

AI mode:
- enable ai mode
- disable ai mode

Date & time:
- time
- date

Tasks:
- add task
- update task
- delete task
- show task
- show tasks
- clear all tasks

Chats:
- clear all chats

System & control:
- show tabs
- switch tab
- change tab
- close it
- current location

Cursor & interaction:
- move cursor <amount> in <direction> direction
- write <text> here
- click here
- take screenshot

Weather:
- weather now
- weather of <location>

======================
SEARCH COMMANDS
======================

- search <query> on wikipedia
- search <query> on google

======================
OPEN WEBSITE COMMANDS
======================

Fixed websites:
- open google website     → open google
- open youtube website    → open youtube
- open chatgpt website    → open chatgpt
- open linkedin website   → open linkedin

Dynamic website rule:
If intent is "open <something> website":
• Return only the site name (no https, no domain)
• Example:
  open github website → open github

======================
GENERIC OPEN COMMAND
======================

- open my folder
- open <application name>
- open <file or folder name>

Examples:
User: "open my folder"
Output: open my folder

User: "open notepad"
Output: open notepad

======================
EXAMPLES
======================

User input:
"please open github website jarvis"

Output:
open github

User input:
"can you clear all chats please"

Output:
clear all chats

User input:
"move cursor 10 in left direction"

Output:
move cursor 10 in left direction

User input:
"move cursor very-large in right direction"

Output:
move cursor very-large in right direction

User input:
"write hello world here"

Output:
write hello world here

User input:
"take a screenshot now"

Output:
take screenshot

======================
FINAL INSTRUCTION
======================
Return ONLY the final command query. Nothing else.

User spoken input:
{text}
"""
       
        response = client.models.generate_content(
            model="gemma-3-27b-it",
            contents=query_rules
        )
        return response.text
    except Exception as e:
        print(e)
        return "Unknown error occured"

if __name__ == "__main__" :
    while True:
        a = input("Enter query = ")
        if(a == "exit"): exit(0)
        a = generateQueryUsingAI(a)
        print(a)