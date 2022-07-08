

db = ["youtube","twitter","facebook","tistory","tumblr"]

db2 = [
    "https://www.youtube.com", "https://youandjunmoney.org", 
    "https://stellanwamp.com", "https://pmang-hd.tumblr.com",
     "https://7wr73rj7j7.tistory.com", "https://play-pokers.com",
      "https://daebbangmoney.com"]


for i in range(len(db2)):
    for y in range(len(db)):
        if db[y] in db2[i]:
            print(db2[i])