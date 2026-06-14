from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
from kivy.core.window import Window
Window.softinput_mode = "below_target"


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(
            orientation="vertical",
            padding=dp(24),
            spacing=dp(16),
        )
        layout.add_widget(MDLabel(
            text="اريد تطبيق بعداد يحسب المده التى أتوقف ف",
            halign="center",
            font_style="H5",
            theme_text_color="Primary",
            size_hint_y=None,
            height=dp(60),
        ))
        self.inp = MDTextField(
            hint_text="اكتب هنا...",
            mode="rectangle",
            size_hint_y=None,
            height=dp(56),
        )
        layout.add_widget(self.inp)
        self.out = MDLabel(
            text="النتيجة ستظهر هنا",
            halign="center",
            theme_text_color="Secondary",
        )
        layout.add_widget(self.out)
        btn = MDRaisedButton(
            text="تنفيذ",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            size=(dp(160), dp(48)),
        )
        btn.bind(on_release=self._run)
        layout.add_widget(btn)
        self.add_widget(layout)

    def _run(self, *_):
        v = self.inp.text.strip()
        self.out.text = f"أدخلت: {v}" if v else "الرجاء إدخال نص"


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"
        self.title = "اريد تطبيق بعداد يحسب المده التى أتوقف ف"
        return MainScreen()


if __name__ == "__main__":
    App().run()
