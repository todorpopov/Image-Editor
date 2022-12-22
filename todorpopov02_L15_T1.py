from tkinter import *
from PIL import ImageTk, Image, ImageOps, ImageFilter
import os

def list_images():
    list = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in list:
        if not f.endswith(('.jpg', '.png', 'jpeg')):
            list.remove(f)
    return list

def get_attributes(path):
    image = Image.open(path)
    attributes = {
        "Image Format": image.format, 
        "Image Mode": image.mode, 
        "Image Size": image.size, 
        "Image Palette": image.palette
    }
    return attributes


def show_image(img_path):
    attributes = get_attributes(img_path)

    format_label.config(text = "Format: " + str(attributes["Image Format"]))
    mode_label.config(text = "Mode: " + str(attributes["Image Mode"]))
    size_label.config(text = "Size: " + str(attributes["Image Size"]))
    palette_label.config(text = "Palette: " + str(attributes["Image Palette"]))

    image = Image.open(img_path)
    image = image.resize((490,490))
    img = ImageTk.PhotoImage(image)

    canvas.create_image(0,0, image=img, anchor="nw")
    canvas.place(x=245, y=5)
    canvas.image=img


def rotate(img_path):
    image = Image.open(img_path)
    rotated_image = image.rotate(90)
    rotated_image.save(img_path)

def mirror_horizontally(img_path):
    image = Image.open(img_path)
    flipped_image = ImageOps.flip(image)
    flipped_image.save(img_path)

def mirror_vertically(img_path):
    image = Image.open(img_path)
    mirrored_image = ImageOps.mirror(image)
    mirrored_image.save(img_path)

def update(image):
    image_1 = image.resize((490,490))
    img = ImageTk.PhotoImage(image_1)

    canvas.create_image(0,0, image=img, anchor="nw")
    canvas.place(x=245, y=5)
    canvas.image=img

def save_image(image):
    image_1 = image.resize((490,490))
    img = ImageTk.PhotoImage(image_1)
    image.save(images.get())

def blur(image_path):
    image = Image.open(image_path)
    blured_image = image.filter(ImageFilter.BLUR)
    update(blured_image)

    global current_image
    current_image = blured_image

def contour(image_path):
    image = Image.open(image_path)
    contoured_image = image.filter(ImageFilter.CONTOUR)
    update(contoured_image)

    global current_image
    current_image = contoured_image

def emboss(image_path):
    image = Image.open(image_path)
    embossed_image = image.filter(ImageFilter.EMBOSS)
    update(embossed_image)

    global current_image
    current_image = embossed_image

def edge_enhance(image_path):
    image = Image.open(image_path)
    edge_enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)
    update(edge_enhanced_image)

    global current_image
    current_image = edge_enhanced_image


root = Tk()
root.title("Image Editor")
root.geometry("740x500")

list = list_images()
images = StringVar()
images.set("See images")

drop = OptionMenu(root, images, *list)
drop.config(width=10)
drop.grid(row=0, column=0, padx = 5, pady = 5, sticky = "nsew")

show_img_btn = Button(root, text = "Show Image", command = lambda: show_image(images.get()))
show_img_btn.grid(row=0, column=1, padx = 5, pady = 5, sticky = "nsew")

format_label = Label(root, text = "Format: ")
format_label.grid(row=2, column=0, padx = 5, pady = 5, sticky = "nsew")

mode_label = Label(root, text = "Mode: ")
mode_label.grid(row=2, column=1, padx = 5, pady = 5, sticky = "nsew")

size_label = Label(root, text = "Size: ")
size_label.grid(row=3, column=0, padx = 5, pady = 5, sticky = "nsew")

palette_label = Label(root, text = "Palette: ")
palette_label.grid(row=3, column=1, padx = 5, pady = 5, sticky = "nsew")

structure_label = LabelFrame(root, text = "Saved automatically")
structure_label.grid(row=6, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

rotate_btn = Button(structure_label, text = "Rotate 90°", command = lambda: [rotate(images.get()), show_image(images.get())])
rotate_btn.config(width=30)
rotate_btn.grid(row= 0, column=0, padx = 5, pady = 5, sticky = "nsew")

mirror_hor_btn = Button(structure_label, text = "Mirror Horizontally", command = lambda: [mirror_horizontally(images.get()), show_image(images.get())])
mirror_hor_btn.config(width=30)
mirror_hor_btn.grid(row= 1, column=0, padx = 5, pady = 5, sticky = "nsew")

mirror_vert_btn = Button(structure_label, text = "Mirror Vertically", command = lambda: [mirror_vertically(images.get()), show_image(images.get())])
mirror_vert_btn.config(width=30)
mirror_vert_btn.grid(row= 2, column=0, padx = 5, pady = 5, sticky = "nsew")


current_image = None

structure_label_2 = LabelFrame(root, text = "Require to be saved")
structure_label_2.grid(row=7, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

blur_btn = Button(structure_label_2, text = "Blur Filter", command = lambda: blur(images.get()))
blur_btn.config(width=30)
blur_btn.grid(row= 0, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

contour_btn = Button(structure_label_2, text = "Contour Filter", command = lambda: contour(images.get()))
contour_btn.config(width=30)
contour_btn.grid(row= 1, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

emboss_btn = Button(structure_label_2, text = "Emboss Filter", command = lambda: emboss(images.get()))
emboss_btn.config(width=30)
emboss_btn.grid(row= 2, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

edge_enhance_btn = Button(structure_label_2, text = "Edge Enhance Filter", command = lambda: edge_enhance(images.get()))
edge_enhance_btn.config(width=30)
edge_enhance_btn.grid(row= 3, column=0, columnspan=2, padx = 5, pady = 5, sticky = "nsew")

undo_btn = Button(structure_label_2, text = "Undo", command = lambda: show_image(images.get()))
#undo_btn.config(width=10)
undo_btn.grid(row = 4, column=0, padx = 5, pady = 5, sticky = "nsew")

save_btn = Button(structure_label_2, text = "Save", command = lambda: save_image(current_image))
#save_btn.config(width=10)
save_btn.grid(row = 4, column=1, padx = 5, pady = 5, sticky = "nsew")

canvas = Canvas(root, bg = "white", height=490, width = 490)
canvas.place(x=245,y=5)

root.mainloop()