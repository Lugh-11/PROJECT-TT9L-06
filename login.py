import tkinter as tk
from tkinter import messagebox
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

        # Layout widgets
        self.login_label.pack(pady=20)
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.user_radio.pack()
        self.admin_radio.pack()
        self.login_button.pack(pady=20)

    def initialize_signup_widgets(self):
        # Your signup widgets initialization here
        pass

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

        # You can replace this with your actual database query to check credentials
        if user_type == "User":
            if username == "user" and password == "user":
                messagebox.showinfo("Login Successful", "Welcome, User!")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password for User")
        elif user_type == "Admin":
            if username == "admin" and password == "admin":
                messagebox.showinfo("Login Successful", "Welcome, Admin!")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password for Admin")
        else:
            messagebox.showerror("Login Failed", "Please select User or Admin")

    def signup(self):
        # Your signup method implementation here
        pass

    def navigate_to_main(self):
        # Your navigation to main method implementation here
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()






