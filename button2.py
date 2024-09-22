from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        button = Button(text='Clique aqui')
        button.bind(on_press=self.on_press_button)  # Vincula o método ao evento on_press
        return button

    def on_press_button(self, instance):  # 'instance' é o botão que disparou o evento
        print("Você apertou o botão!")

if __name__ == '__main__':
    app = ButtonApp()
    app.run()
