import sqlite3
from tkinter import *
from PIL import Image, ImageTk

# Global variable to store the single room image
single_room_image = None

class RoomType:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("ROOM TYPE")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")
        
        top = Frame(self.root, bg="#c9c1a7")
        top.pack(side="top", fill="x")

        middle = Frame(self.root, bg="#c9c1a7")
        middle.pack(expand=True)

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="bottom", fill="x")

        self.label = Label(top, font=('Times New Roman', 50, 'bold'), text="ROOM TYPE", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.pack(pady=10)

        # Room type information
        self.room_types = [
            "Single Room",
            "Double Room",
            "Suite",
            "Family Room"
        ]

        self.create_room_type_selection(middle)

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

    def create_room_type_selection(self, parent):
        for room_type in self.room_types:
            frame = Frame(parent, bg="#c9c1a7", relief="solid", bd=2)
            frame.pack(fill="x", padx=10, pady=5)
            
            # Create a button for the room type
            button = Button(frame, font=('Times New Roman', 16), text=room_type, fg="#725700", anchor="center", bg="#c9c1a7", padx=10, pady=5, width=20, command=lambda rt=room_type: self.go_to_room_details(rt))
            button.pack(fill="both", expand=True)

    def go_to_room_details(self, room_type):
        if room_type == "Single Room":
            self.display_single_room_image()
        else:
            self.root.destroy()
            room_details_ui(room_type)

    def display_single_room_image(self):
        global single_room_image
        self.root.destroy()
        single_room_image = Image.open(r"C:\Users\MEGAT\Desktop\MegatBranch\PROJECT-TT9L-06\Hotel Reservation System\single_room.jpg")
        single_room_ui()

    def go_back(self):
        self.root.destroy()

def single_room_ui():
    root = Tk()
    app = SingleRoom(root)
    root.mainloop()

class SingleRoom:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Single Room")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")
        
        top = Frame(self.root, bg="#c9c1a7")
        top.pack(side="top", fill="x")

        middle = Frame(self.root, bg="#c9c1a7")
        middle.pack(expand=True)

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="bottom", fill="x")

        self.label = Label(top, font=('Times New Roman', 50, 'bold'), text="Single Room", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.pack(pady=10)

        # Load and display the image
        global single_room_image
        self.photo = ImageTk.PhotoImage(single_room_image)

        self.image_label = Label(middle, image=self.photo, bg="#c9c1a7")
        self.image_label.image = self.photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=20)

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.root.destroy()
        room_type_ui()

def room_details_ui(room_type):
    root = Tk()
    app = RoomDetails(root, room_type)
    root.mainloop()

class RoomDetails:

    def __init__(self, root, room_type):
        self.root = root
        pad = 3
        self.root.title(f"{room_type} Details")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")
        
        top = Frame(self.root, bg="#c9c1a7")
        top.pack(side="top", fill="x")

        middle = Frame(self.root, bg="#c9c1a7")
        middle.pack(expand=True)

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="bottom", fill="x")

        self.label = Label(top, font=('Times New Roman', 50, 'bold'), text=f"{room_type} Details", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.pack(pady=10)

        # Add your room details content here
        # This can include images, descriptions, prices, etc.

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

    def go_back(self):
        self.root.destroy()
        room_type_ui()

def room_type_ui():
    root = Tk()
    app = RoomType(root)
    root.mainloop()




