name = input("hello word")
print(name)
print(5 // 2)
print(ord('a'))
print(chr(99))
print(len("中文"))
print("中文".replace("中","郑"))
print("hi %s"%("zmy",))
print("hi %s, your age is %d ,your moeny is %d "%("zmy",33,44))
print("hi %s, your age is %d ,your moeny is %f "%("zmy",33,44.6666))
print("hi %s, your age is %d ,your moeny is %2f "%("zmy",33,44.6666))
print("hi %s, your age is %d ,your moeny is %.2f "%("zmy",33,44.6666))
d ={"name": "郑明玉", "age": 24}
print(d)
d [" xong "] ="zmy"
print(d)

#====判断语句======

c =18
if c<10:
    print("续航三")
elif c>=10 and c<20:
    print("少年")
elif c>18 and c<30:
    print("青年")
else:
    print("老年")

    # ====循环语句======
    for i in d :
        print(i)

girl_str = "loveYou"

for everyChar in girl_str:
    print(everyChar)

#========while循环========
i = 0
while i <= 2:
    name = input('用户名:')
    passwd = input('密码:')
    if ((name == 'root') and (passwd == 'westos')):
        print('登陆成功')
        break
    else:
        print('登陆失败')
        print('您还有%d次机会' %(2-i))
        i = i + 1
else:
    print('失败超过三次，请稍后再试')


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("张三")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

width = 4
height = 5
area = 20


