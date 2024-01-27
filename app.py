import math
from datetime import datetime
import random

from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/datetime")
def hello():
    # 第 一 題
    date = datetime.now()
    return render_template("datetime.html", date=date)


# 第 二 題
@app.route("/quotes")
def quotes():
    with open("quotes.txt") as f:
        random_quotes = random.choice(f.readlines())
    return random_quotes


# quotes = ["If you want to achieve greatness stop asking for permission. ~Anonymous",
#           "Things work out best for those who make the best of how things work out. ~John Wooden",
#           "To live a creative life, we must lose our fear of being wrong. ~Anonymous",
#           "If you are not willing to risk the usual you will have to settle for the ordinary. ~Jim Rohn",
#           "Trust because you are willing to accept the risk, not because it's safe or certain. ~Anonymous",
#           "Take up one idea. Make that one idea your life - think of it, dream of it, live on that idea. Let the brain, muscles, nerves, every part of your body, be full of that idea, and just leave every other idea alone. This is the way to success. ~Swami Vivekananda",
#           "All our dreams can come true if we have the courage to pursue them. ~Walt Disney"]
# random_quotes = random.choice(quotes)
# return random_quotes

# @app.route("/<int:number>")
# def hello(number):
#     # 第 三 題
#     list = []
#     for i in range(2, number + 1): #
#         if number % i == 0:  # 先確認 i 是否是 number 的因數
#             is_prime = True  # 假設 i 是質數
#             for j in range(2, int(i**0.5) + 1):  # 確認裡面的因數 是質數 ，# 確認質數的關係就是 這個質數開根號之後 的前面數值(2 ~ 開根號之後的數值) 就知道他是不是質數，參考https://en.wikipedia.org/wiki/Primality_test
#                                        # 假如 number =  15 ，i = 3 , 3開根號是 1.7
#                 if i % j == 0:  # 3 取 j 的餘數 != 0，代表 3 是 質數
#                     is_prime = False  # 如果這個質數的因數 可以被其他數整除，代表 他 不是 質數
#                     break
#             if is_prime == True:
#                 list.append(i)
#                 # print((2**3))
#     return "the number {} has a lot of 因數，其中是質數的有 {}".format(number , list)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/request")
def request_1():
    person = {"user": "Jimmy",
              "password": "123456"
              }
    return render_template("request.html", person=person)


# with app.open_resource('quotes.txt') as file:
#     app.global_quotes = [line.rstrip() for line in file]
#     print(app.global_quotes) # [b'hi i am jimmy'] 跑出這個出來代表是因為文件內容被視為二進制數據，所以它讀取的文本被表示為字節串（bytes）

# restrip() 會刪除後面的預設尾隨字元。


@app.route("/header")
def header():
    with open("en-abbreviation.txt") as file:
        l = []
        count = 0
        count1 = 0
        read_Line = file.readlines()
        for i in range(len(read_Line)):
            if read_Line[i][0] == "#":
                count += 1
                continue
            else:
                for j in range(count, len(read_Line)):
                    # 'abbr.\t abbreviation\n', 'AWOL\t absent without le' ...
                    read_t = read_Line[j].replace("\n", "")  # 因為 \t 前面是縮寫，後面是全寫，所以先將全寫後面的 \n 給變成空白
                    print(read_t)
                    read_Strip = read_t.split("\t")  # 再根據 \t 將它們一個個地變成 list
                    print(read_Strip)
                    count1 += 1
                    l.append(read_Strip)
                    if count1 == 10:
                        break
                return l

                # print(read_Line[j].strip("\n\t"))


@app.route("/search")
def search():
    return render_template("input.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        count = 0
        l = []
        user_input = request.form["userInput"]
        # print(user_input)
        with open("en-abbreviation.txt", 'r') as file:
            file_ReadLines = file.readlines()
            for i in range(len(file_ReadLines)):
                # if file_ReadLines[i].count(user_input) > 0:
                #     return f"HI, {file_ReadLines[i]}"
                    if file_ReadLines[i].startswith(user_input):
                        count += 1
                        l.append(file_ReadLines[i].replace("\n", "").replace("\t", ""))
                        continue
                    if len(l) >= 10:
                        return f"HI, {l}"
            return f"HI, {l}"

    else:
        return "WTF ? GET OUT"
