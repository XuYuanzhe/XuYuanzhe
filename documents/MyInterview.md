# 2022 面经

### 5/31 
* **15:00** 航天金穗
```
python的魔术方法了解嘛？__new__ __init__ 谁先被调用？
    -new先，init是初始化调用
with用过吗？知道它做了什么吗？什么时候会用，或者说他能打开什么？
    -帮助实现了一个 __enter__ 和 __exit__ 的方法。读取和退出的时候自动调用，在操作文件或网络的异步操作的时候很有用。
解释 *args 和 **kwargs
    -前者是当我们不确定要传递给函数参数的数量时使用的，后者是当我们想将字典作为参数传递给函数时使用的。
知道面向对象吗？
    -封装、继承和多态是面向对象的三大特点
self的用法呢
    -self 代表类的实例，不代表类，代表当前对象的地址，而 self.__class__ 则指向类，通过使用self关键字，我们可以在Python中访问类的属性和方法。
redis用过那些场景？
写个快排吧？
设计个场景一个手机号接收多个账号验证码，现在有 100 个账号要登陆只有 1 个手机怎么处理？
如何避免死锁？
```

# 2021 面经

### 3/2 

* **19:00** 百观科技

### 3/3 

- **18:30** 启明合心

### 3/4 

- **11:00** 阿凡提教育

    <a href="https://leetcode-cn.com/problems/plus-one/">leetcode 66 加一</a>

    <a href="https://leetcode-cn.com/problems/merge-intervals/">leetcode 56 合并区间</a>

    <a href="https://leetcode-cn.com/problems/ones-and-zeroes/">leetcode 474 一和零</a>

- **12:30** 旭闻科技（修改面试时间至3/5）

- **15:00** 途游游戏

  地点：<a href="#">朝阳区 暖山生活广场 B座3F</a>

```
python协程与进程的区别？
    -进程有自己的内存空间，数据栈；协程是一种微线程，自带CPU上下文，若想使用协程则程序中必须有等待，协程执行任务更节省资源。
cpython的dict底层使用的数据结构？
    -哈希表，key必须是可哈希对象。
cpython的gc有哪几种？
    -引用计数；标记-清除；分代回收
OSI网络分层模型？
    -物理层-数据链路层-网络层-传输层-会话层-表示层-应用层
TCP/UDP的区别？
    -TCP可靠但效率低，UDP不可靠但效率高
列举五种设计模式？
    -单例模式——保证一个类仅有一个实例,并提供一个访问它的全局控制点。比如在加-载配置文件时, 可使用该模式。
    -工厂模式——定义一个用以创建对象的接口, 让子类决定实例化哪个类。当遇到需要-根据某个前提条件创建不同的类实现时, 会实用工厂模式
    -装饰者模式——动态的给一个类添加额外的指责。
列举redis的五种数据类型，及应用场景，及底层数据结构？
    String 字符串 全局ID、Session缓存
    Hash 可以将相关的值聚集存储在一起，节省内存空间。
    set 无序集合 点赞、签到、打卡、标签、抽奖
    List 队列和栈 消息队列
    zset 有序集合
如何使用redis实现分布式锁？
    -setnx+lua
redis的内存管理机制与gc？
    -1.被动过期（惰性删除）：key被访问时，如果发现它已经过期就删除。
    -2.主动过期（定期删除）：周期性地从过期字典中选择一部分失效的主键删除。
mongo的ObjectId包含哪些信息？
    -是一个12字节的BSON类型字符串：UNIX时间戳；运行MongoDB的机器；生成此_id的进程；由一个随机数开始的计数器生成的值。
mongo索引有哪几种类型？
    -单字段索引、复合索引、多key索引、文本索引
mongo索引用到什么数据结构？
    -B树
mongo分片集群的架构？
```

* **17:30** 百观科技

  地点：<a href="#">东城区 东直门南大街 来福士办公楼2206室</a>

```
空间复杂度为O(1)的列表去重操作？
    -排序、双指针遍历
```

### 3/5

- **10:30** 阿凡提教育

  地点：<a href="#">海淀区 清河永泰园甲一号 建金中心401-403室</a>

