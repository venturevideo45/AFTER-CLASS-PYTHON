import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_popup():
    messagebox.showinfo("Liked", "You liked the Mahindra Thar!")

def open_details():
    win = tk.Toplevel(root)
    win.title("Details")
    tk.Label(win, text="Mahindra Thar\n4x4 Off-Road SUV", font=("Arial", 12)).pack(pady=20)

root = tk.Tk()
root.title("Thar Album")

# Title
tk.Label(root, text="Mahindra Thar", font=("Arial", 14, "bold")).pack(pady=5)

# Load Image
try:
    img = Image.open("D:\\CODING FILE\\AFTER CLASS PYTHON\\PHOTO ALBUM\\thar.jpg").resize((300, 200))
    photo = ImageTk.PhotoImage(img)
    tk.Label(root, image=photo).pack(pady=5)
except:
    tk.Label(root, text="[ Image 'thar.jpg' missing ]").pack(pady=20)

# Buttons
tk.Button(root, text="Like", command=show_popup).pack(side="left", padx=20, pady=10)
tk.Button(root, text="Details", command=open_details).pack(side="right", padx=20, pady=10)

root.mainloop()
