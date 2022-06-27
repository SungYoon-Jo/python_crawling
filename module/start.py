import save
import login
import put

while 1:

    choice = input('목록을 선택해주세요 bye, data, login, put : ')

    if choice == "bye":
        break

    elif choice == "data":
        save.search()

    elif choice == "login":
        login.add()

    elif choice == "put":
        put.urldata()
    