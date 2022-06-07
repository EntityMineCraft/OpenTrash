#虽然这一目了然，但我还要加注释：以下是导入
import random
import time
#虽然这一目了然，但我还要加注释：以下是变量
MB = random.randint(1,41234)
dMB = random.randint(1,51234)
RT = ['要捡到5kw彩票就好了', '真走运', '卧槽牛逼', '？？？？', 'woc!!!', '卧槽', 'WTF?']
RTS = random.sample(RT, 1)
#虽然这一目了然，但我还要加注释：以下是输出文本
print('Run at',time.asctime())
print('---捡钱模拟器Ver5.2.5(test)---')
print('捡钱模拟器赞助：')
print('开发商：CI工作室')
print('开发者：Entity')
print('语言：python')
print('文本编辑器：VSCode')
print('----------------------')
input('Enter拾钱')
print(time.strftime("*** 在%Y年%m月%d日%H点%M分%S秒那天"))
print('*** 你捡到支票和欠条了! 拿到了',dMB,'支票和',MB,'欠条!')
print('*** 你获得了 钱',dMB-MB)
print(RTS)
input('Enter再捡一次')
MB = random.randint(1,41234)
dMB = random.randint(1,51234)
RTS = random.sample(RT, 1)
print(time.strftime("*** 在%Y年%m月%d日%H点%M分%S秒那天"))
print('*** 你捡到支票和欠条了! 拿到了',dMB,'支票和',MB,'欠条!')
print('*** 你获得了 钱',dMB-MB)
print(RTS)
input('')