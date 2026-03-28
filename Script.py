import tkinter as tk
import pyautogui
import time
import threading

class AutoTypeApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoType GUI")

        self.label = tk.Label(master, text="Text to Type:")
        self.label.pack()

        self.text_input = tk.Entry(master, width=50)
        self.text_input.pack()

        self.delay_label = tk.Label(master, text="Delay before typing (seconds):")
        self.delay_label.pack()

        self.delay_input = tk.Entry(master, width=5)
        self.delay_input.pack()
        self.delay_input.insert(0, "3")  # default delay of 3 seconds

        self.speed_label = tk.Label(master, text="Typing Speed (words per minute):")
        self.speed_label.pack()

        self.speed_slider = tk.Scale(master, from_=10, to=300, orient=tk.HORIZONTAL)
        self.speed_slider.set(50)  # default speed
        self.speed_slider.pack()

        self.activate_button = tk.Button(master, text="Activate", command=self.start_typing)
        self.activate_button.pack()

        self.status_var = tk.StringVar()
        self.status_var.set("Status: Ready")
        self.status_label = tk.Label(master, textvariable=self.status_var)
        self.status_label.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_text)
        self.clear_button.pack()

    def start_typing(self):
        self.status_var.set("Status: Typing...")
        self.master.update()  # refresh the GUI
        delay = int(self.delay_input.get())
        time.sleep(delay)  # wait for the specified delay
        text = self.text_input.get()
        speed = self.speed_slider.get()
        # calculate typing interval
        interval = 60 / speed  # seconds per word

        for word in text.split():
            pyautogui.typewrite(word + ' ', interval)

        self.status_var.set("Status: Complete")

    def clear_text(self):
        self.text_input.delete(0, tk.END)
        self.status_var.set("Status: Ready")

root = tk.Tk()
app = AutoTypeApp(root)
root.mainloop()