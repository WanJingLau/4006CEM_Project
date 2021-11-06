from tkinter import *
import pygame


def music():
    global music_screen
    music_screen = Toplevel()
    
    txt_music_title = "Sound Effects"
    txt_music = "Would you like to on sound effects of the application?"
    geometry_size = "1300x700"

    music_screen.title(txt_music_title)
    music_screen.geometry(geometry_size)

    Label(music_screen, text =  txt_music_title, font = ("Helvetica", 12).place(x=200, y=200)
    Button(music_screen, text = txt_music, font = ("Helvetica", 12), width=16, height=1, cursor="hand2", command = lambda txt_romance=txt_romance: redirect_book_list(txt_romance)).place(x=872.5,y=580)
    

# https://www.myinstants.com/media/sounds/anime-wow-sound-effect-mp3cut.mp3
def wow():
    pygame.mixer.music.load()



# https://www.myinstants.com/instant/spongebob-a-few-moments-later-/
def afewmoments():
    pygame.mixer.music.load()



# https://www.youtube.com/watch?v=h6_8SlZZwvQ