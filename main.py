from flask import Flask
import tkinter as tk
import threading

# Flask Web App
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "<h1>Welcome to My App</h1><p>This is a simple Flask app.</p>"

def run_flask():
    web_app.run(debug=True, use_reloader=False)

# Tkinter GUI App
def run_tkinter():
    def greet():
        label.config(text=f"Hello, {entry.get()}!")

    root = tk.Tk()
    root.title("Simple App")

    label = tk.Label(root, text="Enter your name:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Greet", command=greet)
    button.pack()

    root.mainloop()

# Command-line App
def run_command_line():
    print("Welcome to My Command-line App")
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

run_tkinter()
from kivy.app import App
from kivy.uix.label import Label
from telethon import TelegramClient

class MyApp(App):
    def build(self):
        return Label(text="Hello, this is a Python app converted to APK!")

if __name__ == "__main__":
    MyApp().run()
