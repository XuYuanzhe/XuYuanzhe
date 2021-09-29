# Python Interview 面试相关 基础

▍1、什么是Python？为什么它会如此流行？

Python是一种解释的、高级的、通用的编程语言。

Python的设计理念是通过使用必要的空格与空行，增强代码的可读性。

它之所以受欢迎，就是因为它具有简单易用的语法。

▍2、为什么Python执行速度慢，我们如何改进它？

Python代码执行缓慢的原因，是因为它是一种解释型语言。它的代码在运行时进行解释，而不是编译为本地语言。

为了提高Python代码的速度，我们可以使用CPython、Numba，或者我们也可以对代码进行一些修改。

1. 减少内存占用。
2. 使用内置函数和库。
3. 将计算移到循环外。
4. 保持小的代码库。
5. 避免不必要的循环


▍3、Python有什么特点？

1. 易于编码
2. 免费和开源语言
3. 高级语言
4. 易于调试
5. OOPS支持
6. 大量的标准库和第三方模块
7. 可扩展性(我们可以用C或C++编写Python代码)
8. 用户友好的数据结构


▍4、Python有哪些应用？

1. Web开发
2. 桌面GUI开发
3. 人工智能和机器学习
4. 软件开发
5. 业务应用程序开发
6. 基于控制台的应用程序
7. 软件测试
8. Web自动化
9. 基于音频或视频的应用程序
10. 图像处理应用程序


▍5、Python的局限性？
1. 速度
2. 移动开发
3. 内存消耗(与其他语言相比非常高)
4. 两个版本的不兼容(2，3)
5. 运行错误(需要更多测试，并且错误仅在运行时显示)
6. 简单性


▍6、Python代码是如何执行的？

首先，解释器读取Python代码并检查是否有语法或格式错误。

如果发现错误，则暂停执行。如果没有发现错误，则解释器会将Python代码转换为等效形式或字节代码。

然后将字节码发送到Python虚拟机(PVM)，这里Python代码将被执行，如果发现任何错误，则暂停执行，否则结果将显示在输出窗口中。

图片


▍7、如何在Python中管理内存？

Python内存由Python的私有headspace管理。

所有的Python对象和数据结构都位于一个私有堆中。私用堆的分配由Python内存管理器负责。

Python还内置了一个的垃圾收集器，可以回收未使用的内存并释放内存，使其可用于headspace。


▍8、解释Python的内置数据结构？
Python中主要有四种类型的数据结构。 

列表：列表是从整数到字符串甚至另一个列表的异构数据项的集合。列表是可变的。列表完成了其他语言中大多数集合数据结构的工作。列表在[ ]方括号中定义。
例如：a = [1,2,3,4]

集合：集合是唯一元素的无序集合。集合运算如联合|，交集&和差异，可以应用于集合。{}用于表示一个集合。
例如：a = {1,2,3,4}

元组：Python元组的工作方式与Python列表完全相同，只是它们是不可变的。()用于定义元组。
例如：a =（1,2,3,4）

字典：字典是键值对的集合。它类似于其他语言中的hash map。在字典里，键是唯一且不可变的对象。
例如：a = {'number'：[1,2,3,4]}


▍9、解释//、％、* *运算符？

//(Floor Division)-这是一个除法运算符，它返回除法的整数部分。
例如：5 // 2 = 2

％(模数)-返回除法的余数。
例如：5 ％ 2 = 1

**(幂)-它对运算符执行指数计算。a ** b表示a的b次方。
例如：5 ** 2 = 25、5 ** 3 = 125


▍10、Python中的单引号和双引号有什么区别？

在Python中使用单引号(' ')或双引号(" ")是没有区别的，都可以用来表示一个字符串。

这两种通用的表达方式，除了可以简化程序员的开发，避免出错之外，还有一种好处，就是可以减少转义字符的使用，使程序看起来更简洁，更清晰。


▍11、Python中append，insert和extend的区别?

