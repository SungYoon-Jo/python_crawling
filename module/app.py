from itertools import chain
import save
import login
import put

while 1:

    ch = input('목록을 선택해주세요 bye, data, login, input : ')

    if ch == "bye":
        print("goodday")
        break

    elif ch == "data":
        save.search()

    elif ch == "login":
        login.add()

    elif ch == "input":
        put.urldata()
    