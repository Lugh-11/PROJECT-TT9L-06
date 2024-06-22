import sqlite3
from tkinter import *
from tkinter.ttk import Separator
from tkinter import messagebox
import main

class CheckOut:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("CHECK OUT")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Change background color for check-out page
        self.root.config(bg="#c9c1a7")

        # Main frame to hold all widgets
        main_frame = Frame(self.root, bg="#c9c1a7")
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Configure grid to center widgets
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)
        main_frame.grid_rowconfigure(4, weight=1)
        main_frame.grid_rowconfigure(5, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Title
        self.label = Label(main_frame, font=('Times', 50, 'bold'), text="CHECK OUT", fg="#ffe9a1", anchor="center",
                           bg="#725700", borderwidth=5, relief="groove", padx=20, pady=10)
        self.label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

        # Room Number Entry
        self.room_no_label = Label(main_frame, font=('Times', 20, 'bold'), text="ENTER THE ROOM NUMBER:", fg="#ffe9a1",
                                   anchor="center", bg="#948363")
        self.room_no_label.grid(row=1, column=0, pady=10, sticky="e")

        self.room_var = IntVar()
        self.room_no_entry = Entry(main_frame, width=10, textvariable=self.room_var, font=('Times', 20))
        self.room_no_entry.grid(row=1, column=1, pady=10, sticky="w")

        # Separator
        separator = Separator(main_frame, orient='horizontal')
        separator.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)

        # Information Text Box
        self.get_info_entry = Text(main_frame, height=15, width=90, font=('Times', 12))
        self.get_info_entry.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Buttons Frame
        button_frame = Frame(main_frame, bg="#c9c1a7")
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        # Center the button frame
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        # Check Out Button
        self.check_out_button = Button(button_frame, text="CHECK OUT", font=('', 15), bg="#948363", relief=RIDGE,
                                       height=2, width=15, fg="#ffe9a1", anchor="center", command=self.check_out)
        self.check_out_button.grid(row=0, column=0, padx=10)

        # Home Button
        self.home_button = Button(button_frame, text="HOME", font=('', 15), bg="#948363", relief=RIDGE,
                                  height=2, width=15, fg="#ffe9a1", anchor="center", command=self.return_to_main_page)
        self.home_button.grid(row=0, column=1, padx=10)

    def check_out(self):
        room_number1 = int(self.room_no_entry.get())
        conn = sqlite3.connect('NewHotel.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS NewHotelTable (Fullname TEXT, Address TEXT, mobile_number TEXT, number_days TEXT,'
            ' room_number NUMBER, room_type TEXT, number_of_guests NUMBER, hotel_view TEXT)')
        conn.commit()
        with conn:
            cursor.execute("SELECT room_number FROM NewHotelTable")
            ans = cursor.fetchall()
            room = [i[0] for i in ans]
            if room_number1 in room:
                with conn:
                    cursor.execute("SELECT Fullname, room_number FROM NewHotelTable")
                    ans = cursor.fetchall()
                    for i in ans:
                        if room_number1 == int(i[1]):
                            self.get_info_entry.insert(INSERT,
                                                       '\n' + str(i[0]) + ' has checked out from room ' + str(i[1]) + '\n')
                            with conn:
                                cursor.execute("""DELETE FROM NewHotelTable WHERE room_number = ?""", [room_number1])
                            messagebox.showinfo("Success", "Check-out Successful!")
                            self.return_to_main_page()
            else:
                self.get_info_entry.insert(INSERT, "PLEASE ENTER A VALID ROOM NUMBER")

    def return_to_main_page(self):
        self.root.destroy()
        main.home_ui()

def check_out_ui():
    root = Tk()
    application = CheckOut(root)
    root.mainloop()