```python
# 在1亿数据中找到最大的1w个？
data_list = []
def foo():
    max_list = []
    for data in data_list:
      if data not in max_list:
        max_list.append(data)
        if len(max_list) > 10001:
          max_list.remove(min(max_list))
    return max_list
```

- **12:30** 旭闻科技

  地点：<a href="https://meeting.tencent.con/s/9mpm7thtmnkc">线上面试房间</a>

    <a href="https://leetcode-cn.com/problems/spiral-matrix">leetcode54 螺旋矩阵</a>

- **16:00** 启明合心

  地点：<a href="#">海淀区 知春路 量子芯座1607室</a>

```python
# 台阶问题/斐波那契
fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

- **19:00** 百度

  地点：<a href="https://infoflow.baidu.com/voip/api/meeting/middle/index.html?id=54c7cf2be36c4c3d303151d6a6f1a345#/pc">线上面试房间</a>

    <a href="https://leetcode-cn.com/problems/swap-nodes-in-pairs/">leetcode 24 两两交换链表中的节点</a>

    <a href="https://leetcode-cn.com/problems/3sum/">leetcode 15 三数之和</a>
```
列表和元组的区别是什么?
    元组和列表最大的区别就是，列表中的元素可以进行任意修改，就好比是用铅笔在纸上写的字，写错了还可以擦除重写；而元组中的元素无法修改，除非将元组整体替换掉，就好比是用圆珠笔写的字，写了就擦不掉了，除非换一张纸；可以理解为，tuple 元组是一个只读版本的 list 列表。
已经有了list类型为什么有tuple类型数据?
    https://sikasjc.github.io/2018/06/20/list-and-tuple/
```


### 3/6

- **11:30** BuzzBreak旭闻科技

  地点：<a href="#">海淀区 马甸东路 金奥国际商业区206号</a>

```
用Redis来实现限制一个api或页面访问的频率，例如单ip或单用户一分钟之内只能访问多少次？

    -在redis中保存一个count值（int），key为user:$ip，value为该ip访问的次数，第一次设置key的时候，设置expires。
count加1之前，判断是否key是否存在，不存在的话，有两种情况：1、该ip未访问过；2、该ip访问过，但是key已经过期了。那么此时需要再次设置一次expires。如果用户访问的时候，判断count的值是否大于上限，如果低于上限，就处理请求，否则就拒绝处理请求。

# 考虑这种情况，假设只允许用户60秒内访问100次，如果有一个用户在第1秒访问了1次，在第59秒的时候，访问了99次，然后在第61秒的时候，访问了100次。如果按照策略1的情况处理，第1~60秒之间接受了100次，在第61秒接收100次请求，所以62~120这段时间内，不再处理该ip的请求。
# 貌似没问题，但是，细细思考一下，第59秒到61秒之间接受了99+100=199请求，时间间隔只有3秒。那么这样的话，最初的设计就存在问题了。
解决方案：可以使用redis的list（双向队列）数据结构，key就是user:$ip，也就是每一个ip设置一个双向队列，每次请求到达的时候，进行如下判断：
1、如果list中的元素个数少于100个，那么就将请求到达时的时间戳Lpush到list中。
2、如果list中的元素多余100个，那么，就取出Lindex(-1)即最右边，也就是100个请求中最早的那一个请求的时间戳，如果最早的时间戳和当前时间戳相差超过60秒，那么表示第一个请求已经过期了，就将第一个请求出队Rpop。然后将当前时间戳入队Lpush
```

### 3/11

- **20:00** 学堂在线
- **20:00** 百度视频
  
  地点：<a href="https://meeting.tencent.com/s/fEo6TQMpTQYI">线上面试房间</a>

### 3/12

- **11:00** Moka

  地点：<a href="#">北京市 海淀区 知春路68号领航科技大厦4层</a>

``` python
# 什么时候会用到装饰器？适用于那些场景？有什么好处？
# 手写装饰器 面向切片编程 
import functools

def decorator(fn):
  context = 1
  
  @functools.wraps(fn)
  def wrapper(*args, **kwargs):
    print("context", context)
    return fn(*args, **kwargs)
  return wrapper


@decorator
def func():
  print("I am target")

func()


#带参数的装饰器
def decorator_out(context):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print("context", context)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@decorator_out(3)
def test(*args, **kwargs):
    print(1)

