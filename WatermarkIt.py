import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

from tkinter.filedialog import askopenfilename


def watermark_image():

    picture_id = askopenfilename(initialdir='../Users/wtpar/Pictures', title='Select a File',
                                 filetype=(('jpeg files', '*.jpg'),('all files', '*.*')))
    if picture_id:
        # assuming the picture is found, grab the input from program and add it to image
        watermark_text = watermark_entry.get()
        with Image.open(picture_id).convert('RGBA') as picture:

            # make blank image for watermark text to overlay on the image
            text = Image.new('RGBA', picture.size, (255,255,255,0))

            # using ImageDraw, create the text to overlay
            draw = ImageDraw.Draw(text)

            # necessary to pick a font, any font will do but .ttf required on end
            font = ImageFont.truetype('arial.ttf',size=40, encoding='unic')

            # draw text, half opacity, color is white but can change by tweeking the tuple in fill
            draw.text((picture.size[0]/2, picture.size[1]/2), f'© {watermark_text}', font=font, fill=(255,255,255,128))

            # spit out the image and convert it to a savable file type
            out = Image.alpha_composite(picture,text).convert('RGB')

            # specify the file name, wont give error if file with same name already exists it seems
            watermarked_picture_name = picture_id[:-4] + '_watermarked.jpg'
            out.show()  # show the image and save!
            out.save(watermarked_picture_name)

            # let user know it was successful
            messagebox.showinfo(title='Success!', message=f'Picture watermarked and saved as {watermarked_picture_name}')


# offer option to close program
def shutdown():
    screen.destroy()


# set up the GUI interface

screen = tk.Tk()
screen.title('Watermark It Before You Lose It!')
screen.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=300, bg='white', highlightthickness=0)

watermark_query = tk.Label(text='What would you like for your watermark to say?: ')
watermark_query.grid(row=1, column=0)

watermark_entry = tk.Entry()
watermark_entry.grid(row=1, column=1)
watermark_entry.focus() # will put the cursor here to save user time

# execute watermarking button
enter_button = tk.Button(text='Find Image to Watermark', command=watermark_image)
enter_button.grid(row=2,column=0)

# shut down program
shutdown_button = tk.Button(text='Close Program', command=shutdown)
shutdown_button.grid(row=2, column=1)

# tell the screen to show up and stay up
screen.mainloop()
