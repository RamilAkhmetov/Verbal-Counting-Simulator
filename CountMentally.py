import tkinter as tk
#import time
import random
#import winsound
#import os
#import threading

base_font = ("Arial", 12)
light_green = "#C4F4CE"
salmon = "#FA8072"

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
        #trainerMenu.add_command(label="Мои рекорды", command=self.showRecords)
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

        #tk.Label(master=labels_frame, text="Время (в секундах)", font=base_font).grid(
            #row=1, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        #time_entry = tk.Entry(master=entries_frame)
        #time_entry.grid(row=1, column=0, sticky="w", padx=(5, 0), pady=(10, 0))
        second_row = tk.Frame(master=self.master)
        second_row.pack(pady=(50, 0))
        checkVar1 = tk.IntVar()
        checkVar2 = tk.IntVar()
        checkVar3 = tk.IntVar()
        checkVar1.set(0)
        checkVar2.set(0)
        checkVar3.set(0)
        single = tk.Checkbutton(master=second_row, variable=checkVar1, text="Однозначные", font=base_font)
        double = tk.Checkbutton(master=second_row, variable=checkVar2, text="Двузначные", font=base_font)
        triple = tk.Checkbutton(master=second_row, variable=checkVar3, text="Трехзначные", font=base_font)
        single.grid(row=0, column=0)
        double.grid(row=0, column=1)
        triple.grid(row=0, column=2)
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
        add = tk.Checkbutton(master=third_row, variable=checkVar4, text="Сложение", font=base_font)
        add.grid(row=0, column=0, sticky="w", padx=(5, 0))
        deduct = tk.Checkbutton(master=third_row, variable=checkVar5, text="Вычитание", font=base_font)
        deduct.grid(row=0, column=1, sticky="w", padx=(5, 0))
        tk.Button(master=buttons_frame, font=base_font, text="Начать",
                  command=lambda: self.startTest(int(count_entry.get()), 0,
                  checkVar1.get(), checkVar2.get(), checkVar3.get(), checkVar4.get(), checkVar5.get()),
                  bg="light green").grid(
            row=0, column=2, sticky="w", padx=(0, 60), pady=(10, 0))

    def startTest(self, count_q, tim, n1, n2, n3, ad, ded):
        App.clear_frame(self.master)

        test = Test(self.master, count_q, tim, n1, n2, n3, ad, ded)
        self.destroy()

