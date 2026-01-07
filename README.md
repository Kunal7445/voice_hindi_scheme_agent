# Hindi Scheme Voice Assistant

Hindi Scheme Voice Assistant is a Python-based voice agent designed to help users interact with government schemes in Hindi. It uses speech recognition, planning, and execution modules to provide relevant information about eligibility and available schemes.

---

## 📌 Project Overview

This project demonstrates AI-based voice interaction using Python. Users can speak in Hindi, and the system transcribes the speech, plans actions based on the input, executes relevant tasks, evaluates results, and responds with information about government schemes. It is modular, extensible, and designed for practical assistance.

---

## ✨ Key Features

- Hindi speech-to-text conversion  
- Natural language planning and task execution  
- Eligibility checking for government schemes  
- Modular architecture with memory, planner, executor, and evaluator  
- Text-to-speech response for interactive communication  

---

## 🛠 Technology Stack

**Languages & Frameworks**  
- Python 3.x  

**Key Libraries**  
- `whisper` for speech recognition  
- `speech` module for TTS/STT  
- Custom agent modules: `memory`, `planner`, `executor`, `evaluator`  

**Project Structure**
- `agent/` – handles memory, planning, execution, and evaluation  
- `speech/` – text-to-speech and speech-to-text  
- `demo_audio/` – sample input files  
- `data/schemes.json` – database of schemes  

---

## 🧩 Application Design

The application uses a modular agent architecture:
1. **Memory:** logs and manages user interactions  
2. **Planner:** determines actions based on input  
3. **Executor:** executes tasks using the stored data  
4. **Evaluator:** evaluates results and determines response  
5. **STT/TTS:** handles Hindi speech input and output  

This design allows the system to be extended with new schemes, tools, or languages easily.

---

## 📊 Learning Outcomes

- Building AI-powered voice assistants in Python  
- Working with speech recognition and text-to-speech  
- Implementing modular agent-based architecture  
- Processing Hindi natural language inputs  
- Integration of planning, execution, and evaluation modules  

---

## 🔮 Future Enhancements

- Multi-language support (English + Hindi)  
- Integration with real-time government APIs for schemes  
- Context-aware memory and long-term user interaction  
- GUI or mobile interface for broader accessibility  

---

## 👨‍💻 Author

**Kunal Singh**  
Computer Science Graduate  

📫 Email: kunal.singh7445@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/kunal-singh-229130261/

