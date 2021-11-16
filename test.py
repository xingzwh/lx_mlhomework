# -*- codeing = utf-8 -*-
import pandas as pd

# 将2021年成都空气质量数据作为测试集
df = pd.read_csv('2021年成都空气质量数据.csv')
# 取质量等级  AQI指数  当天AQI排名  PM2.5 。。。8列数据
# SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame 解决方法
df1 = df[['AQI指数', '当天AQI排名', 'PM2.5', 'PM10', 'So2', 'No2', 'Co', 'O3']].copy()

air_quality = []
# print(df['质量等级'].value_counts())
# 质量等级列数据为字符串  转为为标签  便于判断预测
for i in df['质量等级']:
    if i == "优":
        air_quality.append('1')
    elif i == "良":
        air_quality.append('2')
    elif i == "轻度污染":
        air_quality.append('3')
    elif i == "中度污染":
        air_quality.append('4')
    elif i == "重度污染":
        air_quality.append('5')
    elif i == "严重污染":
        air_quality.append('6')

print(air_quality)
df1['空气质量'] = air_quality

# 将数据写入test.txt
# print(df1.values, type(df1.values)) # <class 'numpy.ndarray'>
with open('test.txt', 'w') as f:
    for x in df1.values:
        print(x)
        s = ','.join([str(i) for i in x])
        # print(s, type(s))
        f.write(s + '\n')
