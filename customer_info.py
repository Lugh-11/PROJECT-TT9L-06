from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import main

class CustomerInfo:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("LIST OF CUSTOMER")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")  # Dark mode background color

        # Colors
        header_bg = "#725700"
        content_bg = "#c9c1a7"
        old_money_bg = "#6A4D23"  # Old money style color
        button_bg = "#725700"
        button_fg = "#ffe9a1"

        # Create main frames
        top = Frame(self.root, bg=header_bg)
        top.pack(side="top", fill="x")

        left = Frame(self.root, bg=content_bg)
        left.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        right = Frame(self.root, bg=content_bg)
        right.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        bottom = Frame(self.root, bg=header_bg)
        bottom.pack(side="bottom", fill="x")

        # Header Label
        self.label = Label(top, font=('Times', 40, 'bold'), text="CUSTOMER INFORMATION", fg="#ffe9a1", bg=header_bg)
        self.label.pack(pady=20)

        # Name Entry
        self.name_label = Label(left, font=('Times', 20, 'bold'), text="Name", fg="#ffe9a1", bg=old_money_bg, width=15)
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_customer_entry = Text(left, height=20, width=40, font=('Times', 16), bg="#FFFFFF", fg="#000000")
        self.name_customer_entry.grid(row=1, column=0, padx=10, pady=10)

        # Room No Entry
        self.room_no_label = Label(right, font=('Times', 20, 'bold'), text="Room Number", fg="#ffe9a1", bg=old_money_bg, width=15)
        self.room_no_label.grid(row=0, column=0, padx=10, pady=10)

        self.room_no_customer_entry = Text(right, height=20, width=40, font=('Times', 16), bg="#FFFFFF", fg="#000000")
        self.room_no_customer_entry.grid(row=1, column=0, padx=10, pady=10)

        # Home Button
        self.home_button = Button(bottom, text="Back", font=('Times', 20, 'bold'), bg=button_bg, fg=button_fg, relief=RIDGE, height=2, width=15, command=self.go_back)
        self.home_button.pack(side="left", padx=(20, 10), pady=20)

        # Display Button
        self.display_button = Button(bottom, text="Display", font=('Times', 20, 'bold'), bg=button_bg, fg=button_fg, relief=RIDGE, height=2, width=15, command=self.display_info)
        self.display_button.pack(side="left", padx=(10, 20), pady=20)

        # Check if Name and Room No are filled
        self.name_customer_entry.bind('<KeyRelease>', self.check_fields)
        self.room_no_customer_entry.bind('<KeyRelease>', self.check_fields)

    def check_fields(self, event=None):
        name_text = self.name_customer_entry.get("1.0", 'end-1c')
        room_text = self.room_no_customer_entry.get("1.0", 'end-1c')
        if name_text.strip() and room_text.strip():
            self.display_button.config(state=NORMAL)
        else:
            self.display_button.config(state=DISABLED)

    def display_info(self):
        conn = sqlite3.connect('Hotel.db')
        try:
            with conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Hotel (Fullname TEXT, Address TEXT, mobile_number TEXT, number_days TEXT, room_number INTEGER)')
                conn.commit()

                cursor.execute("SELECT Fullname FROM Hotel")
                names = cursor.fetchall()
                self.name_customer_entry.delete(1.0, tk.END)
                for name in names:
                    self.name_customer_entry.insert(tk.INSERT, name[0] + '\n')

                cursor.execute("SELECT room_number FROM Hotel")
                rooms = cursor.fetchall()
                self.room_no_customer_entry.delete(1.0, tk.END)
                for room in rooms:
                    self.room_no_customer_entry.insert(tk.INSERT, str(room[0]) + '\n')

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def go_back(self):
        self.root.destroy()
        main.home_ui() 

def customer_info_ui():
    root = tk.Tk()
    application = CustomerInfo(root)
    root.mainloop()








