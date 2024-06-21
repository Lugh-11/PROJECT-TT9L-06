import tkinter as tk
from tkinter import messagebox
import os
import sqlite3
import bcrypt

class LoginApp:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.title("Login")

        bg = "#c9c1a7"

        # Set background color of root window
        self.root.configure(bg=bg)

        # Create frames
        self.login_frame = tk.Frame(self.root, bg=bg)
        self.signup_frame = tk.Frame(self.root, bg=bg)

        # Initialize widgets
        self.initialize_login_widgets()
        self.initialize_signup_widgets()

        # Show login frame by default
        self.show_login_frame()

        # Test Database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users(
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )'''
        )

    def initialize_login_widgets(self):
        self.login_label = tk.Label(self.login_frame, text="Login", font=('Times', 24, 'bold'), bg="#948363",
                                    fg="#ffe9a1", relief="ridge", bd=3)
        self.username_label = tk.Label(self.login_frame, text="Username:", font=('Times', 16), bg="#948363",
                                       fg="#ffe9a1")
        self.username_entry = tk.Entry(self.login_frame, font=('Times', 12))
        self.password_label = tk.Label(self.login_frame, text="Password:", font=('Times', 16), bg="#948363",
                                       fg="#ffe9a1")
        self.password_entry = tk.Entry(self.login_frame, show="*", font=('Times', 16))
        self.user_type_var = tk.StringVar(value="User")
        self.user_radio = tk.Radiobutton(self.login_frame, text="User", variable=self.user_type_var, value="User",
                                         bg="#c9c1a7", fg="#725700", font=('Times', 12))
        self.admin_radio = tk.Radiobutton(self.login_frame, text="Admin", variable=self.user_type_var, value="Admin",
                                          bg="#c9c1a7", fg="#725700", font=('Times', 12))
        self.login_button = tk.Button(self.login_frame, text="Login", font=('Times', 16, 'bold'), bg="#948363",
                                      fg="#ffe9a1", command=self.login)
        self.signup_button = tk.Button(self.login_frame, text="Sign Up", font=('Times', 16, 'bold'), bg="#948363",
                                       fg="#ffe9a1", command=self.show_signup_frame)

        # Layout widgets
        self.login_label.pack(pady=20)
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.user_radio.pack()
        self.admin_radio.pack()
        self.login_button.pack(pady=20)
        self.signup_button.pack(pady=10)

    def initialize_signup_widgets(self):
        self.signup_label = tk.Label(self.signup_frame, text="Sign Up", font=('Times', 24, 'bold'), bg="#948363",
                                     fg="#ffe9a1", relief="ridge", bd=3)
        self.new_username_label = tk.Label(self.signup_frame, text="New Username:", font=('Times', 16), bg="#948363",
                                           fg="#ffe9a1")
        self.new_username_entry = tk.Entry(self.signup_frame, font=('Times', 12))
        self.new_password_label = tk.Label(self.signup_frame, text="New Password:", font=('Times', 16), bg="#948363",
                                           fg="#ffe9a1")
        self.new_password_entry = tk.Entry(self.signup_frame, show="*", font=('Times', 16))
        self.confirm_password_label = tk.Label(self.signup_frame, text="Confirm Password:", font=('Times', 16),
                                               bg="#948363", fg="#ffe9a1")
        self.confirm_password_entry = tk.Entry(self.signup_frame, show="*", font=('Times', 16))
        self.signup_submit_button = tk.Button(self.signup_frame, text="Submit", font=('Times', 16, 'bold'), bg="#948363",
                                              fg="#ffe9a1", command=self.signup)
        self.back_to_login_button = tk.Button(self.signup_frame, text="Back to Login", font=('Times', 16, 'bold'),
                                              bg="#948363", fg="#ffe9a1", command=self.show_login_frame)

        # Layout widgets
        self.signup_label.pack(pady=20)
        self.new_username_label.pack()
        self.new_username_entry.pack()
        self.new_password_label.pack()
        self.new_password_entry.pack()
        self.confirm_password_label.pack()
        self.confirm_password_entry.pack()
        self.signup_submit_button.pack(pady=20)
        self.back_to_login_button.pack(pady=10)

    def show_login_frame(self):
        self.signup_frame.pack_forget()
        self.login_frame.pack()

    def show_signup_frame(self):
        self.login_frame.pack_forget()
        self.signup_frame.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type_var.get()

        if user_type == "Admin":
            if username == "admin" and password == "123":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
                self.navigate_to_admin()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password for Admin")
        else:
            if username != '' and password != '':
                self.cursor.execute('SELECT password FROM users WHERE username=?', (username,))
                result = self.cursor.fetchone()
                if result:
                    stored_password = result[0]
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        messagebox.showinfo('Success', 'Logged in successfully.')
                        self.navigate_to_main()
                    else:
                        messagebox.showerror("Login Failed", "Invalid username or password for User")
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password for User")
            else:
                messagebox.showerror("Login Failed", "Please fill all the fields")

    def signup(self):
        new_username = self.new_username_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_username and new_password and confirm_password:
            if new_password == confirm_password:
                self.cursor.execute('SELECT username FROM users WHERE username=?', (new_username,))
                if self.cursor.fetchone() is not None:
                    messagebox.showerror('Error', 'Username already exists')
                else:
                    encoded_password = new_password.encode('utf-8')
                    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                    self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                                        (new_username, hashed_password.decode('utf-8')))
                    self.conn.commit()
                    messagebox.showinfo("Sign Up Successful", f"Account created for {new_username}")
                    self.show_login_frame()
            else:
                messagebox.showerror("Sign Up Failed", "Passwords do not match")
        else:
            messagebox.showerror('Error', 'Please fill all the fields')

    def navigate_to_main(self):
        self.root.destroy()
        os.system("python main.py")

    def navigate_to_admin(self):
        self.root.destroy()
        os.system("python admin_interfaces.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()



