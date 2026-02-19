import tkinter as tk
from tkinter import ttk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(False, False)

        # State
        self.expression = ""
        self.memory = 0.0
        self.dark_mode = True

        # Colors
        self.set_theme()

        self.create_style()
        self.create_widgets()

    def set_theme(self):
        if self.dark_mode:
            self.bg = "#1e1e1e"
            self.btn = "#2d2d2d"
            self.text = "#ffffff"
            self.accent = "#4fc3f7"
            self.display_bg = "#121212"
        else:
            self.bg = "#f4f4f4"
            self.btn = "#ffffff"
            self.text = "#000000"
            self.accent = "#1976d2"
            self.display_bg = "#ffffff"
        self.configure(bg=self.bg)

    def create_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "TEntry",
            fieldbackground=self.display_bg,
            foreground=self.text,
            insertcolor=self.text,
            font=("Segoe UI", 10),
            borderwidth=0
        )

        style.configure(
            "Calc.TButton",
            background=self.btn,
            foreground=self.text,
            font=("Segoe UI", 15, "bold"),
            padding=8,
            borderwidth=0
        )

        style.map(
            "Calc.TButton",
            background=[("active", self.accent)],
            foreground=[("active", "#000000")]
        )

    def create_widgets(self):
        self.display = ttk.Entry(self, justify="right")
        self.display.pack(fill="x", padx=10, pady=10, ipady=10)

        top = tk.Frame(self, bg=self.bg)
        top.pack(fill="x")

        ttk.Button(top, text="☀ / 🌙", style="Calc.TButton", command=self.toggle_theme).pack(side="right", padx=10)

        frame = tk.Frame(self, bg=self.bg)
        frame.pack(expand=True, fill="both")

        buttons = [
            ("sin",1,0),("cos",1,1),("tan",1,2),("log",1,3),
            ("√",2,0),("x²",2,1),("M+",2,2),("M-",2,3),
            ("7",3,0),("8",3,1),("9",3,2),("/",3,3),
            ("4",4,0),("5",4,1),("6",4,2),("*",4,3),
            ("1",5,0),("2",5,1),("3",5,2),("-",5,3),
            ("0",6,0),(".",6,1),("=",6,2),("+",6,3),
            ("C",7,0),("MR",7,1)
        ]

        for text,row,col in buttons:
            ttk.Button(
                frame,
                text=text,
                style="Calc.TButton",
                command=lambda t=text: self.on_click(t) # type: ignore
            ).grid(row=row, column=col, sticky="nsew", padx=6, pady=6)

        for i in range(8): frame.rowconfigure(i, weight=1)
        for j in range(4): frame.columnconfigure(j, weight=1)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
        self.create_style()
        for widget in self.winfo_children(): widget.destroy()
        self.create_widgets()

    def on_click(self, char): # type: ignore
        try:
            if char == "=":
                result = eval(self.expression) # type: ignore
                self.display_value(result) # type: ignore
            elif char == "C":
                self.expression = ""
                self.display.delete(0, tk.END)
            elif char == "sin": self.apply_func(math.sin) # type: ignore
            elif char == "cos": self.apply_func(math.cos) # type: ignore
            elif char == "tan": self.apply_func(math.tan) # type: ignore
            elif char == "log": self.apply_func(math.log10) # type: ignore
            elif char == "√": self.apply_func(math.sqrt) # type: ignore
            elif char == "x²": self.apply_func(lambda x: x*x) # type: ignore
            elif char == "M+": self.memory += float(self.display.get())
            elif char == "M-": self.memory -= float(self.display.get())
            elif char == "MR": self.display_value(self.memory) # type: ignore
            else:
                self.expression += char # type: ignore
                self.display.insert(tk.END, char) # type: ignore
        except:
            self.display_value("Error") # type: ignore

    def apply_func(self, func): # type: ignore
        value = float(self.display.get())
        result = func(value) # type: ignore
        self.display_value(result) # type: ignore

    def display_value(self, value): # type: ignore
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(value)) # type: ignore
        self.expression = str(value) # type: ignore
if __name__ == "__main__":
    Calculator().mainloop()