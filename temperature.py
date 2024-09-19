#TODO: 读取weather.json文件，打印出temperature字段下的data数组中每个地点的温度

import json

# 打开并加载json文件
with open('weather.json', 'r') as f:
    data = json.load(f)

# 遍历temperature字段下的data数组
for item in data['temperature']['data']:
    # 打印每个地点的温度
    print(f"地点: {item['place']}, 温度: {item['value']} {item['unit']}")