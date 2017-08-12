---------------------------------
as
import some as other
print(other.name);
和
import some
other = some
del some
print(other.name)
一样。

----------------------------------
global #在函数里使用全局变量要先使用（global 变量名）；

-----------------------------------
with #他会在程序关闭前自动使用函数的__exit__();
file = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()
和
with open("/tmp/foo.txt")
 as file:
    data = file.read()
他会自动使用file。close();
--------------------------------------
assert #他判断这句话的对错，对继续下一行代码，错就退出
--------------------------------------
yield #有了他函数就像生成器，就像__iter__（）.....next一样
>>> def fun2():  
...     print 'first'  
...     yield 5  
...     print 'second'  
...     yield 23  
...     print 'end...'  
...   
>>> g1 = fun2()  
>>> g1.next()             //第一次运行,暂停在yield 5               
first  
5  
>>> g1.next()             //第二次运行,暂停在yield 23  
second  
23  
>>> g1.next()             //第三次运行,由于之后没有yield,再次next()就会抛出错误  
end...  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
StopIteration  
>>>   
--------------------------------------------------------
except #他要结合try一起使用
import sys
try:
    s = raw_input('Enter something --> ')  #可能得到异常的语句
except EOFError:       #锁定是哪种异常
    print 'ERROR INPUT !'   #出现异常的处理方法
    sys.exit()
print s
--------------------------------------------------------
exec:
注意：python2时exec 是一个语法声明，不是一个函数。也就是说和if,for一样。但在Python3.0中，exec是一个函数而不是语句。
使用exec执行一个字符串：

>>> exec('print("http://coderschool.cn/1735.html")')
http://coderschool.cn/1735.html
>>> a = 2
>>> exec("a=1")
>>> a
1


但是，比如下面这个例子就会报错：
>>> from math import sqrt
>>> exec("sqrt = 1")
>>> sqrt(4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable


上面例子报错是因为变量名和内建函数名相互干扰了，所以，为了安全起见，可以增加一个字典，起到命名空间的作用。命名空间，可以浅显的理解为放置变量的地方。可以用字典起到放置代码字符串命名空间的作用。实例：
>>> a = 2
>>> b = 3
>>> g = {"a":6,"b":3}
>>> a
2
>>> g['a']
6
>>> from math import sqrt
>>> d = {"sqrt":1}
>>> sqrt(4)
2.0
>>> d['sqrt']
1


exec还可以带多个参数，比如：
exec(expr, globals) 其中globals必须是字典


通过带两个参数的形式也可以解决命名冲突，实例：
>>> from math import sqrt
>>> ff = {}
>>> exec("sqrt=1",ff)
>>> sqrt(4)
2.0
>>> ff['sqrt']
1
---------------------------------------------------------
finally #结合try一起使用，当程序报错退出时，先执行finally的代码
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
-----------------------------------------------------------
lambda #g = lambda x:x+1就像def g(x):return x+1
g = lambda x:x+1
g(1)
>>>2
g(2)
>>>3

or

>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>>
>>> print filter(lambda x: x % 3 == 0, foo)
[18, 9, 24, 12, 27]
>>>
>>> print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>>
>>> print reduce(lambda x, y: x + y, foo)
139
----------------------------------------------------------------
