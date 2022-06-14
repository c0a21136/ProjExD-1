from random import randint

TARGET_STRING_NUM = 5 # 表示文字数
LOST_STRING_NUM = 3   # 欠損文字数

def main():
    taget_strings = [] # 対象文字を保存するリスト
    for i in range(TARGET_STRING_NUM):
        rand = randint(65,90) # 65(A)~90(Z)の乱数を作成
        taget_strings.append(rand)

    lost_strings = [] # 欠損文字を保存するリスト
    for i in range(LOST_STRING_NUM):
        rand = 0 # 乱数を保存する変数
        while (True):
            rand = randint(65, 90) # 65(A)~90(Z)
            if (rand not in taget_strings):
                break 
        lost_strings.append(rand)

    print("対象文字")
    # 対象文字の表示後、欠損文字の表示
    for i in taget_strings: 
        print("{:3s}".format(chr(i)), end="")
    for i in lost_strings:
        print("{:3s}".format(chr(i)), end="")
    print("")

    print("欠損文字")
    for i in lost_strings:
        print("{:3s}".format(chr(i)), end="")
    print("")

    print("表示文字")
    for i in taget_strings:
        print("{:3s}".format(chr(i)), end="")
    print("")

    n = int(input("欠損文字はいくつあるでしょう?"))
    if n == len(lost_strings):
        print("正解")
        string_ans(lost_strings)
    else:
        print("不正解です。またチャレンジしてください")
        for i in range(30):
            print("-", end="")
        print("")

# 欠損文字の入力を求めて実際の文字と適合しているか確認する関数
def string_ans(lost_strings):
    ansers = []
    # 実際の欠損文字数の分の文字数の入力を求める
    for i in range(LOST_STRING_NUM):
        i = input(f"{i+1}もじめは?")
        ansers.append(ord(i))

    # 欠損文字にヒットする度に1足していく
    status = 0
    for a in ansers:
        if (a in lost_strings):
            status += 1
        else:
            continue

    # 実際に欠損した文字数と入力してヒットした文字数が一致したときに正解を返す
    if (status == LOST_STRING_NUM):
        print("正解!!")
    else:
        print("不正解です。またチャレンジしてください")
        for i in range(30):
            print("-", end="")
        print("")   


if __name__ == "__main__":
    main()
