from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from test import Classificar # importa o codigo test pra esse codigo
from kivy.uix.image import Image

class StartScreen(GridLayout):

	def __init__(self, **kwargs):        #declara como vai ser o grid
		super(StartScreen, self).__init__(**kwargs)

		theclass = Classificar()
		sourcepath = Classificar.sourcepath
		self.cols = theclass.numerodeimagens +1
		self.add_widget(Label(text= theclass.rodar()))
		for numero in range(0,theclass.numerodeimagens) :
			self.add_widget(Image(source=sourcepath+"galaxy"+str(numero+1)+".jpg", allow_stretch=1))


class BIDHU(App):

	def build(self):
		return StartScreen()


if __name__ == '__main__':
	BIDHU().run()