append：在列表末尾添加新元素。
insert：在列表的特定位置添加元素。
extend：通过添加新列表来扩展列表。

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
>[1,2,3,4,5,6]

## insert(position,value)
numbers.insert(2,7)  
print(numbers)
>[1,2,7,3,4,5,6]

numbers.extend([7,8,9])
print(numbers)
>[1,2,7,3,4,5,6,7,8,9]

numbers.append([4,5])
>[1,2,7,3,4,5,6,7,8,9,[4,5]]


▍12、break、continue、pass是什么？

break：在满足条件时，它将导致程序退出循环。
continue：将返回到循环的开头，它使程序在当前循环迭代中的跳过所有剩余语句。
pass：使程序传递所有剩余语句而不执行。


▍13、区分Python中的remove，del和pop？

remove：将删除列表中的第一个匹配值，它以值作为参数。
del：使用索引删除元素，它不返回任何值。
pop：将删除列表中顶部的元素，并返回列表的顶部元素。

numbers = [1,2,3,4,5]
numbers.remove(5)
> [1,2,3,4]

del numbers[0]
>[2,3,4]

numbers.pop()
>4


▍14、什么是switch语句。如何在Python中创建switch语句？

switch语句是实现多分支选择功能，根据列表值测试变量。

switch语句中的每个值都被称为一个case。

在Python中，没有内置switch函数，但是我们可以创建一个自定义的switch语句。

switcher = {
   1: "January",
   2: "February",
   3: "March",
   4: "April",
   5: "May",
   6: "June",
   7: "July",
   8: "August",
   9: "September",
   10: "October",
   11: "November",
   12: "December"
}
month = int(input())
print(switcher.get(month))

> 3
march


▍15、举例说明Python中的range函数?

range：range函数返回从起点到终点的一系列序列。
range(start, end, step)，第三个参数是用于定义范围内的步数。

# number
for i in range(5):
    print(i)
> 0,1,2,3,4

# (start, end)
for i in range(1, 5):
    print(i)
> 1,2,3,4

# (start, end, step)
for i in range(0, 5, 2):
    print(i)
>0,2,4


▍16、==和is的区别是？

==比较两个对象或值的相等性。
is运算符用于检查两个对象是否属于同一内存对象。

lst1 = [1,2,3]
lst2 = [1,2,3]

lst1 == lst2
>True

lst1 is lst2
>False


▍17、如何更改列表的数据类型？

要将列表的数据类型进行更改，可以使用tuple()或者set()。

lst = [1,2,3,4,2]

# 更改为集合
set(lst)    ## {1,2,3,4}
# 更改为元组
tuple(lst)  ## (1,2,3,4,2)


▍18、Python中注释代码的方法有哪些？

在Python中，我们可以通过下面两种方式进行注释。

