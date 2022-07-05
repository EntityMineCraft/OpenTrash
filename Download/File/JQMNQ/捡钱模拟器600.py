#The file by CI Studio™
#作者：Entity
#成员：任之炼
#答疑：FFS、Ninecloud、高木同学...
#灵感来源于MMORPG的捡钱机制
import random
import time
import socket
class tc:
    rel = '\033[0m'
    yel = '\033[93m'
    blu = '\033[94m'
    red = '\033[91m'
MB = random.randint(0,922337)
gMB = random.randint(0,2147483)
M = gMB-MB
RT = ['要捡到5kw彩票就好了','卧槽牛逼','？？？？','woc!!!','卧槽','WTF?']
RTS = random.sample(RT, 1)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(tc.red,'WLANIP=',s.getsockname()[0])
print('Run at',time.asctime(),tc.rel)
print('---捡钱模拟器Ver6.0.0(Bate)---')
print('捡钱模拟器赞助：')
print('开发商：CI工作室')
print('开发者：Entity')
print('语言：python')
print('文本编辑器：VSCode、QPython、')
print('CEdit（kolibriOS）、notepad')
print('野生猿类优(劣)秀(质)产物')
print('更新:5.9.1版本')
print('----------------------')
input(tc.yel+ 'Enter拾钱')
print(time.strftime("*** 在%Y年%m月%d日%H点%M分%S秒那天"))
print('*** 你捡到支票和欠条了! 拿到了',gMB,'支票和',MB,'欠条!')
print('*** 你获得了 钱',gMB-MB,tc.rel)
print(RTS)
TorF = random.randint(0,1)
badtime = random.randint(3,7)
if M >= 100000:
    print(tc.red+ '你进了监狱，因为你私吞巨款',tc.rel)
    input(tc.blu+ '警察：说说吧，你有什么感想'+tc.rel)
    if TorF == 0:
        print('你被假释了')
        print('你和你的plmm过上了没羞没噪的生活')
        print('ah that’s♂good')
    else:
        print('你被判了',badtime,'年的有期徒刑')
else:
    if M >= 1:
        print('你把',gMB-MB,'存进了银行卡')
        print('你的小♂日子过得挺不错')
    else:
        print(tc.red+'Mother的哪个二臂'+tc.rel)
input('')
