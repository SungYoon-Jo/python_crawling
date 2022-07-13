# import save
# import login
import indata as ipd

while 1:

    ch = input('목록을 선택해주세요 bye, data, login, inputdata = ipd : ')

    if ch == "bye":
        print("Have a nice day!")
        break

    # elif ch == "data":
    #     save.search()

    # elif ch == "login":
    #     login.add()

    elif ch == "ipd":
        ipd.urldata()

    else:
        print("올바른 명령어를 선택해주세요")