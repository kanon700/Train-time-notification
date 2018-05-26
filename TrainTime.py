import pandas
import re
import datetime
import numpy as np

def getNearestValue(list, num):
    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

if __name__ == "__main__":


    url = "https://roote.ekispert.net/ja/timetable/25000/1350"
    date = datetime.datetime.now()

    fetched_df = pandas.io.html.read_html(url,index_col=0)
    timetable =fetched_df[0]
    #fetched_df = fetched_df.split(' ')
    #print(df.index.values)
    #print(df.columns.values)

    test=df.at[5,1]
    test = test.split()
    test = [int(s) for s in test]

\
    print(getNearestValue(test,30))

    # pattern=r'([0-9]*)'
    # lists=re.findall(pattern,fetched_df)
    # print(lists)


    #fetched_df[0].to_csv('output.csv',index='false', encoding="utf-8")
