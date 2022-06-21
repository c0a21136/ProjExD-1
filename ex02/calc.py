# tkinterのモジュールをインポートする
from itertools import count
import tkinter as tk
import tkinter.messagebox as tkm


def main():
    
    # ボタン以外を入力したときの動作
    def button_click(event):
        btn = event.widget
        txt = btn["text"]
        if txt == "+":
            entry.insert(tk.END, "+")
        elif txt == "=":
            formula = entry.get()
            result = eval(formula)
            entry.delete(0, tk.END)
            entry.insert(tk.END, int(result))
        else:
            entry.insert(tk.END, int(txt))
    

    # tkクラスからアプリの基本となるインスタンスを作成
    root = tk.Tk()
    root.title("計算機")
    root.geometry("300x600")

    # 数字を表示する画面を作成する
    entry = tk.Entry(justify="right",
                    width=10,
                    font=("Times New Roman",40)
                    )
    entry.grid(row=0, column=0, columnspan=3)
    
    # 数字のボタンを9~0まで作成する
    r = 1
    c = 0
    for i in range(9, -1, -1):
        button = tk.Button(root,
                        width=4,
                        height=2,
                        text=i,
                        font=("Times New Roman", 30)
                        )
        if (i%3==0):
            r += 1
            c = 0
        else:
            c += 1
        button.grid(row=r, column=c)
        button.bind("<1>", button_click)
    
    # プラスボタンを作成する
    plus_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="+",
                        font=("Times New Roman", 30)
                        )
    plus_button.grid(row=5, column=1)
    plus_button.bind("<1>", button_click)

    equal_button = tk.Button(root,
                        width=4,
                        height=2,
                        text="=",
                        font=("Times New Roman", 30)
                        )
    equal_button.grid(row=5, column=2)
    equal_button.bind("<1>", button_click)

    root.mainloop()


if __name__ == "__main__":
    main()