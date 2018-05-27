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
    walktime= '00:15:00'
    today=datetime.date.today()

    # ttime = datetime.datetime.strptime(test, '%H:%M:%S')
    # print(ttime)

    fetched_df = pandas.io.html.read_html(url,index_col=0)
    df=fetched_df[0]
    list=[]

    for index, row in df.iterrows():
        test=df.at[index,1]
        test = test.split()
        for item in test:
            item=re.sub(r'\D', '',item)
            # print(str(index)+':'+str(item))
            ttime=datetime.datetime.strptime(str(datetime.date.today())+' '+str(index)+':'+str(item)+':00', '%Y-%m-%d %H:%M:%S')
            list.append(ttime)

    # print(list)

    # idx = np.abs((date - np.asarray(list)).argmin())
    # print(np.asarray(list) - date)
    # print(np.abs(date - list[90]).argmin)
    # print(date - list[90])
    # print(date)
    # print(list[90])

    for val in list:
        if (date < val) :
            print(val)
            break


    # 0が平日 1が土日祝
    # timetable =fetched_df[0]
    # test=df.at[5,1]
    # test = test.split()
    # test = [int(s) for s in test]
    # print(getNearestValue(test,30))

    #fetched_df = fetched_df.split(' ')
    #print(df.index.values)
    #print(df.columns.values)

    # print(lists)

    # 0が平日 1が土日祝
    # fetched_df[0].to_csv('output0.csv',index='false', encoding="utf-8")
    # fetched_df[1].to_csv('output1.csv',index='false', encoding="utf-8")
