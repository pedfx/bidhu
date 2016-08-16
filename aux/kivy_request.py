from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from test import Classificar # importa o codigo test pra esse codigo
from kivy.uix.image import Image

class StartScreen(GridLayout):

	def __init__(self, **kwargs):        #declara como vai ser o grid
		super(StartScreen, self).__init__(**kwargs)

		#theclass = Classificar()
		#sourcepath = Classificar.sourcepath
		#self.cols = theclass.numerodeimagens +1
		#self.add_widget(Label(text= theclass.rodar()))
		#for numero in range(0,theclass.numerodeimagens) :
		#	self.add_widget(Image(source=sourcepath+"galaxy"+str(numero+1)+".jpg", allow_stretch=1))

		ra = raw_input("Please write the ra of your desired galaxy: \n")
		dec = raw_input("Please write the dec of your desired galaxy: \n")
		web = "http://skyserver.sdss.org/dr12/en/tools/chart/image.aspx?ra=" + ra + "&dec=" + dec + "&width=512&height=512&scale=0.2"
		print web

		self.cols = 1
		self.add_widget(Label(text=web))

class BIDHU(App):

	def build(self):
		return StartScreen()


if __name__ == '__main__':
	BIDHU().run()
