"""Пакет Front. Содержит класс главного окна, Ui классы и главный цикл приложения.
 Данный пакет отвечает за визуальную составляющую. Классы данного пакета не поддерживают
 сложную логику. Основные вычисления проводятся в классах пакета BackPackage"""

import BackPackage
from kivy.app import App
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        img = Image(source='/path/to/real_python.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x': .5, 'center_y': .5})

        return img


if __name__ == '__main__':
    app = MainApp()
    app.run()