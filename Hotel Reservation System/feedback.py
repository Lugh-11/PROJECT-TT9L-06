import sqlite3
from tkinter import *
from tkinter import messagebox

def feedback_ui():
    feedback_window = Toplevel()
    feedback_window.title("Leave Feedback")
    feedback_window.geometry("400x300")
    feedback_window.configure(bg="#c9c1a7")

    Label(feedback_window, text="Leave your feedback", font=('Times', 20), bg="#c9c1a7", fg="#725700").pack(pady=20)
    feedback_text = Text(feedback_window, font=('Times', 15), height=10, width=50)
    feedback_text.pack(pady=20)

    def submit_feedback():
        feedback_content = feedback_text.get("1.0", END).strip()
        if feedback_content:
           conn = sqlite3.connect('Hotel.db')  # Connect to the database
           try:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)')  # Create table if it doesn't exist
                cursor.execute('INSERT INTO Feedback (content) VALUES (?)', (feedback_content,))  # Insert feedback into the table
                conn.commit()
                messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")
                feedback_window.destroy()
           finally:
                conn.close()  # Ensure the connection is closed
        else:
            messagebox.showwarning("Empty Feedback", "Please enter some feedback before submitting.")

    Button(feedback_window, text="Submit Feedback", font=('Times', 15), bg="#948363", fg="#ffe9a1", command=submit_feedback).pack(pady=10)