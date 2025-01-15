# python实现一个简单抽奖系统

# 让我们的电脑可以支持服务访问
# 需要一个web框架
# 导入Flask库，Flask是一个用于开发Web应用的框架，在这里，我们使用它来搭建一个简单的Web应用。
# pip install Flask 安装Flask库
from flask import Flask, render_template

# 导入随机数生成器，用来从列表中随机选择一个英雄
from random import randint

# 创建Flask应用实例
app = Flask(__name__)

# 定义一个包含英雄名称的列表，作为抽奖选项
hero = [
    "黑暗之女",
    "狂战士",
    "正义巨像",
    "卡牌大师",
    "德邦总管",
    "无畏战车",
    "诡术妖姬",
    "猩红收割者",
    "远古恐惧",
    "正义天使",
    "无极剑圣",
    "牛头酋长",
    "符文法师",
    "亡灵战神",
    "战争女神",
    "众星之子",
    "迅捷斥候",
    "麦林炮手",
    "祖安怒兽",
    "雪原双子",
    "赏金猎人",
    "寒冰射手",
    "蛮族之王",
    "武器大师",
    "堕落天使",
    "时光守护者",
    "炼金术士",
]

# 创建一个路由'/index'，用来展示页面


@app.route('/index')
def index():
    # 返回一个模板（HTML页面），并将英雄列表传递给页面
    return render_template('index.html', hero=hero)

# 创建一个路由'/choujiang'，用来进行抽奖


@app.route('/choujiang')
def choujiang():
    # 随机生成一个数字，这个数字会对应到hero列表中的一个元素
    num = randint(0, len(hero)-1)
    # 返回模板页面，并将抽奖结果（随机选择的英雄）传递给页面
    return render_template('index.html', hero=hero, result=hero[num])


# 启动Flask开发服务器，开启调试模式
app.run(debug=True)