test()
```

- **15:00** 天眼查
  
  地点：<a href="https://interview.nowcoder.com/interview/19553573/interviewee?code=2bIX4HKc">线上面试房间</a>
  
  <a href="https://leetcode-cn.com/problems/xx4gT2/">剑指 Offer II 076. 数组中的第 k 大的数字</a>

### 3/16

- **20:00** 百度

  地点：<a href="https://infoflow.baidu.com/voip/api/meeting/middle/index.html?id=201f6a8f9eed52990f6b46ac3e398180#/pc">线上面试房间</a>

```python
# 一个自然数可以分解为若干个自然数相乘，对于指定自然数n,请求出每种分解自然数之和最小的一个（不考虑1，若是素数，则是它本身）
def foo(n):
    rv = []
    for i in range(2, n+1):
        if n % i == 0:
            ii = n // i
            rv.append(i + ii)
    return min(rv)

foo(24)
```

### 3/17

- **10:00** GamesVessel

  地点：<a href="#">海淀区 王庄路 清华同方科技广场D座东楼12层</a>

### 3/20 

- **11:00** GamesVessel
  
  地点：<a href="#">海淀区 王庄路 清华同方科技广场D座东楼12层</a>
  
### 3/23

- **15:00** 猿辅导
  
  地点：<a href="#">朝阳区 阜荣街10号首开广场B座</a>

### 3/28

* **14:00** 字节跳动
  
  地点：<a href="https://people.toutiaocloud.com/hire/bridge/video/interviewee/893c9fe4-59e2-4592-b32d-1186a550a2f4">线上面试房间</a>

### 6/10

* **14:00** 豆瓣

  地点：<a href="#">酒仙桥路14号兆维工业园B3区1门3层</a>

```python
# 假设有如下字符串匹配模式：+ 表示匹配一个字符，* 表示匹配任意多个（0个或多个）字符，请编写一个函数满足这两种符号。如 "x+1yz*z" 匹配 "xy1yzxyyz" 。

```

### 9/14

* **15:00** 智线云科技 **现场面试**（三面没过）
  
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/20210922185358.png)

⬆图一

![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/20210922185437.png)

⬆图二
```
一面
说说你解决过的最难的一个网页爬虫问题
了解MySQL的两种引擎吗？
    - InnoDB和MyISAM
      InnoDB 支持事务，MyISAM 不支持事务
      InnoDB 支持外键，MyISAM 不支持
      InnoDB 是聚集索引，MyISAM 是非聚集索引
redis有几种数据类型知道吗？
列举一下python常用的数据类型？
这其中哪些是可变的数据类型？
    -list dict可变，tuple string int float bool不可变
dict的底层逻辑是什？元组可以做dict的key吗？为什么？
    -hashmap 可以 因为可哈希
做过py2向py3迁移，能列举几个他们的区别吗？
    -print函数 字符串 True False


二面
scrapy框架中最重要的文件是哪一个？组合集成了middlewares、pipelines这些模块的那个文件叫什么？
    -scrapy.cfg是针对Scrapy框架的配置；
     settings.py是针对于项目本身的设置，比如用什么中间件、并发数量、UA、Pipelines等等
scrapy创建项目的时候都包含哪些文件说得上来吗？
    scrapy.cfg            # deploy configuration file
    tutorial/             # project's Python module, you'll import your code from here
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
scrapy的工作模式是什么样的？
    -Scrapy框架主要由六大组件组成，它们分别是调度器(Scheduler)、下载器(Downloader)、爬虫（Spider）、中间件（Middleware）、实体管道(Item Pipeline)和Scrapy引擎(Scrapy Engine)
    1、Scrapy Engine(引擎): 引擎负责控制数据流在系统的所有组件中流动，并在相应动作发生时触发事件。
    2、Scheduler(调度器): 调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎。
    3、Downloader（下载器）： 下载器负责获取页面数据并提供给引擎，而后提供给spider。
    4、Spider（爬虫）： Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。 每个spider负责处理一个特定(或一些)网站。
    5、Item Pipeline(管道)： Item Pipeline负责处理被spider提取出来的item。典型的处理有清理、 验证及持久化(例如存储到数据库中)。
    6、Downloader Middlewares（下载中间件）： 下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
    7、Spider Middlewares（Spider中间件）： Spider中间件是在引擎及Spider之间的特定钩子(specific hook)，处理spider的输入(response)和输出(items及requests)。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。