1. 三引号'''，用于多行注释。
2. 单井号#，用于单行注释。


▍19、!=和is not运算符的区别？

!=如果两个变量或对象的值不相等，则返回true。
is not是用来检查两个对象是否属于同一内存对象。

lst1 = [1,2,3,4]
lst2 = [1,2,3,4]

lst1 != lst2
>False

lst1 is not lst2
>True


▍20、Python是否有main函数？

是的，它有的。只要我们运行Python脚本，它就会自动执行。


▍21、什么是lambda函数？

Lambda函数是不带名称的单行函数，可以具有n个参数，但只能有一个表达式。也称为匿名函数。

a = lambda x, y：x + y 
print(a(5, 6))

> 11


▍22、iterables和iterators之间的区别？

iterable：可迭代是一个对象，可以对其进行迭代。在可迭代的情况下，整个数据一次存储在内存中。

iterators：迭代器是用来在对象上迭代的对象。它只在被调用时被初始化或存储在内存中。迭代器使用next从对象中取出元素。

# List is an iterable
lst = [1,2,3,4,5]
for i in lst:
    print(i)

# iterator
lst1 = iter(lst)
next(lst1)
>1
next(lst1)
>2
for i in lst1:
    print(i)
>3,4,5 


▍23、Python中的Map Function是什么？

map函数在对可迭代对象的每一项应用特定函数后，会返回map对象。


▍24、解释Python中的Filter？

过滤器函数，根据某些条件从可迭代对象中筛选值。

# iterable
lst = [1,2,3,4,5,6,7,8,9,10]

def even(num):
    if num%2==0:
        return num

# filter all even numbers
list(filter(even,lst))
---------------------------------------------
[2, 4, 6, 8, 10] 


▍25、解释Python中reduce函数的用法？

reduce()函数接受一个函数和一个序列，并在计算后返回数值。

from functools import reduce

a = lambda x,y:x+y
print(reduce(a,[1,2,3,4]))

> 10 


▍26、什么是pickling和unpickling？

pickling是将Python对象(甚至是Python代码)，转换为字符串的过程。
unpickling是将字符串，转换为原来对象的逆过程。


▍27、解释*args和**kwargs？

*args，是当我们不确定要传递给函数参数的数量时使用的。

def add（* num）：
    sum = 0 
    for val in num：
        sum = val + sum 
    print（sum）


add（4,5）
add（7,4,6）
add（10,34,23）
--------------------- 
9 
17 
67

**kwargs，是当我们想将字典作为参数传递给函数时使用的。

def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))


intro(name="alex",Age=22, Phone=1234567890)
intro(name="louis",Email="a@gmail.com",Country="Wakanda", Age=25)
--------------------------------------------------------------
Data type of argument: <class 'dict'>
name is alex
Age is 22
Phone is 1234567890

Data type of argument: <class 'dict'>
name is louis
Email is a@gmail.com
Country is Wakanda
Age is 25


▍28、解释re模块的split()、sub()、subn()方法？

split()：只要模式匹配，此方法就会拆分字符串。
sub()：此方法用于将字符串中的某些模式替换为其他字符串或序列。
subn()：和sub()很相似，不同之处在于它返回一个元组，将总替换计数和新字符串作为输出。

import re
string = "There are two ball in the basket 101"


re.split("\W+",string)
---------------------------------------
['There', 'are', 'two', 'ball', 'in', 'the', 'basket', '101']

re.sub("[^A-Za-z]"," ",string)
----------------------------------------
'There are two ball in the basket'

re.subn("[^A-Za-z]"," ",string)
-----------------------------------------
('There are two ball in the basket', 10)


▍29、Python中的生成器是什么？

生成器(generator)的定义与普通函数类似，生成器使用yield关键字生成值。

如果一个函数包含yield关键字，那么该函数将自动成为一个生成器。

# A program to demonstrate the use of generator object with next() A generator function 
def Fun(): 
   yield 1
   yield 2
   yield 3

# x is a generator object 
x = Fun()
print(next(x))
-----------------------------
1
print(next(x))
-----------------------------
2


▍30、如何使用索引来反转Python中的字符串?

string = 'hello'

string[::-1]
>'olleh'


▍31、类和对象有什么区别？

类(Class)被视为对象的蓝图。类中的第一行字符串称为doc字符串，包含该类的简短描述。

在Python中，使用class关键字可以创建了一个类。一个类包含变量和成员组合，称为类成员。

对象(Object)是真实存在的实体。在Python中为类创建一个对象，我们可以使用obj = CLASS_NAME()
例如：obj = num()

使用类的对象，我们可以访问类的所有成员，并对其进行操作。

class Person:
    """ This is a Person Class"""
    # varable
    age = 10
    def greets(self):
        print('Hello')


# object
obj = Person()
print(obj.greet)
----------------------------------------
Hello


▍32、你对Python类中的self有什么了解？

self表示类的实例。

通过使用self关键字，我们可以在Python中访问类的属性和方法。

注意，在类的函数当中，必须使用self，因为类中没有用于声明变量的显式语法。


▍33、_init_在Python中有什么用？

“__init__”是Python类中的保留方法。

它被称为构造函数，每当执行代码时都会自动调用它，它主要用于初始化类的所有变量。


▍34、解释一下Python中的继承？

继承(inheritance)允许一个类获取另一个类的所有成员和属性。继承提供代码可重用性，可以更轻松地创建和维护应用程序。

被继承的类称为超类，而继承的类称为派生类/子类。


▍35、Python中OOPS是什么？

面向对象编程，抽象(Abstraction)、封装(Encapsulation)、继承(Inheritance)、多态(Polymorphism)


▍36、什么是抽象？

抽象(Abstraction)是将一个对象的本质或必要特征向外界展示，并隐藏所有其他无关信息的过程。


▍37、什么是封装？

封装(Encapsulation)意味着将数据和成员函数包装在一起成为一个单元。

它还实现了数据隐藏的概念。


▍38、什么是多态？

多态(Polymorphism)的意思是「许多形式」。

子类可以定义自己的独特行为，并且仍然共享其父类/基类的相同功能或行为。


▍39、什么是Python中的猴子补丁？

猴子补丁(monkey patching)，是指在运行时动态修改类或模块。

from SomeOtherProduct.SomeModule import SomeClass

def speak(self):
    return "Hello!"

SomeClass.speak = speak


▍40、Python支持多重继承吗？

Python可以支持多重继承。多重继承意味着，一个类可以从多个父类派生。


▍41、Python中使用的zip函数是什么？

zip函数获取可迭代对象，将它们聚合到一个元组中，然后返回结果。

zip()函数的语法是zip(*iterables)

numbers = [1, 2, 3]
string = ['one', 'two', 'three'] 
result = zip(numbers,string)

print(set(result))
-------------------------------------
{(3, 'three'), (2, 'two'), (1, 'one')}


▍42、解释Python中map()函数？

map()函数将给定函数应用于可迭代对象(列表、元组等)，然后返回结果(map对象)。

我们还可以在map()函数中，同时传递多个可迭代对象。 

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)

print(list(result))


▍43、Python中的装饰器是什么？

装饰器(Decorator)是Python中一个有趣的功能。

它用于向现有代码添加功能。这也称为元编程，因为程序的一部分在编译时会尝试修改程序的另一部分。

def addition(func):
    def inner(a,b):
        print("numbers are",a,"and",b)
        return func(a,b)
    return inner

@addition
def add(a,b):
   print(a+b)

add(5,6)
---------------------------------
numbers are 5 and 6
sum: 11


▍44、编写程序，查找文本文件中最长的单词

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))
----------------------------------------------------
['comprehensions']


▍45、编写程序，检查序列是否为回文

a = input("Enter The sequence")
ispalindrome = a == a[::-1]

ispalindrome
>True


▍46、编写程序，打印斐波那契数列的前十项

fibo = [0,1]
[fibo.append(fibo[-2]+fibo[-1]) for i in range(8)]

fibo
> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


▍47、编写程序，计算文件中单词的出现频率

from collections import Counter

def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print(word_count("test.txt"))


▍48、编写程序，输出给定序列中的所有质数

lower = int(input("Enter the lower range:"))
upper = int(input("Enter the upper range:"))
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(lower, upper)))

-------------------------------------------------
Enter the lower range:10
Enter the upper range:50
[11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

▍49、编写程序，检查数字是否为Armstrong

图片

将每个数字依次分离，并累加其立方(位数)。

最后，如果发现总和等于原始数，则称为阿姆斯特朗数(Armstrong)。

num = int(input("Enter the number:\n"))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


▍50、用一行Python代码，从给定列表中取出所有的偶数和奇数

a = [1,2,3,4,5,6,7,8,9,10]
odd, even = [el for el in a if el % 2==1], [el for el in a if el % 2==0]

print(odd,even)
> ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])

---

### **python的内存管理机制，如何避免循环引用的问题**

引用计数；分代回收；标记-清除

https://zhuanlan.zhihu.com/p/124290355

当一个对象有新的引用时，对象的引用计数+1；当一个对象的引用被销毁时，对象的引用计数-1；

循环引用导致引用计数不能清零会造成内存泄漏；函数的参数适用了可变变量 `list` `dict`  而默认不是这种可变变量

如果循环引用中，两个对象都定义了*__del__*方法，gc模块不会销毁这两个不可达对象，因为gc模块不知道应该先调用哪个对象的*__del__*方法（例如，两个对象a和b，如果先销毁a，则在销毁b时，会调用b的*__del__*方法，该方法中很可能使用了a，这时会造成异常），所以为了安全起见，gc模块会把对象放到*gc.garbage*中，并把它们称为uncollectable。很明显，这种情况会造成内存泄漏，要解决的话，只能显式调用其中某个对象的*__del__*方法来打破僵局。


### **在python中随机化列表中的元素**

```
numpy.random.randint(k, size=n)
numpy.random.shuffle(seq)
random.sample(seq, k)
random.choice(seq)
```


### **python iterator generator**

​						迭代器	生成器

可迭代对象	 序列 (字符串，列表，元组)

​						字典

可迭代的对象的意思是就是说这个实体是可迭代的，例如字符、列表、元组、字典、迭代器等等，可以用for ... in进行循环，可以使用for循环迭代的标志是内部实现了`__iter__`方法。

可迭代对象仅含有`__iter__`的内部方法，你可以通过封装next()方法（python3中为`__next__()`）来将其做成一个迭代器，以生成器（generator，特殊的函数类型的迭代器）为例，你可以通过yield关键字来做一个迭代器，只不过名字被叫做generator，yield可以看做就是为对象添加了`__iter__`方法和指示下一次迭代的`next()/__next__()`方法。

使用isinstance(实体名,Iterable)可判断是否为可迭代对象

在py2中 range 和 xrange 前者返回list后者返回的是一个生成器，不会一下子开辟出所有的内存空间，生成一个开一个。



### **with 语法的实现方式**

帮助实现了一个`__enter__` 和 `__exit__` 的方法。读取和退出的时候自动调用，在操作文件或网络的异步操作的时候很有用。


### **python 类里面的mixin的用法**

相当于一种多重继承，子类拥有所有父类的变量、成员函数。


### **如何创建一个python的元类**

实例对象是由类来创建，类是由元类来创建的。

python的类都是由 `type` 类继承的，可以想象为元类是一个类的父类。

在Django中多用元类创建语法糖。


### **python的线程进程和携程协程**

进程：是CPU对程序的一次**执行过程**、一次**执行任务**。各个进程有自己的内存空间、数据栈等。

线程：是进程中执行运算的最小单位，是进程中的一个**实体**。

协程：比线程更小的执行单元，又称微线程，在单线程上执行多个任务，自带CPU上下文。想要使用协程，那么我们的任务必须有等待。当我们要完成的任务有耗时任务，属于IO密集型任务时，我们使用协程来执行任务会节省很多的资源。

python使用`threading`实现多线程，使用`gevent + asyncio`实现携程。在Python的进程里只有一个GIL。一个线程需要执行任务，必须获取GIL。

​	* 好处：直接杜绝了多个线程访问内存空间的安全问题。

​	* 坏处：Python的多线程不是真正多线程，不能充分利用多核CPU的资源。


### **python性能调优**

首先看瓶颈在哪里，如果在CPU计算比较重可以用c实现一下；如果是跟code关系不大主要是网络数据库这一块，就要看sql语法和携程调用有没有充分使用；`line_profiler` 在code里写上可以帮助分析这一块的性能； `cProfiler` 帮助分析整体性能；火焰图 


### **同步异步阻塞非阻塞**

- 同步和异步关注的是**消息通信机制**。所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该调用就不返回；而异步则是相反，调用在发出之后，这个调用就直接返回了，所以没有返回结果**。

  你打电话问书店老板有没有《分布式系统》这本书，如果是同步通信机制，书店老板会说，你稍等，”我查一下"，然后开始查啊查，等查好了（可能是5秒，也可能是一天）告诉你结果（返回结果）。
  而异步通信机制，书店老板直接告诉你我查一下啊，查好了打电话给你，然后直接挂电话了（不返回结果）。然后查好了，他会主动打电话给你。在这里老板通过“回电”这种方式来回调。

- 阻塞和非阻塞关注的是**程序在等待调用结果（消息，返回值）时的状态**。阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回；非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。

  你打电话问书店老板有没有《分布式系统》这本书，你如果是阻塞式调用，你会一直把自己“挂起”，直到得到这本书有没有的结果，如果是非阻塞式调用，你不管老板有没有告诉你，你自己先一边去玩了， 当然你也要偶尔过几分钟check一下老板有没有返回结果。
  在这里阻塞与非阻塞与是否同步异步无关。跟老板通过什么方式回答你结果无关

  

### **http 1.0 / 1.1 / 2.0**

首先http协议是一种构建在TCP协议之上的应用层协议,主要是用途客户端和服务端的沟通.

- HTTP1.1默认使用长连接，可有效减少TCP的三次握手开销。
- HTTP 1.1支持只发送header信息(不带任何body信息)，如果服务器认为客户端有权限请求服务器，则返回100，否则返回401。客户端如果接受到100，才开始把请求body发送到服务器。这样当服务器返回401的时候，客户端就可以不用发送请求body了，节约了带宽。
- HTTP2.0对header压缩；使用多路复用技术，多路复用允许同时通过单一的 HTTP/2 连接发起多重的请求-响应消息。



### **TCP/IP**

- 应用层

- 表示层

- 会话层

- 传输层

  |            | TCP                                              | UDP                                        |
  | ---------- | ------------------------------------------------ | ------------------------------------------ |
  | 可靠性     | 可靠                                             | 不可靠                                     |
  | 连接性     | 面向连接                                         | 无连接                                     |
  | 效率       | 传输效率低                                       | 传输效率高                                 |
  | 双工性     | 全双工                                           | 一对一、一对多、多对一、多对多             |
  | 传输速度   | 慢                                               | 快                                         |
  | 应用场景   | 对效率要求低，对准确性要求高或者要求有链接的场景 | 对效率要求高，对准确性要求低的场景         |
  | 应用层协议 | SMTP电子邮件/HTTP万维网/FTP文件传输              | DNS域名转换/TFTP文件传输/NFS远程文件服务器 |

  

- 网络层				

  - 路由器	拥有独立MAC帮助转发，本身没有传输包的功能实际传输是委托给数据链路层的

  - IP协议是不可靠协议，数据处理被认为是上层协议要做的事

  - 32位IP地址分为网络位和地址位，这样可以减少路由表记录的数目

    - A类IP地址：0.0.0.0 ～1 27.0.0.0
    - B类IP地址：128.0.0.1 ～ 191.255.0.0
    - C类IP地址：192.168.0.0 ～ 239.255.255.0

    

- 数据链路层		
  - 交换机	通过维护一张MAC地址表，只发送给目标MAC地址指向的那一台电脑（以太网）

- 物理层				
  - 集线器	无脑将信号转发给所有MAC地址

### **swap 虚拟内存**

虚拟内存则是虚拟出来的、使用磁盘代替内存。memory就是机器的物理内存，读写速度低于cpu一个量级，但是高于磁盘不止一个量级。所以，程序和数据如果在内存的话，会有非常快的读写速度。内存的断电丢失数据是一个不能把所有数据和程序都保存在内存中对原因。当内存没有可用的，就必须要把内存中不经常运行的程序给踢出去。但是踢到哪里去，这时候swap就出现了。**swap全称为swap place，即交换区**，当内存不够的时候，被踢出的进程被暂时存储到交换区。当需要这条被踢出的进程的时候，就从交换区重新加载到内存，否则它不会主动交换到真实内存中。



### **冒泡排序\快速排序\你了解的排序算法**