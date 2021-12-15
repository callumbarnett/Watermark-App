from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import tkfilebrowser as tkf


def chosen_image():
    global display_img
    global test
    file = tkf.askopenfilename(parent=root,
                               initialdir='/',
                               initialfile='tmp',
                               filetypes=[("Pictures", "*.png|*.jpg|*.JPG"),
                                          ("All files", "*")])

    open_img = Image.open(file)
    # open_img.save()
    resized = open_img.resize((500, 500), Image.ANTIALIAS)
    fmt_image = ImageTk.PhotoImage(resized)
    display_img = fmt_image
    image_label.config(image=display_img)
    test = open_img


def watermark():
    global display_img
    global test

    watermark_image = test

    draw = ImageDraw.Draw(watermark_image)
    # ("font type",font size)
    font = ImageFont.truetype("arial.ttf", 50)

    # add Watermark
    # (255,255,255)-White color text
    draw.text((0, 0), "That'sMine.com", (255, 255, 255), font=font)
    plt.subplot(1, 2, 2)
    plt.title("white text")
    watermark_image.show()


root = Tk()
root.title('Watermarker')
root.configure(background='#D3D3D3')
root.minsize(500, 500)
root.maxsize(1000, 1000)

# Font
button_font = font.Font(family='Corbel')

# Preset Image
image = Image.open('Scotland.png')
resized_img = image.resize((500, 500), Image.ANTIALIAS)
test = ImageTk.PhotoImage(resized_img)
display_img = test

select_button = Button(root, text='Choose Image', font=button_font, command=chosen_image).grid(column=5, row=5,
                                                                                               padx=100, pady=100,
                                                                                               ipadx=50, ipady=50)
watermark_button = Button(root, text="Add Watermarker", font=button_font, command=watermark).grid(column=5, row=6,
                                                                                padx=100, pady=100,
                                                                                ipadx=50, ipady=50)

image_label = Label(text='Image', image=display_img)
image_label.grid(column=0, columnspan=5, row=0, rowspan=10, padx=10)
#image_label.place(x=10, y=10)
root.mainloop()
