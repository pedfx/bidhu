from kivy.app import App # importa a classe app pra o codigo
from kivy.uix.gridlayout import GridLayout # importa o visual de grid
from kivy.uix.label import Label # importa a classe label pra o codigo
from test import Classificar # importa o codigo test pra esse codigo
from kivy.uix.image import Image # importa a classe image pra o codigo

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
