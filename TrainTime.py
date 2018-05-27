# coding:utf-8
#!/usr/bin/python

import pandas
import re
import datetime
import subprocess

if __name__ == "__main__":
    # 到着予定時刻は現在時間+walktimeの時間
    walktime=15
    date = datetime.datetime.now()
    date+=datetime.timedelta(minutes=walktime)

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
            # 到着予定時刻と比較するためにdatetime形式でリストに追加する
            ttime=datetime.datetime.strptime(str(datetime.date.today())+' '+str(index)+':'+str(item)+':00', '%Y-%m-%d %H:%M:%S')
            list.append(ttime)

    # リストと到着予定時刻から最短で乗れる電車の時刻を取得
    for index, val in enumerate(list):
        if (date < val) :
            if index == 0 :
                print("次は始発です")
            else:
                # valは「2018-05-27 23:06:00」の形式のため、splitで時分を切り出す
                val=str(val).split()
                val=str(val[1]).split(":")
                print("次に乗れる電車は"+str(val[0])+"時"+str(val[1])+"分です")
            break
    else:
        print("終電にも間に合いません")

    # ↓csvに吐き出したいとき
    # fetched_df[0].to_csv('output0.csv',index='false', encoding="utf-8")
    # fetched_df[1].to_csv('output1.csv',index='false', encoding="utf-8")
