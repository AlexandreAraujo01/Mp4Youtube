from tkinter import *
from tkinter import filedialog
from turtle import color
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


#functions

def selected_path():
    # allow user to select a path on your pc
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    # get user path
    get_link = link_field.get()
    # get select path
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    # download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete My Friend!.')
    
    

screen = Tk()
tittle = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()


# image logo
logo_img = PhotoImage(file='comu.png')
# resize
logo_img = logo_img.subsample(2,2)

canvas.create_image(250, 250, image=logo_img)

# select path for download
path_label = Label(screen, text="Select the Path for Download: ",font=('Roboto',11),background='#f00',fg='#fff')
select_btn = Button(screen, text="Choose Path",font=('Roboto',10),command=selected_path)

# link field)
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter The Download Link Továrisch: ",font=('Roboto',13),background='#f00',fg='#fff')

#download btns
download_btn = Button(screen,text="Download File",command=download_file)


# add  widgets to window
canvas.create_window(250,350, window=link_label)
canvas.create_window(250,375, window=link_field)
canvas.create_window(50,20, window=select_btn)
canvas.create_window(250,410, window=download_btn)

# link change
canvas.create_window(250,475, window=path_label)



screen.mainloop()