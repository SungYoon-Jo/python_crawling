import pandas as pd
# import numpy as np

file = "google.csv"

df = pd.read_csv(file, sep='\t', names=["href"])
# print(df)

# print(df.size)

# for i in df.index:
#     print(df.loc[i])

for i in range(1):
    print(df.loc[i])

# csv 파일의 특정 행 출력 가능




# 과정 페이지에 해당하는 URL을 불러와서 CSV파일로 저장 -> 누리캅스 사이트 접속 -> URL입력 공간에 저장된 CSV 파일 입력 하고 중복체크 -> alert 내용 저장 