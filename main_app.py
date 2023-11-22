import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from calendar_app import CalendarApp
from timer_app import TimerApp

class MainApp:
    def init(self, root):
        self.root = root
        self.root.title("Головний Додаток")

        # Бокова панель
        self.side_panel = ttk.Frame(root, width=150, height=300, relief="solid", borderwidth=1)
        self.side_panel.pack(side="left", fill="y")

        # Кнопка календаря
        self.calendar_button = ttk.Button(self.side_panel, text="Календар")
        self.calendar_button.pack(pady=10)
        self.calendar_button.config(command=self.show_calendar)

        # Кнопка таймера
        self.timer_button = ttk.Button(self.side_panel, text="Таймер")
        self.timer_button.pack(pady=10)
        self.timer_button.config(command=self.show_timer)

        # Додатки
        self.calendar_app = None
        self.timer_app = None

    def show_calendar(self):
        if self.timer_app:
            self.timer_app.destroy()
            self.timer_app = None

        if not self.calendar_app:
            self.calendar_app = tk.Toplevel(self.root)
            self.calendar_app.protocol("WM_DELETE_WINDOW", self.close_calendar_app)
            app = CalendarApp(self.calendar_app)

    def show_timer(self):
        if self.calendar_app:
            self.calendar_app.destroy()
            self.calendar_app = None

        if not self.timer_app:
            self.timer_app = tk.Toplevel(self.root)
            self.timer_app.protocol("WM_DELETE_WINDOW", self.close_timer_app)
            app = TimerApp(self.timer_app)

    def close_calendar_app(self):
        self.calendar_app.destroy()
        self.calendar_app = None

    def close_timer_app(self):
        self.timer_app.destroy()
        self.timer_app = None

if __name__ == "main":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()