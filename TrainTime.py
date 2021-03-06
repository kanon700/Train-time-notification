# coding:utf-8
#!/usr/bin/python

import pandas
import re
import datetime

def TrainTimeNotification():
    # 到着予定時刻は現在時間+walktimeの時間
    walktime=15
    arrivaltime = datetime.datetime.now()
    arrivaltime+=datetime.timedelta(minutes=walktime)

    # 駅すぱーとから時刻表を取得する
    url = "https://roote.ekispert.net/ja/timetable/25000/1350"
    fetched_df = pandas.io.html.read_html(url,index_col=0)

    # 0が平日 1が土日祝
    df = fetched_df[0]
    list=[]
    # 時間毎サーチ(1列目)
    for hour, row in df.iterrows():
        mindata = df.at[hour,1]
        mindata = mindata.split()
        # 分毎サーチ(2列目)
        for min in mindata:
            min = re.sub(r'\D', '',min)
            # datetime形式でlistに追加する
            ttime = datetime.datetime.strptime(str(datetime.date.today())+' '+str(hour)+':'+str(min)+':00', '%Y-%m-%d %H:%M:%S')
            list.append(ttime)

    # リストと到着予定時刻から最短で乗れる電車の時刻を取得
    for index, traintime in enumerate(list):
        if arrivaltime < traintime :
            # traintimeは「2018-05-27 23:06:00」の形式のため、splitで時分を切り出す
            traintime = str(traintime).split()
            traintime = str(traintime[1]).split(":")
            if index == 0 :
                notice = "次は始発で"+str(traintime[0])+"時"+str(traintime[1])+"分です"
            else:
                notice = "次に乗れる電車は"+str(traintime[0])+"時"+str(traintime[1])+"分です"
            break
    else:
        notice = "終電にも間に合いません"

    return notice

if __name__ == '__main__':
    TrainTimeNotification()
