import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random
import string


def get_response(user):

    user = user.lower().strip()

    if user in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today? 😊"

    elif user == "time":
        return datetime.now().strftime("Current Time: %I:%M:%S %p")

    elif user == "date":
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif user == "ai":
        return "AI stands for Artificial Intelligence."

    elif user == "machine learning":
        return "Machine Learning is a subset of AI that learns from data."

    elif user == "python":
        return "Python is one of the most popular languages for AI and ML."

    elif user == "motivate me":
        return "Keep learning. Every expert was once a beginner. 🚀"

    elif user == "study tips":
        return """
📚 Study Tips

• Practice coding daily
• Revise regularly
• Build projects
• Learn by doing
• Stay consistent
"""

    elif user == "joke":

        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did Python go to school? To improve its class! 😆",
            "Why do Java developers wear glasses? Because they don't C# 😄"
        ]

        return random.choice(jokes)

    elif user == "fact":

        facts = [
            "AI stands for Artificial Intelligence.",
            "Python was created by Guido van Rossum.",
            "Machine Learning is a subset of AI.",
            "The first computer bug was an actual insect."
        ]

        return random.choice(facts)

    elif user == "quote":

        quotes = [
            "Dream big and dare to fail.",
            "Success is the sum of small efforts repeated every day.",
            "Believe you can and you're halfway there."
        ]

        return random.choice(quotes)

    elif user.startswith("calculate"):

        try:
            expression = user.replace("calculate", "").strip()
            result = eval(expression)
            return f"Result = {result}"

        except:
            return "Invalid expression."

    elif user == "password":

        chars = string.ascii_letters + string.digits + "!@#$%&*"

        password = ''.join(
            random.choice(chars)
            for _ in range(10)
        )

        return f"Generated Password:\n{password}"

    elif "happy" in user:
        return "That's wonderful! Keep smiling 😊"

    elif "sad" in user:
        return "Tough times don't last, but tough people do 💪"

    elif "stressed" in user:
        return "Take a deep breath and relax 🌿"

    elif user == "help":

        return """
📌 AVAILABLE COMMANDS

👋 Greetings
hello
hi
hey

🕒 Utilities
time
date
calculate 10+5
password

📚 Knowledge
ai
machine learning
python

😊 Fun
joke
fact
quote

💪 Productivity
motivate me
study tips

❤️ Mood
i am happy
i am sad
i am stressed

❌ Exit
bye
quit
exit
"""

    elif user in ["bye", "quit", "exit"]:

        root.after(1000, root.destroy)

        return "Goodbye! Have a wonderful day! 👋"

    else:
        return "I don't understand that command.\nType 'help'."



def send_message():

    user_message = entry.get()

    if user_message == "":
        return

    timestamp = datetime.now().strftime("%H:%M")

    chat_area.insert(
        tk.END,
        f"\n👤 You ({timestamp})\n{user_message}\n",
        "user"
    )

    response = get_response(user_message)

    chat_area.insert(
        tk.END,
        f"\n🤖 Bot ({timestamp})\n{response}\n",
        "bot"
    )

    chat_area.see(tk.END)

    entry.delete(0, tk.END)



def clear_chat():
    chat_area.delete("1.0", tk.END)



root = tk.Tk()

root.title("🤖 Smart AI Chatbot")

root.geometry("950x700")

root.configure(bg="#121212")

root.resizable(False, False)


header = tk.Label(
    root,
    text="🤖 SMART AI CHATBOT",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E1E",
    fg="#00E5FF",
    pady=15
)

header.pack(fill="x")


chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 11),
    bd=0
)

chat_area.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

chat_area.tag_config(
    "user",
    foreground="#00E676",
    font=("Segoe UI", 11, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="#40C4FF",
    font=("Segoe UI", 11)
)

chat_area.insert(
    tk.END,
    """
🤖 Welcome to Smart AI Chatbot

Type 'help' to see available commands.

Enjoy chatting!
---------------------------------------------------
""",
    "bot"
)


input_frame = tk.Frame(
    root,
    bg="#121212"
)

input_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

entry = tk.Entry(
    input_frame,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    font=("Segoe UI", 13),
    relief="flat"
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10),
    ipady=12
)



send_btn = tk.Button(
    input_frame,
    text="Send ➤",
    font=("Segoe UI", 11, "bold"),
    bg="#00C853",
    fg="white",
    relief="flat",
    cursor="hand2",
    command=send_message
)

send_btn.pack(
    side="right",
    ipadx=15,
    ipady=8
)


clear_btn = tk.Button(
    root,
    text="🗑 Clear Chat",
    font=("Segoe UI", 11, "bold"),
    bg="#D50000",
    fg="white",
    relief="flat",
    cursor="hand2",
    command=clear_chat
)

clear_btn.pack(
    pady=10,
    ipadx=15,
    ipady=6
)



footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    bg="#1E1E1E",
    fg="gray",
    font=("Segoe UI", 9)
)

footer.pack(fill="x")


entry.bind("<Return>", lambda event: send_message())


root.mainloop()