class Test(tk.Frame):
    def __init__(self, master=None, count_q=10, tim=60, n1=1, n2=1, n3=1, ad=1, ded=1):
        super().__init__(master)
        self.master = master
        self.task_frame = tk.Frame(master=self.master)
        self.task_frame.pack()
        self.first_row= None
        self.count_q = count_q
        self.tim = tim
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.ad = ad
        self.ded = ded
        self.bt = None
        self.bt1 = None
        self.bt2 = None
        self.bt3 = None
        self.current = 1
        self.numbers = []
        self.results = []
        self.timer_thread = None
        self.initUI()

    def initUI(self):
        self.first_row = tk.Frame(master=self.master)
        self.first_row.pack(pady=(50, 0))

        stop_button = tk.Button(master=self.first_row, text="Завершить", font=base_font, bg=salmon)
        stop_button.bind("<Button-1>", self.stopTest)
        stop_button.grid(row=0, column=1, padx=(50, 0))
        if self.n1 == 1:
            self.numbers.extend(list(range(1, 10)))
        if self.n2 == 1:
            self.numbers.extend(list(range(11, 100)))
        if self.n3 == 1:
            self.numbers.extend(list(range(101, 1000)))
        self.generate_task()
        #self.timer_thread = threading.Thread(target=self.timer, args=(self.tim, first_row), daemon=True)
        #self.timer_thread.start()

    def generate_task(self):
        tk.Label(master=self.first_row, text=f"Вопрос №{self.current}. Всего: {self.count_q}", font=base_font).grid(
            row=0, column=0, sticky="w")
        if self.current > self.count_q:
            App.clear_frame(self.master)
            self.showResult()
            return
        second_row = tk.Frame(master=self.task_frame)
        second_row.pack(pady=(50, 0))
        random.seed()

        int1 = random.choice(self.numbers)
        int2 = random.choice(self.numbers)



        rn = random.randint(0, 1)

        result = (int1 - int2) if rn == 0 else (int1 + int2)
        result3 = result + (-1) ** random.randint(1, 2) * 10
        while result3 == result:
            result3 = result + (-1) ** random.randint(1, 2) * 10
        result1 = random.choice(self.numbers)
        while result1 == result3 or result1 == result:
            result1 = random.choice(self.numbers)
        result2 = random.choice(self.numbers)
        while result2 == result1 or result2 == result3 or result2 == result:
            result2 = random.choice(self.numbers)

        task = f"{int1}+{int2}=?" if rn == 1 else f"{int1}-{int2}=?"
        tk.Label(master=second_row, font=("Arial", 25, "bold"), text=task).pack()
        third_row = tk.Frame(master=self.task_frame)
        third_row.pack(pady=(50, 0))
        self.bt = tk.Button(master=third_row, text=str(result), font=base_font, command=self.correct_answer_clicked)
        self.bt1 = tk.Button(master=third_row, text=str(result1), font=base_font, command=lambda: self.bad_answer_clicked(1))
        self.bt2 = tk.Button(master=third_row, text=str(result2), font=base_font, command=lambda: self.bad_answer_clicked(2))
        self.bt3 = tk.Button(master=third_row, text=str(result3), font=base_font, command=lambda: self.bad_answer_clicked(3))
        lst = list(range(4))
        rnd = random.choice(lst)
        self.bt.grid(row=0, column=rnd)
        lst.remove(rnd)
        rnd = random.choice(lst)
        self.bt1.grid(row=0, column=rnd)
        lst.remove(rnd)
        rnd = random.choice(lst)
        self.bt2.grid(row=0, column=rnd)
        lst.remove(rnd)
        rnd = random.choice(lst)
        self.bt3.grid(row=0, column=rnd)
        lst.remove(rnd)


    def correct_answer_clicked(self):

        #if "sounds" in os.listdir():
            #if "correct_answer.mp3" in os.listdir("sounds"):
                #pass
                #winsound.PlaySound("sounds/correct_answer.mp3", winsound.SND_FILENAME)
        self.results.append(1)
        self.bt.config(bg=light_green)
        self.go_next()

    def bad_answer_clicked(self, n):

        #if "sounds" in os.listdir():
            #if "bad_answer.mp3" in os.listdir("sounds"):
                #pass
                #winsound.PlaySound("sounds/bad_answer.mp3", winsound.SND_FILENAME)
        self.results.append(0)
        self.bt.config(bg=light_green)
        if n == 1:
            self.bt1.config(bg=salmon)
        elif n == 2:
            self.bt2.config(bg=salmon)
        elif n == 3:
            self.bt3.config(bg=salmon)
        self.go_next()


    # def timer(self, n, first_row):
    #     lb = tk.Label(master=self, text=time.time(), font=base_font)
    #     lb.grid(row=4, column=2)
    #     start = time.time()
    #     while (time.time() - start) < n:
    #         lb.config(text=str(int(time.time()-start)))
    #     App.clear_frame(self.master)
    #     self.showResult()



    def showResult(self):

        count_correct = 0
        for i in range(len(self.results)):
            if self.results[i] == 1:
                count_correct += 1
        fr = tk.Frame(master=self.master)
        fr.pack()
        tk.Label(master=fr, font=("Arial", 25, "bold"), text=f"Ваш результат: {count_correct} из {self.count_q}").pack(
            pady=(50, 0)
        )


    def stopTest(self, event):
        App.clear_frame(self.master)
        self.showResult()
        #self.timer_thread.paused = True
        #self.timer_thread = None
        #newtest = NewTest(self.master)
        #self.destroy()


    def go_next(self):
        self.current += 1
        print(self.current)
        App.clear_frame(self.task_frame)
        self.generate_task()




def main():
    root = tk.Tk()
    root.geometry("600x600")
    root.title("CountMentally")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()