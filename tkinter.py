from tkinter import *
t = Tk()

def buttonpress():
	Label(t, font = (60)).grid(row = 5, column = 2)
t.geometry("600x600")
t.title("Join the Game")
Label(t, text="INSTRUCTIONS: Press the button and see what happens!").grid()

a = ["Option1", "Option2", "Option3"]

for i in a:
	j = lambda y = i:buttonpress(y)
	Button(t, text = i, bg = "black", fg = "white", width = 10, height = 2,
	 command=j).grid(row = i, column = 1, pady = 6)



t.mainloop()
