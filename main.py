from kivy.config import Config
Config.set('graphics', 'resizable', '0')
# Config.set('graphics', 'width', '400')
# Config.set('graphics', 'height', '500')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

Window.size = (400, 500)

save_input = ''

class Interface(BoxLayout):
    screen = ObjectProperty()

    def calc(self, instance):
        global save_input
        if instance.text is 'C':
            save_input = self.screen.text = ''
        elif instance.text is not '=':
            save_input += instance.text
            self.screen.text += instance.text
        else:
            try:
                save_input = self.screen.text = str(eval(save_input))
            except:
                save_input = self.screen.text = ''

class CalculatorApp(App):
    title = 'KivyCalculator'
    def build(self):
        return Interface()

if __name__=='__main__':
    CalculatorApp().run()