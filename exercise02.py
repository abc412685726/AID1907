# 经理：曹操 刘备 孙权
# 技术：曹操 刘备 关羽 张飞
# 是经理也是技术的有谁？
# 是经理不是技术的有谁？
# 不是经理是技术的有谁？
# 张飞是经理么？
# 总共有多少人？
# 身兼一职有多少人？


#字典 内嵌一个集合
dict01={'经理':{'曹操','刘备','孙权'},'技术':{'曹操','刘备','关羽','张飞'}}
set01=dict01['经理']
set02=dict01['技术']
# 是经理也是技术的有谁？
print(set01&set02)#     dict01['经理']&dict01['技术']
# 是经理不是技术的有谁？
print(set01-set02)
# 不是经理是技术的有谁？
print(set02-set01)
# 张飞是经理么？
print('张飞' in set01)
# 总共有多少人？
set03=set01|set02
print(len(set03))
# 身兼一职有多少人？
set03=set01^set02
print(len(set03))