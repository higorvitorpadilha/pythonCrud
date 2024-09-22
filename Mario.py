from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img = AsyncImage(
            source='https://i1.sndcdn.com/artworks-000435591132-l6c2ir-t500x500.jpg',
            size_hint=(1, .5),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        return img

# O bloco abaixo deve ficar fora da classe
if __name__ == '__main__':
    app = MainApp()
    app.run()