聊一聊你在工作中使用git的一些命令和方法
    -git remote 
聊一聊Linux你用过的一些指令吧
    -ps grep ls ll touch cp cat vim scp top cd rm mkdir mv which su pwd kill zip
怎么查询日志最近的一条输出？
    -tail -f -n 10
我写一个例子 <s>://<host>:<port>/<path> 把他理解为一个url这样完整吗？
    -不完整，但说不上来
访问http://www.baidu.com实际上是访问了哪里？
连接数据库需要哪些信息？
    -host、port、user、pwd、db这些吧
    -那这些是怎么组合起来访问的呢？
    -<s>://<host>:<port>/?user=xxx&pwd=xxx
    -应该是 <s>://<username>:<password>@<host>:<port>/<path>
说说你这里的gRPC是什么吧
    -gRPC是google开源的一个高性能、跨语言的RPC框架
那怎么理解RPC？他是基于什么实现的呢？比如http服务是基于http协议的
    -Remote Procedure Call Protocol（远程过程调用协议）
     本质的区别就是RPC主要是基于TCP/IP协议的
你这里不可以写shell命令，他是一种应用程序那你说说$1在shell中是什么含义
    -第一个传递的参数
那$0呢
    -Shell本身的文件名
` `用过吗？可以讲讲吗？
    -被单引号括起来的字符都是普通字符，就算特殊字符也不再有特殊含义；
     而被双引号括起来的字符中，"$"、"\"和反引号是拥有特殊含义的，
     "$"代表引用变量的值，而反引号代表引用命令
你这里写Flask + Rdis + JavaScript那flask他是一个server吗？
    -用flask写了一个简单的server
怎么启动服务的呢？
    -python main.py
这里不会有一些问题吗？如果现在服务挂掉了怎么办？
    -了解比较浅
uwsgi听说过吗？
    -听说过，具体记不清了
有用过Django的框架吗？
    -写过简单的blog项目
那你写blog里面的登陆发布这些模块叫什么知道吗？
    -APP?
对app，所以你启的这个main.py不能称之为是一个service，应该用uwsgi+nginx来做，了解nginx吗？
    -好像是做负载均衡的
嗯，呐说说你知道哪些负载均衡的模式
    -记不清了（基于DNS负载均衡[解析ip分配给服务器]，基于硬件负载均衡，基于软件负载均衡[根据OSI分为四层和七层负载均衡，本质上是把数据包偷天换日]）
    -正向代理与反向代理
    -两者的区别在于代理的对象不一样：正向代理代理的对象是客户端(科学上网工具)，反向代理代理的对象是服务端(拨打10086,访问baidu.com)
    
    两层结构（图一）
    -在这种结构里,uWSGI作为服务器，它用到了HTTP协议以及wsgi协议，flask应用作为application，实现了wsgi协议。当有客户端发来请求，
     uWSGI接受请求，调用flask app得到相应，之后相应给客户端。通常来说，Flask等web框架会自己附带一个wsgi服务器(这就是flask应用可以直接启动的原因)，
     但是这只是在开发阶段用到的，在生产环境是不够用的。
    三层结构（图二）
    -这种结构里，uWSGI作为中间件，它用到了uwsgi协议(与nginx通信)，wsgi协议(调用Flask app)。当有客户端发来请求，nginx先做处理(静态资源是nginx的强项)，
     无法处理的请求(uWSGI),最后的相应也是nginx回复给客户端的。
    
你也用过tornado框架，那你觉得它和flask、django这两个是一回事吗？
    -tornado是一个服务器程序，如何理解，我觉得比如tornado提供了控制webserver的方式，控制层面包括了各种webserver的细节。当然tornado中是可以定义对于web请求的返回
你这里说用过mitmporxy用它是帮助做什么事的呢？


三面
你的个人职业规划是什么？技术专精又或是架构师方向？
说一下你解决过的最难的问题？
有没有想过修改Selenium的一些参数让对方网站无法识别？
你说你注重专业基础学习，那我想问一下二叉查找树的时间复杂度是多少？
    -logn 应该是平衡状态下 logn 最慢是 n 在一条链上
