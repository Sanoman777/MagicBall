import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class MagicBallApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Виджет для отображения ответа
        self.answer_label = Label(text='Задайте вопрос и нажмите на кнопку "Предсказать".')
        layout.add_widget(self.answer_label)

        # Кнопка для предсказания
        predict_button = Button(text='Предсказать', on_release=self.predict)
        layout.add_widget(predict_button)

        return layout

    def predict(self, instance):
        answers = [
            "Бесспорно",
            "Предрешено",
            "Никаких сомнений",
            "Определённо да",
            "Можешь быть уверен в этом",
            "Мне кажется — да",
            "Вероятнее всего",
            "Хорошие перспективы",
            "Знаки говорят — да",
            "Да",
            "Пока не ясно, попробуй снова",
            "Спроси позже",
            "Лучше не рассказывать",
            "Сейчас нельзя предсказать",
            "Сконцентрируйся и спроси опять",
            "Даже не думай",
            "Мой ответ — нет",
            "По моим данным — нет",
            "Перспективы не очень хорошие",
            "Весьма сомнительно"
        ]

        # Генерация случайного ответа
        answer = random.choice(answers)
        self.answer_label.text = answer

if __name__ == '__main__':
    MagicBallApp().run()
