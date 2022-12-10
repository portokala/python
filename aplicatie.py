from tkinter import *
t = Tk()

def buttonpress():
	Label(t, font = (60)).grid(row = 5, column = 2)
t.geometry("600x600")
t.title("Hai sa o inveselim pe Andreiutza")
Label(t, text="INSTRUCTIUNI: Apasa butonul acesta pentru a o gadila pe Andreiutza").grid()

a = ["o gadilam la subrat", "o gadilam pe spate", "o gadilam pe burtica"]

for i in a:
	j = lambda y = i:buttonpress(y)
	Button(t, text = i, bg = "black", fg = "white", width = 10, height = 2,
	 command=j).grid(row = i, column = 1, pady = 6)



t.mainloop()