这里的n是什么呢？
    -n 个节点
二叉查找树和二分法哪个速度更快？
    -两者时间复杂度都是 log2(n)
    -两者明显的区别是二分查找速度快删除和插入困难，二对于建立的二叉树索引来说，他的插入和删除是相对较快的。为什么会出现这两者的差别其实底层更多的考虑的是数据的存储结构：
    1）从空间性能，顺序存储会对空间资源做到百分之百的利用，而链式存储对对空间的利用不是百分之百，因为存储了指针，不是真正的数据
    2）从时间性能上来讲读取速度的话顺序存储更优，插入和删除操作链式存储更优，链式存储只需要移动指针，不需要移动元素。
什么时候采用二分什么时候采用二叉索引？
    1）如果我们的数据是不进行频繁变化且是有序，而且查询相对较多的情况下采用二分查找
    2）我们的数据是频繁变化的考虑到后面的数据扩容的情况下，我们考虑采用二叉索引的方式，但是这种会有一点空间资源的牺牲。

对操作系统有理解吗？
什么是僵尸进程什么是孤儿进程？
    -就是只要子进程退出，父进程还在运行，但父进程没有读取子进程状态，子进程进入僵尸状态（Z状态），会造成内存泄漏、内存资源浪费；
     父进程先于子进程退出，子进程会被1号进程领养，1号进程称init进程。1号进程会在子进程退出的时候，回收子进程的退出信息，防止子进程变成僵尸进程，没什么危害
```
  
  

### 9/23

* **10:30** 懂球帝

  地点：<a href="#">海淀区锦秋国际大厦B座11F</a>
  
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/20210922172935.png)

⬆图三

```
# 手写一个快排算法
def quick_sort(arr):
    if not arr:
        return[]
    else:
        first=arr[0]
        left=quick_sort([l for l in arr[1:]if l<first])
        right=quick_sort([r for r in arr[1:]if r>=first])
        return left+[first]+right 

# 手写一个字符串反转
a = '123456789'
b1 = a[::-1]
b2 = ''.join(reversed(a))

画一个scrapy的架构图
    -图三
redis的几种数据结构了解吗？
    String 字符串。
        全局ID：使用int类型的incrby的原子性；
        热点数据缓存；
    Hash可以将相关的值聚集存储在一起，节省内存空间。
    Set	无序集合
        点赞、签到、打卡、标签、抽奖
    List存储有序的字符串(从左到右)，元素可以重复。可以充当队列和栈的角色。
        消息队列。
    Zset 有序集合
        排行榜
怎么判断二叉树平衡？
    -AVL 左右两个子树的高度差的绝对值均不超过1    
```


* **14:00** Momenta
```
说说进程线程和协程？
都说python慢，慢在哪里？
    -全局解释器锁(Global Interpreter Lock)（GIL）, 是因为 Python 是解释型语言而不是编译型语言, 是因为 Python 是一种动态类型的语言
python2和python3的区别你觉得哪个点你印象比较深？
    -print不再是语句，而是函数；
     Python2 默认编码是 ASCII，Python3 默认编码是 Unicode(utf-8)；
     在 Python2 中很多返回列表对象的内置函数和方法在Python3都改成了返回类似于迭代器的对象，因为迭代器的惰性加载特性使得操作大数据更有效率；
     True 和 False 在 Python2 中是两个全局变量，在数值上分别对应 1 和 0 Python3 修正了这个缺陷，True 和 False 变为两个关键字。
```


* **15:00** 知乎
  
  地点：<a href="#">海淀区学院路甲 5 号 768 创意园 A座15号门1002</a>
  
```
一个数组把0放在右边其他元素顺序排列不变
说说三次握手四次挥手？
如果 C 发送的 ack S 没有接收会出现什么情况？
二叉树的三种遍历?
    -先、中、后（基于根节点）
说说进程线程和协程？
    -最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
    -第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
    -因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
那协程是用户态还是内核态？
    -协程就是一种用户态内的上下文切换技术，协程是一种用户态的轻量级线程。
画一个scrapy的架构图
    -图三
