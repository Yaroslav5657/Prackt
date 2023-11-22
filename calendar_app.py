import tkinter as tk
from tkcalendar import Calendar

class CalendarApp:
    def init(self, root):
        self.root = root
        self.root.title("Календар")

        self.calendar = Calendar(self.root, selectmode="day", year=2023, month=11, day=19)
        self.calendar.pack(side="top", fill="both", expand=True)
        self.calendar.columnconfigure(0, weight=1)

if __name__ == "main":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()