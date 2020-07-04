from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class CalculatorApp(App):
    def build(self):
        self.formula = '0'

        main = BoxLayout(orientation = 'vertical', padding = 5)
        calc_buttons = GridLayout(cols = 4, spacing = 3, size_hint = (1, .6))

        self.lbl = Label(text = '0', size_hint = (1, .4), font_size = 40, halign = 'right', valign = 'center', text_size= (400 - 50, 500 * .4 - 50 ))


        calc_buttons.add_widget( Button(text = '7', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '8', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '9', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '/', on_press = self.add_operation) )

        calc_buttons.add_widget( Button(text = '4', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '5', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '6', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = 'x', on_press = self.add_operation) )

        calc_buttons.add_widget( Button(text = '1', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '2', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '3', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '-', on_press = self.add_operation) )


        calc_buttons.add_widget( Button(text = '.', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '0', on_press = self.add_number) )
        calc_buttons.add_widget( Button(text = '=', on_press = self.calc_result) )
        calc_buttons.add_widget( Button(text = '+', on_press = self.add_operation) )

        main.add_widget(self.lbl)
        main.add_widget(calc_buttons)
        return main

    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        if (self.formula[-2] == instance.text or self.formula[-2] == '+' or self.formula[-2] == '-' or self.formula[-2] == '/' or self.formula[-2] == 'x'):
            self.formula = self.formula[:-2]
            self.formula += str(instance.text)
        self.update_label()

    def update_label(self):
        self.lbl.text = self.formula

    def calc_result(self, instance):
        self.lbl.text = self.lbl.text.replace('x', '*')
        try:
            self.lbl.text = str(eval(self.lbl.text))
        except:
            self.formula = "ERROR"
            self.update_label()
        self.formula = "0"

if __name__ == "__main__":
    CalculatorApp().run()