git出现冲突pull不下code怎么解决？
什么是死锁？怎么避免？
    -当线程互相持有对方所需要的资源时，会互相等待对方释放资源，如果线程都不主动释放所占有的资源，将产生死锁。
    -尝试获取锁的时候加一个超时时间，这也就意味着在尝试获取锁的过程中若超过了这个时限该线程则放弃对该锁请求。
    -银行家算法是避免死锁的一种重要方法
redis的几种数据结构了解吗？
    -string、set、zset、hash、list
redis为什么快？除了基于内存操作还有其他原因吗？
    -IO多路复用
redis的淘汰机制有了解吗？
    -每隔一段时间扫描如果设置了TTL到点就删除；
     或下次访问key时候删掉数据；
```


* **18:00** 领创集团
```
# 手写一个二叉树中序遍历的递归 value  left  right
def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    
# 手写一个二叉树先序遍历的递归 left  value  right
def preorder(root):
    if not root:
        return 
    print(root.val)
    preorder(root.left)
    preorder(root.right)
   
# 手写一个二叉树后序遍历的递归 left  right value
def postorder(root):
    if not root:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.val)

dict的底层是什么实现的？时间复杂度是多少？为什么？
    -hashmap, O(1), 
MySQL写一条 select 最重要的是什么？
    -命中索引
都说python的多线程是假的但是为什么还要用多线程？好在哪里？
    -多线程有两个好处：CPU并行，IO并行。
     Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
     多核多线程比单核多线程更差，原因是单核下的多线程，每次释放GIL，唤醒的那个线程都能获取到GIL锁，所以能够无缝执行，但多核下，CPU0释放GIL后，其他CPU上的线程都会进行竞争，但GIL可能会马上又被CPU0拿到，导致其他几个CPU上被唤醒后的线程会醒着等待到切换时间后又进入待调度状态，这样会造成线程颠簸(thrashing)，导致效率更低)
你怎么理解这个分布式爬虫的分布式
    -url被分给不同的爬虫，但是不同爬虫的效率又是不一样的，所以说共享队列，共享数据，让效率高的爬虫多去做任务，而不是等着效率低的爬虫
说说yeild函数
    -在一个函数中，程序执行到yield语句的时候，程序暂停，返回yield后面表达式的值，在下一次调用的时候，从yield语句暂停的地方继续执行，如此循环，直到函数执行完。
怎么编写高质量的代码？
    -Type Hints 写的话不仅IDE可以提示你类型与参数；在一些库里可以的到比较友好的提示和错误处理

```


### 9/24

* **15:00** 小黑盒
  
  <a href="https://leetcode-cn.com/problems/3sum/">leetcode 15 三数之和</a>
  
  <a href="https://leetcode-cn.com/problems/find-peak-element/">leetcode 162 寻找峰值</a>


### 9/26

* **14:00** 知乎
  
  地点：<a href="#">海淀区学院路甲 5 号 768 创意园 A座15号门1002</a>

```
# 二分查找算法

# 两个栈实现一个队列

正则匹配 `<.*>` 和 `<.*?>` 分别对 `<h1>title</h1>` 进行正则匹配输出什么
    -前者匹配全部，后者匹配 <h1>
正则匹配里的 * 和 + 有什么区别
    -前者匹配零次或多次，后者匹配一次或多次
```

* **17:00** 小黑盒 

  地点：<a href="#">朝阳区利星行广场B座1601</a>
  
  <a href="https://leetcode.cn/problems/sort-colors/">leetcode75 颜色分类</a>
  
```
# 字符串匹配问题（kmp算法）
https://www.zhihu.com/question/21923021
```

---

## **通用参考**

**我的问题问完了，你还有什么要问我的吗？**
> 您对这个岗位的长期规划是什么？
> 
> 您希望我在短期内解决哪些问题？
> 
> 刚才您问到的xxx问题我答的(不)好，我想问下您是怎么理解这个地方的。
> 
> 您对这个岗位三到五年职业规划的建议是什么呢？

## **其他参考**

面试部分的描述：
https://github.com/tuteng/Best-websites-a-programmer-should-visit-zh#%E9%9D%A2%E8%AF%95%E5%87%86%E5%A4%87

Python Interview：
https://github.com/XuYuanzhe/XuYuanzhe/blob/main/documents/PythonInterview.md

```diff
- text in red
+ text in green
! text in orange
# text in gray
```