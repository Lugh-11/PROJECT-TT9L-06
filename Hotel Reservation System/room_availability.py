from tkinter import *
from tkinter import ttk
import sqlite3
import main  

class RoomAvailabilityPage:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("K I N G S T O N  H O T E L - ROOM AVAILABILITY")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label with border
        self.label = Label(self.main_frame, text="Room Availability 🚪", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7", bd=4, relief="groove")
        self.label.pack(pady=20)

        # Results Frame
        self.results_frame = Frame(self.main_frame, bg="#c9c1a7")
        self.results_frame.pack(pady=20)

        # Refresh Button
        self.refresh_button = ttk.Button(self.main_frame, text="REFRESH AVAILABILITY", command=self.update_availability)
        self.refresh_button.pack(pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", command=self.back_to_main)
        self.back_button.pack(pady=10)

        self.update_availability()

    def update_availability(self):
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        conn = sqlite3.connect('NewHotel.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT room_number FROM NewHotelTable''')
        occupied_rooms = [row[0] for row in cursor.fetchall()]
        conn.close()

        row_num = 0
        col_num = 0
        row_frame = None

        for room_number in range(101, 201):
            if col_num == 0:
                row_frame = Frame(self.results_frame, bg="#FFFFFF", bd=2, relief="solid")
                row_frame.grid(row=row_num, column=0, padx=5, pady=5, columnspan=10, sticky='ew')

            if room_number in occupied_rooms:
                color = 'red'
            else:
                color = 'green'

            room_label = Label(row_frame, text=f"🚪{room_number}", font=('Times', 15), fg=color, bg="#c9c1a7")
            room_label.grid(row=0, column=col_num, padx=5, pady=5)

            col_num += 1
            if col_num == 10:
                col_num = 0
                row_num += 1

    def back_to_main(self):
        self.root.withdraw()  # Hide the current window
        admin_root = Tk()  # Create a new window for the admin interface
        admin_interface = main.AdminInterface(admin_root)  # Create an instance of AdminInterface
        admin_root.mainloop()

def room_availability_ui():
    availability_root = Tk()
    app = RoomAvailabilityPage(availability_root)
    availability_root.mainloop()
