import tkinter as tk
import pygame
import random

class RussianRouletteGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Русская рулетка")

        # Установка иконки
        self.master.iconbitmap("your_icon.ico")

        self.canvas = tk.Canvas(self.master, width=300, height=200)
        self.canvas.pack()

        self.button_spin = tk.Button(self.master, text="Прокрутить", command=self.spin_chamber)
        self.button_spin.pack(pady=10)

        self.sound_shot = pygame.mixer.Sound("shot.wav")
        self.sound_empty = pygame.mixer.Sound("empty.wav")

        self.bullet_position = random.randint(1, 2)
        self.text_id = None  # Идентификатор текста для последующего удаления

    def spin_chamber(self):
        # Удаляем предыдущий текст, если он существует
        if self.text_id:
            self.canvas.delete(self.text_id)

        result = random.randint(1, 2)
        if result == self.bullet_position:
            self.text_id = self.canvas.create_text(150, 100, text="Выстрел!", font=("Helvetica", 16), fill="red")
            self.play_sound(self.sound_shot)
        else:
            self.text_id = self.canvas.create_text(150, 100, text="Патрон пропущен", font=("Helvetica", 16), fill="green")
            self.play_sound(self.sound_empty)

    def play_sound(self, sound):
        pygame.mixer.Sound.play(sound)

def main():
    root = tk.Tk()
    game = RussianRouletteGame(root)
    root.mainloop()

if __name__ == "__main__":
    pygame.mixer.init()  # Инициализация звука
    main()
