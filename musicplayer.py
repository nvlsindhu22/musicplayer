from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteSong():
    lb.delete(ANCHOR)

def playSong():
    lb.play(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('Music World Happy Playlist')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

song_list = []

for item in song_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addSong_btn = Button(
    button_frame,
    text='Add Song',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addSong_btn.pack(fill=BOTH, expand=True, side=LEFT)

delSong_btn = Button(
    button_frame,
    text='Delete Song',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteSong
)
delSong_btn.pack(fill=BOTH, expand=True, side=LEFT)

playSong_btn = Button(
    button_frame,
    text=' Play',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=playSong
)
playSong_btn.pack(fill=BOTH, expand=True, side=LEFT)
ws.mainloop()
