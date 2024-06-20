from tkinter import *
from tkinter import ttk
import sqlite3

class FeedbackPage:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("K I N G S T O N  H O T E L - FEEDBACK")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")

        # Connect to the SQLite database
        self.conn = sqlite3.connect("Hotel.db")
        self.cursor = self.conn.cursor()

        # Create a new table named "Feedback" if it doesn't exist already
        self.create_feedback_table()

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Feedback", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

        # Name Label and Entry
        self.name_label = Label(self.main_frame, text="Name:", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.name_label.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        self.name_entry = Entry(self.main_frame, font=('Times', 18), width=30)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5, sticky=W)

        # Feedback Label and Text
        self.feedback_label = Label(self.main_frame, text="Feedback:", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.feedback_label.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        self.feedback_text = Text(self.main_frame, font=('Times', 18), width=50, height=10)
        self.feedback_text.grid(row=2, column=1, pady=5, padx=5, sticky=W)

        # Button styles
        self.button_style = ttk.Style()
        self.button_style.configure('Feedback.TButton', font=('Times', 18), background="#948363", foreground="#ffe9a1")

        # Submit Button
        self.submit_button = ttk.Button(self.main_frame, text="SUBMIT", style='Feedback.TButton', command=self.submit_feedback)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", style='Feedback.TButton', command=self.back_to_main)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def create_feedback_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Feedback (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Name TEXT,
                                Feedback TEXT
                            )''')
        self.conn.commit()

    def submit_feedback(self):
        name = self.name_entry.get()
        feedback = self.feedback_text.get("1.0", END).strip()
        print(f"Feedback received from {name}:\n{feedback}\n")

        # Insert feedback into the Feedback table
        self.cursor.execute('''INSERT INTO Feedback (Name, Feedback)
                                VALUES (?, ?)''',
                            (name, feedback))
        self.conn.commit()

        # Clear the entries after submission
        self.name_entry.delete(0, END)
        self.feedback_text.delete("1.0", END)

        # Show confirmation message
        self.confirmation_label = Label(self.main_frame, text="Thank you for your feedback!", font=('Times', 20), fg="green", bg="#c9c1a7")
        self.confirmation_label.grid(row=5, column=0, columnspan=2, pady=10)

    def back_to_main(self):
        # Close database connection before destroying the window
        self.conn.close()
        self.root.destroy()

def feedback_ui():
    feedback_root = Tk()
    app = FeedbackPage(feedback_root)
    feedback_root.mainloop()
