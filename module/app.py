import save
import login
import put

while True:

    choice = input('목록을 선택해주세요 bye, take, login, input : ')

    if choice == "bye" or "BYE":
        break

    elif choice == "take":
        save.search()

    elif choice == "login":
        login.add()

    elif choice == "input":
        put.urldata()
    