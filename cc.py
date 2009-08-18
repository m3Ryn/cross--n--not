from Tkinter import *
import tkMessageBox

class MyGame:
	def __init__(self, parent):
		self.MyParent = parent
		self.frame = Frame(parent)
		self.frame.pack()
		self.frame2 = Frame(parent)
		self.frame2.pack()
		self.lastbutton="o"

		self.label = Label(self.frame2, text = "No Overwriting!")

		self.b1 = Button(self.frame, height=4, width=8)
		self.b1.grid(row=0, column=0)
		self.b1.configure(command = self.click1)

		self.b2 = Button(self.frame, height=4, width=8)
		self.b2.grid(row=0, column=1)
		self.b2.configure(command = self.click2)

		self.b3 = Button(self.frame, height=4, width=8)
		self.b3.grid(row=0, column=2)
		self.b3.configure(command = self.click3)

		self.b4 = Button(self.frame, height=4, width=8)
		self.b4.grid(row=1, column=0)
		self.b4.configure(command = self.click4)

		self.b5 = Button(self.frame, height=4, width=8)
		self.b5.grid(row=1, column=1)
		self.b5.configure(command = self.click5)

		self.b6 = Button(self.frame, height=4, width=8)
		self.b6.grid(row=1, column=2)
		self.b6.configure(command = self.click6)

		self.b7 = Button(self.frame, height=4, width=8)
		self.b7.grid(row=2, column=0)
		self.b7.configure(command = self.click7)

		self.b8 = Button(self.frame, height=4, width=8)
		self.b8.grid(row=2, column=1)
		self.b8.configure(command = self.click8)

		self.b9 = Button(self.frame, height=4, width=8)
		self.b9.grid(row=2, column=2)
		self.b9.configure(command = self.click9)

		self.buttonplay = Button(self.frame, text = "Play Again", command = self.Play)
		self.buttonplay.configure(height=2,width=8)
		self.buttonplay.grid(row=4, column=1)

	def oppwin(self):
		result=tkMessageBox.askyesno("Options", "   "+self.lastbutton +" wins!"'\n' "Play Again?")
		if result == True:
			self.Play()
		if result == False:
			self.MyParent.destroy()
			return()

	def Win(self):

		if self.b1["text"]==self.b2["text"]==self.b3["text"]=="X":
			self.oppwin()
		if self.b1["text"]==self.b2["text"]==self.b3["text"]=="O":
			self.oppwin()
		if self.b1["text"]==self.b4["text"]==self.b7["text"]=="X":
			self.oppwin()
		if self.b1["text"]==self.b4["text"]==self.b7["text"]=="O":
			self.oppwin()
		if self.b4["text"]==self.b5["text"]==self.b6["text"]=="X":
			self.oppwin()
		if self.b4["text"]==self.b5["text"]==self.b6["text"]=="O":
			self.oppwin()
		if self.b7["text"]==self.b8["text"]==self.b9["text"]=="X":
			self.oppwin()		
		if self.b7["text"]==self.b8["text"]==self.b9["text"]=="O":
			self.oppwin()
		if self.b2["text"]==self.b5["text"]==self.b8["text"]=="X":
			self.oppwin()
		if self.b2["text"]==self.b5["text"]==self.b8["text"]=="O":
			self.oppwin()		
		if self.b3["text"]==self.b6["text"]==self.b9["text"]=="X":
			self.oppwin()
		if self.b3["text"]==self.b6["text"]==self.b9["text"]=="O":
			self.oppwin()
		if self.b1["text"]==self.b5["text"]==self.b9["text"]=="X":
			self.oppwin()
		if self.b1["text"]==self.b5["text"]==self.b9["text"]=="O":
			self.oppwin()
		if self.b3["text"]==self.b5["text"]==self.b7["text"]=="X":
			self.oppwin()
		if self.b3["text"]==self.b5["text"]==self.b7["text"]=="O":
			self.oppwin()

	def Play(self):
		self.MyParent.destroy()
		root = Tk()
		mygame = MyGame(root)
		root.mainloop()

	def click1(self):
		if self.lastbutton == "o":
			if (self.b1["text"]=="X" or self.b1["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else: 
            
				self.lastbutton = "x"
				self.b1["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b1["text"]=="X" or self.b1["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b1["text"] = "O"
				self.Win()

	def click2(self):
		if self.lastbutton == "o":
			if (self.b2["text"]=="X" or self.b2["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b2["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b2["text"]=="X" or self.b2["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b2["text"] = "O"
				self.Win()

	def click3(self):
		if self.lastbutton == "o":
			if (self.b3["text"]=="X" or self.b3["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b3["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b3["text"]=="X" or self.b3["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b3["text"] = "O"
				self.Win()

	def click4(self):
		if self.lastbutton == "o":
			if (self.b4["text"]=="X" or self.b4["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b4["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b4["text"]=="X" or self.b4["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b4["text"] = "O"
				self.Win()

	def click5(self):
		if self.lastbutton == "o":
			if (self.b5["text"]=="X" or self.b5["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b5["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b5["text"]=="X" or self.b5["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b5["text"] = "O"
				self.Win()

	def click6(self):
		if self.lastbutton == "o":
			if (self.b6["text"]=="X" or self.b6["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b6["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b6["text"]=="X" or self.b6["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b6["text"] = "O"
				self.Win()

	def click7(self):
		if self.lastbutton == "o":
			if (self.b7["text"]=="X" or self.b7["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b7["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b7["text"]=="X" or self.b7["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b7["text"] = "O"
				self.Win()

	def click8(self):
		if self.lastbutton == "o":
			if (self.b8["text"]=="X" or self.b8["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b8["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b8["text"]=="X" or self.b8["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b8["text"] = "O"
				self.Win()

	def click9(self):
		if self.lastbutton == "o":
			if (self.b9["text"]=="X" or self.b9["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "x"
				self.b9["text"] = "X"
				self.Win()
		elif self.lastbutton == "x":
			if (self.b9["text"]=="X" or self.b9["text"]=="O"):
				tkMessageBox.showerror("Invalid Click", "The button can be clicked only once!")
			else:
				self.lastbutton = "o"
				self.b9["text"] = "O"
				self.Win()
	


root = Tk()
root.title("Cross 'n' Nots")
game = MyGame(root)
root.mainloop()