import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


class Display(App):
    lbl = None
    _i = 0

    def Clock_Callback(self, dt):
        self._i += 1
        self.lbl.text = str(self._i)

    def build(self):
        self.box = BoxLayout(orientation='horizontal', spacing=20)
        self.lbl = Label(
            text='0°F',
            font_size='150'
        )

        self.box.add_widget(self.lbl)

        # Clock.schedule_interval(self.Clock_Callback, 1)

        return self.box
