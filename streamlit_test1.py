import json
import matplotlib.pyplot as plt
import streamlit as st


# 打开并加载json文件
with open('weather.json', 'r') as f:
    data = json.load(f)


# 提取地点和温度数据
places = [item['place'] for item in data['temperature']['data']]
temperatures = [item['value'] for item in data['temperature']['data']]

#分列准备
col1, col2 = st.columns([1, 3])

# 创建选择框
place_selected = col1.selectbox('select a place：', places)

# 找到选择的地点的温度
temperature_selected = temperatures[places.index(place_selected)]


# 展示选择的地点和温度
col2.write(f"Location：{place_selected}")
col2.write(f"Temperature：{temperature_selected}")

# 创建柱状图
bars = plt.bar(places, temperatures)
plt.xlabel('Place')
plt.ylabel('Temperature')
plt.title('Temperature of all places')

# 高亮选择的地点
for bar, place in zip(bars, places):
    if place == place_selected:
        bar.set_color('r')
    else:
        bar.set_color('b')

# 旋转x轴的标签
plt.xticks(rotation=90)

# 在Streamlit页面中显示柱状图
col2.pyplot(plt)