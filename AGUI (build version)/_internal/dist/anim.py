import tkinter as tk
import customtkinter as ctk

# List of images
images = ["img/img1.png", "img/img2.png", "img/img3.png"]
current_image = 1

def change_image():
    global current_image
    if current_image < len(images):
        image = tk.PhotoImage(file=images[current_image])
        label.configure(image=image)
        label.image = image  # Keep a reference to the image
        current_image += 1
    
    if current_image > len(images):
        current_image = 0
        
root = ctk.CTk()
root.title("Animation")
ctk.set_appearance_mode("dark")

w = 854
h = 480

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

# Initial image
image = tk.PhotoImage(file=images[0])
label = ctk.CTkLabel(root, image=image, text="")
label.pack()

change_image_button = ctk.CTkButton(root, text="Change Image", command=change_image, bg_color="gray12", fg_color="gray12")
change_image_button.pack()

root.mainloop()