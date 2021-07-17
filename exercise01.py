# 在控制台循环输入字符串
# 如果输入空字符串 停止
# 打印所有不重复的字符串
set01=set()
while True:
    a=input('请输入字符串')
    if a=='':
        break
    else:
        set01.add(a)
for i in set01:
    print(i)
