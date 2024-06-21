from tkinter import *
import pygame
import check_in_ui
import check_out
import get_info
import customer_info
import os
import room_type  # Ensure this is imported correctly
from PIL import Image, ImageTk
import login
import feedback

# Define the base directory path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the audio file path
audio_file_path = os.path.join(BASE_DIR, 'hotel_music.mp3')

pygame.mixer.init()

# Function to play music
def play_music():
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play(loops=0)

class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("K I N G S T O N   H O T E L")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Play the music
        play_music()

        # Set the background color
        self.root.configure(bg="#c9c1a7")

        # Create a main frame to add a message
        top = Frame(self.root)
        top.pack(side="top")

        # Create a frame to add buttons
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # Create a label to display the hotel name
        self.label = Label(top, font=('Times', 50, 'bold'), text="K I N G S T O N  HOTEL ♕", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.grid(row=0, column=3)

        # Create a check-in button
        self.check_in_button = Button(bottom, text="CHECK IN", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                      width=50,
                                      fg="#ffe9a1", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # Call the check-in UI function
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # Create a check-out button
        self.check_out_button = Button(bottom, text="CHECK OUT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=check_out.check_out_ui)  # Call the check-out UI function
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        self.room_type_button = Button(bottom, text="FEEDBACK", font=('Times', 20), bg="#948363", relief=RIDGE,
                                       height=2, width=50, fg="#ffe9a1", anchor="center", command=feedback.feedback_ui)
        self.room_type_button.grid(row=2, column=2, padx=10, pady=10)

        # Create an exit button
        self.exit_button = Button(bottom, text="EXIT", font=('Times', 20), bg="#948363", relief=RIDGE, height=2, width=50,
                                  fg="#ffe9a1",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=3, column=2, padx=10, pady=10)

        # Create a customer information button (initially disabled)
        self.room_info_button = Button(bottom, text="CUSTOMER INFORMATION 🔒", font=('Times', 20), bg="#948363", relief=RIDGE,
                                       height=2,
                                       width=50, fg="#ffe9a1", anchor="center",
                                       command=get_info.get_info_ui, state=DISABLED)  # Locked
        self.room_info_button.grid(row=4, column=2, padx=10, pady=10)

        # Create a list of customers button (initially disabled)
        self.get_info_button = Button(bottom, text="LIST OF CUSTOMER 🔒", font=('Times', 20), bg="#948363",
                                      relief=RIDGE,
                                      height=2, width=50, fg="#ffe9a1", anchor="center",
                                      command=customer_info.customer_info_ui, state=DISABLED)  # Locked
        self.get_info_button.grid(row=5, column=2, padx=10, pady=10)

def start_main():
    root = Tk()
    application = Hotel(root)
    root.mainloop()

if __name__ == '__main__':
    start_main()




