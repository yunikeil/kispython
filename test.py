import tkinter as tk

class SynchronizedTextFields:
    def __init__(self, master):
        self.master = master
        master.title("Синхронизированные текстовые поля")

        # Создаем два текстовых поля
        self.text1 = tk.Text(master, height=10, width=50)
        self.text2 = tk.Text(master, height=10, width=50)

        # Размещаем текстовые поля на форме
        self.text1.grid(row=0, column=0)
        self.text2.grid(row=0, column=1)

        # Привязываем функции к событию "изменение текста"
        self.text1.bind('<KeyRelease>', self.sync)
        self.text2.bind('<KeyRelease>', self.sync)

    def sync(self, event=None):
        # Получаем текст из первого текстового поля
        text1 = self.text1.get('1.0', 'end-1c')

        # Получаем текст из второго текстового поля
        text2 = self.text2.get('1.0', 'end-1c')

        # Если текст в первом текстовом поле отличается от текста во втором,
        # то заменяем текст во втором текстовом поле на текст из первого
        if text1 != text2:
            self.text2.delete('1.0', 'end')
            self.text2.insert('1.0', text1)

        # Если текст во втором текстовом поле отличается от текста в первом,
        # то заменяем текст в первом текстовом поле на текст из второго
        elif text2 != text1:
            self.text1.delete('1.0', 'end')
            self.text1.insert('1.0', text2)

# Создаем корневое окно
root = tk.Tk()

# Создаем экземпляр класса и запускаем главный цикл
app = SynchronizedTextFields(root)
root.mainloop()
