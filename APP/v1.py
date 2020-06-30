from PIL import ImageTk
import PIL.Image
from tkinter import *
import tkinter as tk

windo = Tk()
windo.configure(background='white')
windo.title("Sort App")
windo.geometry('1120x420')
windo.resizable(0,0)

def clear():
    txt2.delete(first=0,last=100)
    T.destroy()
    FA1.destroy()

def search():
    global result,T,FA,FA1
    query = txt2.get()

    def quicksort(tengah, awal, akhir):
        if akhir - awal > 1:
            p = partition(tengah, awal, akhir)
            quicksort(tengah, awal, p)
            quicksort(tengah, p + 1, akhir)
     
     
    def partition(tengah, awal, akhir):
        pivot = tengah[awal]
        i = awal + 1
        j = akhir - 1
     
        while True:
            while (i <= j and tengah[i] <= pivot):
                i = i + 1
            while (i <= j and tengah[j] >= pivot):
                j = j - 1
     
            if i <= j:
                tengah[i], tengah[j] = tengah[j], tengah[i]
            else:
                tengah[awal], tengah[j] = tengah[j], tengah[awal]
                return j
     
    urut = query.split()
    urutan = [int(x) for x in urut]
    quicksort(urutan, 0, len(urutan))
    result = urutan
    T = tk.Text(windo, borderwidth=7, height=1, width=57, font=('times', 16))
    T.place(x=430, y=250)
    T.configure(state='normal')
    T.insert(tk.END, result)
    T.configure(state='disabled')
    FA1 = tk.Button(windo, text="Clear",command = clear, fg="white", bg="red", font=('times', 15, ' bold '))
    FA1.place(x=430, y=300)

def destroy_widget(widget):
    widget.destroy()

im = PIL.Image.open('./meta/a.jpg')
im =im.resize((351,263), PIL.Image.ANTIALIAS)
wp_img = ImageTk.PhotoImage(im)
panel4 = Label(windo, image=wp_img,bg = 'white')
panel4.pack()
panel4.place(x=20, y=100)

im1 = PIL.Image.open('./meta/search.png')
im1 =im1.resize((70,70), PIL.Image.ANTIALIAS)
sp_img = ImageTk.PhotoImage(im1)
panel5 = Button(windo,borderwidth=0,command = search, image=sp_img,bg = 'white')
panel5.pack()
panel5.place(x=920, y=165)

pred = tk.Label(windo, text="Sort App", width=30, height=2, fg="white",bg="black",
                font=('times', 25, ' bold '))
pred.place(x=274, y=10)

lab = tk.Label(windo, text="Masukkan Angka", width=18, height=1, fg="white",bg="blue2",
                font=('times', 16, ' bold '))
lab.place(x=544, y=120)

txt2 = tk.Entry(windo,borderwidth = 7, width=26, bg="white", fg="black", font=('times', 25, ' bold '))
txt2.place(x=430, y=170)

windo.mainloop()
