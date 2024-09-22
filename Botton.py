from kivy.app import App
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        self.count = 0  # Inicializa o contador

        button = Button(
            text='Fl Galera',
            size_hint=(.5, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        self.count += 1  # Incrementa o contador a cada clique
        print(f"Você apertou o botão {self.count} vez(es)")

if __name__ == '__main__':
    app = MainApp()
    app.run()
