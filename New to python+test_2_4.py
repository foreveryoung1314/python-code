#print可以输出字符串
print('Hello World')
print("Hello World")

#可以输出数字
print(520)
print(34.2)

#含有运算符的表达式
print(5+4)

#将数据输出文件中,注意点，1.所指定的盘符存在。2.使用file=fp
fp=open('E:/text.txt','a+')#a+ 如果文件不存在就创建，如果文件存在就在文件内容的后面继续追加
print('hello world',file=fp)
fp.close

#不进行换行输出（输出内容在一行当中）
print('hello',"world",'Python')

print('hello\tworld')
print('hello\nworld')
print('hello\rworld')#world将hello进行了覆盖
print('hello\bworld')#\b 是退一个格
print('http:\\\www.baidu.com')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加r或R
#注意事项，最后一个字符串不能是反斜杠
print(r'hello\nworld')
print(chr(0b100111001011000))  #0b后面跟的是二进制
print(ord('乘'))  #20056是上面二进制对应的十进制

name='王大姐'
print(name)
print('标识',id(name))
print('类型',type(name))
print('数值',name)
