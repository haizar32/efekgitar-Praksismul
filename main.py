import matplotlib.pyplot as plt
import pygame.mixer as mx
import soundfile as sf
from tkinter import *
import librosa


def distortion(x):
    N = len(x)
    y = []
    th = 1/10
    for i in range(N):
        if abs(x[i])<th: y.append(2*x[i])
        elif abs(x[i])>=th:
            if x[i]>0: y.append((3-(2-x[i]*3)**2)/3)
            elif x[i]<0: y.append((-(3-(2-abs(x[i])*3)**2))/3)
        elif abs(x[i]) > 2*th:
            if x[i]>0: y.append(1)
            elif x[i]<0: y.append(-1)
    return y

root = Tk()

y, sr = librosa.load("Guitar.wav")
x =  distortion(y)

sf.write('Product.wav', x, sr, subtype='PCM_16')

def plot():
    plt.plot(x)
    plt.show()

def plot_ori():
    plt.plot(y)
    plt.show()

def stop():
    mx.music.stop()

def play_ori():
    mx.init()
    mx.music.load('Guitar.wav')
    mx.music.play()

def play():
    mx.init()
    mx.music.load('Product.wav')
    mx.music.play()

button1 = Button(root,text='Play Distorted',command=play,bg='green',fg='white')
button1.pack(side=LEFT)
button2 = Button(root,text='Play Original',command=play_ori,bg='green',fg='white')
button2.pack(side=LEFT)
button3 = Button(root,text='Show Distorted Wavefrom',command=plot,bg='blue',fg='white')
button3.pack(side=LEFT)
button4 = Button(root,text='Show Original Wavefrom',command=plot_ori,bg='blue',fg='white')
button4.pack(side=LEFT)
button5 = Button(root,text='Stop',command=stop,bg='red',fg='white')
button5.pack(side=RIGHT)

root.mainloop()


