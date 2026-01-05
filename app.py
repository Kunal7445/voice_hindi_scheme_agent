from speech.stt import speech_to_text
from speech.tts import speak
from agent.memory import Memory
from agent.planner import plan
from agent.executor import execute
from agent.evaluator import evaluate
import sys

memory = Memory()

# Step 1: Speech to text
text, confidence = speech_to_text("demo_audio/input.wav")
memory.log(text)

# Step 2: Planning
action = plan(text, memory)

# Step 3: Ask for missing info
if action.startswith("ASK"):
    speak("Hello Kunal, How you doing today.")
    sys.exit(0)

# Step 4: Execute tools
result = execute(action, memory)
status = evaluate(result)

# Step 5: Respond and EXIT
if status == "SUCCESS":
    speak(f"आप इन योजनाओं के लिए पात्र हैं: {', '.join(result)}")
else:
    speak("माफ़ कीजिए, कोई उपयुक्त योजना नहीं मिली।")

sys.exit(0)
