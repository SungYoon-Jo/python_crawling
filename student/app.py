import start as st

while 1:

    ch = input('목록을 선택해주세요 start: st, bye : ')

    if ch == "bye":
        print("Have a nice day!")
        break

    elif ch == "st":
        st.urldata()

    else:
        print("올바른 명령어를 선택해주세요")