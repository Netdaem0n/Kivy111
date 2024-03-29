# расположение виджетов "друг на друге"
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
   def build(self):
      txt = Label(text='Это надпись')
      btn = Button(text='Это кнопка')
      btn.add_widget(Button(text='Тоже кнопка')) # новая кнопка - потомок первой кнопки
      layout = BoxLayout()
      layout.add_widget(txt)
      layout.add_widget(btn) # эта команда делает видимыми сразу две кнопки (пробуйте убрать)
      return layout

MyApp().run()
# вторая кнопка визуально не находится на первой!
# расположением своих потомков управляют только виджеты-макеты (layout)
# остальные виджеты (например, кнопка) не влияют на место и размер своих потомков