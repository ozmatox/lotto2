from kivy.app import App
from kivy.uix.label import Label

class Lotto2App(App):
    def build(self):
        return Label(text="Lotto2 App")

if __name__ == "__main__":
    Lotto2App().run()
