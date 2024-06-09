from tkinter import *
from tkinter import ttk
import get_info
import customer_info
from room_availability import room_availability_ui

class HotelAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L")
        self.root.geometry("800x600")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True)

        # Title label
        self.label = Label(self.main_frame, text="Admin", font=('Times', 50, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Button styles
        self.button_style = ttk.Style()
        self.button_style.configure('Admin.TButton', font=('Times', 20), background="#948363", foreground="#ffe9a1")

        # Customer Information Button
        self.room_info_button = ttk.Button(self.main_frame, text="CUSTOMER INFORMATION", style='Admin.TButton',
                                           command=self.show_customer_info)
        self.room_info_button.pack(pady=10)

        # List of Customers Button
        self.get_info_button = ttk.Button(self.main_frame, text="LIST OF CUSTOMERS", style='Admin.TButton',
                                          command=self.show_customer_list)
        self.get_info_button.pack(pady=10)

        # Room Availability Button
        self.room_availability_button = ttk.Button(self.main_frame, text="ROOM AVAILABILITY", style='Admin.TButton',
                                                   command=self.show_room_availability)
        self.room_availability_button.pack(pady=10)

        # Separator
        self.separator = ttk.Separator(self.main_frame, orient=HORIZONTAL)
        self.separator.pack(fill=X, pady=20)

        # Exit Button
        self.exit_button = ttk.Button(self.main_frame, text="EXIT", style='Admin.TButton', command=self.exit_app)
        self.exit_button.pack(pady=10)

    def show_customer_info(self):
        get_info.get_info_ui()  # Call get_info_ui function from get_info.py file

    def show_customer_list(self):
        customer_info.customer_info_ui()  # Call customer_info_ui function from customer_info.py file

    def show_room_availability(self):
        room_availability_ui()  # Call room_availability_ui function for room availability

    def exit_app(self):
        self.root.destroy()

# Create the main application window
root = Tk()
app = HotelAdmin(root)
root.mainloop()
