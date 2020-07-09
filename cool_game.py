from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Button
import game
import Dodge
import Dodge2
import duck
class app():
	def __init__(self):
		window=Tk()
		window.title("Cool Games")
		window.iconbitmap(r"img\tkicon.ico")
		# window.config(bg="#ffff00")
		Label(window,text="_____________________________________").grid(row=0,column=0)
		Label(window,text="Cool Games",font="freesanbold.ttf 40 bold italic").grid(row=0, column=1)
		Label(window,text="_____________________________________").grid(row=0,column=2)
		games=Frame(window)
		games.config(background="blue")
		Label(window,text="Select The Game you wnt to play",font='none 15 italic').grid(row=1,column=0)
		# games=Tk()
		games.grid(row=2,column=0,sticky=W)

		# games.pack()
		Button(games,text="__Dodge Box__",command=lambda:self.select(window,1)).grid(column=0,row=0)
		Button(games,text="Dodge Box 2.0",command=lambda:self.select(window,2)).grid(column=0,row=1)
		Button(games,text="__Duck game__",command=lambda:self.select(window,3)).grid(column=0,row=2)
		Button(games,text="____S P P S___",command=lambda:self.select(window,4)).grid(column=0,row=3)

		intro=Frame(window)
		# intro.config(bg="red")
		intro.grid(row=1,column=2,sticky=E)
		intro_text=["About the Developer:"," Name:T Prajwal prabhu "," Built using:Python","Date:6/6/2020",]

		r=0
		c=0
		for text in intro_text:
			Label(intro,text=text,font="none 15 italic").grid(row=r,column=c,sticky=W)
			r+=1
			if r==1:
				c+=1
		
		img=self.image(r"img\_dodge.png")
		imag=Label(image=img).grid(row=4,column=0)

		img1=self.image(r"img\dodge3.png")
		imag1=Label(image=img1).grid(row=4,column=1)

		img2=self.image(r"img\duck.png")
		imag2=Label(image=img2).grid(row=4,column=2)

		img3=self.image(r"img\spss.png")
		imag3=Label(image=img3).grid(row=5,column=0)
		window.mainloop()


	def image(self,img):
		load=Image.open(img)
		render=ImageTk.PhotoImage(load)
		return render

	def select(self,window,id):
		window.destroy()
		if id==1:
			self.Dodge()
		elif id==2:
			self.Dodge2()
		elif id==3:
			self.Duck()
		elif id==4:
			self.SPPS()





	def Dodge(self):
		intro_text=["In this game have to just miss the box from hitting the moving box","Use arrow key to move left or right"]
		dodge=Tk()  
		dodge.title("Doge Box")
		dodge.iconbitmap(r"img\tkicon.ico")
		dodge_=Frame(dodge)
		dodge_.grid(row=1,column=0)		
		Label(dodge,text="Dodge Box",font="freesanbold.ttf 40 bold italic").grid(row=0, column=1)
		
		r=0
		c=0
		for text in intro_text:
			Label(dodge_,text=text,font="none 15 italic").grid(row=r,column=c,sticky=W)
			r+=1

		image=self.image(r"img\dodge.png")
		img=Label(image=image)
		img.grid(row=2 ,column=0)
		image1=self.image(r"img\dodge1.png")
		img1=Label(image=image1)
		img1.grid(row=2,column=1)
		Label(dodge,text="To Play The game click->" ,font="none 19 bold").grid(row=3, column=0)
		Button(dodge,text="Play",command=Dodge.intro).grid(row=3,column=1)

		dodge.mainloop()		

	def Dodge2(self):

		intro_text=["In this game have to just miss the box from hitting the moving box","Use arrow key to move left or right","There are three levels:","hard","medium","easy"]
		dodge=Tk()  
		dodge.title("Doge Box")
		dodge.iconbitmap(r"img\tkicon.ico")
		dodge_=Frame(dodge)
		dodge_.grid(row=1,column=0)		
		Label(dodge,text="Dodge Box 2.0",font="freesanbold.ttf 40 bold italic").grid(row=0, column=1)
		
		r=0
		c=0
		for text in intro_text:
			Label(dodge_,text=text,font="none 15 italic").grid(row=r,column=c,sticky=W)
			r+=1

		image=self.image(r"img\_dodge.png")
		img=Label(image=image)
		img.grid(row=2 ,column=0)
		image1=self.image(r"img\_dodge1.png")
		img1=Label(image=image1)
		img1.grid(row=2,column=1)
		image2=self.image(r"img\dodge2.png")
		img2=Label(image=image2)
		img2.grid(row=3,column=0)
		image3=self.image(r"img\dodge3.png")
		img3=Label(image=image3)
		img3.grid(row=3,column=1)
		Label(dodge,text="To Play The game click->" ,font="none 19 bold").grid(row=4, column=0)
		Button(dodge,text="Play",command=Dodge2.start).grid(row=4,column=1)

		dodge.mainloop()		

	def Duck(self):

		intro_text=["The game is similer to snack game ","Use arrow key to move up or down","And touch tne red box some times magic happence and the box will disapeare"]
		dodge=Tk()  
		dodge.title("Duck Game")
		dodge.iconbitmap(r"img\tkicon.ico")
		dodge_=Frame(dodge)
		dodge_.grid(row=1,column=0)		
		Label(dodge,text="Duck Game",font="freesanbold.ttf 40 bold italic").grid(row=0, column=1)
		
		r=0
		c=0
		for text in intro_text:
			Label(dodge_,text=text,font="none 15 italic").grid(row=r,column=c,sticky=W)
			r+=1

		image=self.image(r"img\duck.png")
		img=Label(image=image)
		img.grid(row=2 ,column=0)
		image1=self.image(r"img\duck1.png")
		img1=Label(image=image1)
		img1.grid(row=2,column=1)
		image2=self.image(r"img\duck2.png")
		img2=Label(image=image2)
		img2.grid(row=3,column=0)
		
		Label(dodge,text="To Play The game click->" ,font="none 19 bold").grid(row=3, column=1)
		Button(dodge,text="Play",command=duck.intro ).grid(row=3,column=2)

		dodge.mainloop()		

	def SPPS(self):

		intro_text=["Hi this game is called 'Stone paper Penncil Scissor'","Winning Rules are:","stone vs paper=paper(winner)","stone vs pencil=Stone","stone vs sicssor=Stone","Paper vs pencil=pencil","Paper vs sicssor=sicssor","pencil vs sicssor=sicssor"]
		dodge=Tk()  
		dodge.title("SPPS")
		dodge.iconbitmap(r"img\tkicon.ico")
		dodge_=Frame(dodge)
		dodge_.grid(row=1,column=0)		
		Label(dodge,text="SPPS",font="freesanbold.ttf 40 bold italic underline").grid(row=0, column=1)
		
		r=0
		c=0
		for text in intro_text:
			Label(dodge_,text=text,font="none 15 italic").grid(row=r,column=c,sticky=W)
			r+=1

		image=self.image(r"img\spss.png")
		img=Label(image=image)
		img.grid(row=2 ,column=0)
		image1=self.image(r"img\spss1.png")
		img1=Label(image=image1)
		img1.grid(row=2,column=1)
		image2=self.image(r"img\spss2.png")
		img2=Label(image=image2)
		img2.grid(row=2,column=2)
		image3=self.image(r"img\spss3.png")
		img3=Label(image=image3)
		img3.grid(row=3,column=0)
		
		Label(dodge,text="To Play The game click->" ,font="none 19 bold").grid(row=3, column=1)
		Button(dodge,text="Play",command=game.main ).grid(row=3,column=2)

		dodge.mainloop()		

app()


