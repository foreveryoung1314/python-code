#数据类型
#int
n1=90
n2=-70
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示成二进制，十进制，八进制，十六进制
print('十进制',189)
print('二进制',0b1011011)
print('八进制',0o176)
print('十六进制',0x1EAF)

#float

m1=1.1
m2=2.2
m3=2.3
print(m1+m2)
print(m1+m3)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#bool
#布尔值可以转成整数计算
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
print(f1+1) #布尔值可以转成整数计算 1+1=2
print(f2+1)

#str
str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
str3="""人生苦短，
我用Python"""
str4='''人生苦短,
我用Python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3)
print(str4)

#数据类型转换
name='张三'
age=20
print('我叫'+name+'，今年'+str(age)+'岁')
