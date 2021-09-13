import tkinter as tk
import time

base_font = ("Arial", 12)
light_green = "#C4F4CE"


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(master=self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.initUI()

    def initUI(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        trainerMenu = tk.Menu(menubar)
        trainerMenu.add_command(label="Новый тест", command=self.newTest)
        trainerMenu.add_command(label="Мои рекорды", command=self.showRecords)
        menubar.add_cascade(label="Тренажер", menu=trainerMenu)

    def newTest(self):
        App.clear_frame(self.frame)
        newtest = NewTest(self.frame)

    def showRecords(self):
        pass


    @staticmethod
    def clear_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

class NewTest(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()

    def initUI(self):
        first_row = tk.Frame(master=self.master)
        first_row.pack(fill=tk.X)
        labels_frame = tk.Frame(master=first_row)
        labels_frame.pack(side=tk.LEFT)
        entries_frame = tk.Frame(master=first_row)
        entries_frame.pack(side=tk.LEFT)
        buttons_frame = tk.Frame(master=first_row)
        buttons_frame.pack(side=tk.RIGHT)
        tk.Label(master=labels_frame, text="Количество примеров", font=base_font).grid(
                 row=0, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        count_entry = tk.Entry(master=entries_frame)
        count_entry.grid(row=0, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        tk.Button(master=buttons_frame, font=base_font, text="Начать", command=self.startTest, bg="light green").grid(
                  row=0, column=2, sticky="w", padx=(0, 60), pady=(10, 0))
        tk.Label(master=labels_frame, text="Время (в секундах)", font=base_font).grid(
            row=1, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        time_entry = tk.Entry(master=entries_frame)
        time_entry.grid(row=1, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        second_row = tk.Frame(master=self.master)
        second_row.pack()
        checkVar1 = tk.IntVar()
        checkVar2 = tk.IntVar()
        checkVar3 = tk.IntVar()
        checkVar1.set(0)
        checkVar2.set(0)
        checkVar3.set(0)
        single = tk.Checkbutton(master=second_row, variable=checkVar1, text="Однозначные", font=base_font)
        double = tk.Checkbutton(master=second_row, variable=checkVar2, text="Двузначные", font=base_font)
        triple = tk.Checkbutton(master=second_row, variable=checkVar3, text="Трехзначные", font=base_font)
        third_row = tk.Frame(master=self.master)
        third_row.pack(pady=(50, 0))
        checkVar4 = tk.IntVar()
        checkVar5 = tk.IntVar()
        checkVar6 = tk.IntVar()
        checkVar7 = tk.IntVar()
        checkVar4.set(0)
        checkVar5.set(0)
        checkVar6.set(0)
        checkVar7.set(0)
        multiply = tk.Checkbutton(master=third_row, variable=checkVar4, text="Умножение", font=base_font)
        multiply.grid(row=0, column=0, sticky="w", padx=(5, 0))

    def startTest(self):
        pass


def main():
    root = tk.Tk()
    root.geometry("600x600")
    root.title("CountMentally")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()