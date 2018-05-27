import pandas
import re
import datetime
import numpy as np

def getNearestValue(list, num):
    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

if __name__ == "__main__":
    # 到着予定時刻は現在時間+walktimeの時間
    walktime=15
    date = datetime.datetime.now()
    date+=datetime.timedelta(minutes=walktime)
    today=datetime.date.today()

    # 駅すぱーとから時刻表を取得する
    url = "https://roote.ekispert.net/ja/timetable/25000/1350"
    fetched_df = pandas.io.html.read_html(url,index_col=0)

    # 0が平日 1が土日祝
    df=fetched_df[0]
    # 取得した時刻をdatetime形式でlist化する
    list=[]
    for index, row in df.iterrows():
        test=df.at[index,1]
        test = test.split()
        for item in test:
            item=re.sub(r'\D', '',item)
            ttime=datetime.datetime.strptime(str(datetime.date.today())+' '+str(index)+':'+str(item)+':00', '%Y-%m-%d %H:%M:%S')
            list.append(ttime)

    # リストと到着予定時刻から最短で乗れる電車の時刻を取得
    for val in list:
        if (date < val) :
            print(val)
            break

    # 0が平日 1が土日祝
    # fetched_df[0].to_csv('output0.csv',index='false', encoding="utf-8")
    # fetched_df[1].to_csv('output1.csv',index='false', encoding="utf-8")
