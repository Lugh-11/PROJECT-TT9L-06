from tkinter import *
from tkinter.font import Font
import check_in_ui
import check_out
import get_info
import customer_info
import os

#CHANGING HOTEL NAME
class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # set background color
        self.root.configure(bg="#c9c1a7")

        # create mainframe to add message
        top = Frame(self.root)
        top.pack(side="top")

        # create frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # display message
        self.label = Label(top, font=('Times', 50, 'bold'), text="K I N G S T O N  HOTEL", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.grid(row=0, column=3)

        # create check in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                      width=50,
                                      fg="#ffe9a1", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # call check_in_ui_fun from check_in_ui.py file
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # create check out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=check_out.check_out_ui)  # call check_out_ui function from check_out.py file
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # create show list button
        self.room_info_button = Button(bottom, text="ROOMS INFORMATION", font=('Times', 20), bg="#948363", relief=RIDGE,
                                       height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=get_info.get_info_ui)  # call get_info_ui function from get_info.py file
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # create get information of all the guest
        self.get_info_button = Button(bottom, text="GUEST INFORMATION", font=('Times', 20), bg="#948363",
                                      relief=RIDGE,
                                      height=2, width=50, fg="#ffe9a1", anchor="center",
                                      command=customer_info.customer_info_ui)
        # call customer_info_ui function from customer_info.py file
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # button to exit the program
        self.exit_button = Button(bottom, text="EXIT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2, width=50,
                                  fg="#ffe9a1",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()

