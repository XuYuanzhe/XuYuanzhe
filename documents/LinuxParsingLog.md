# Linux 操作系统对log的一些处理手段的记录

**杀僵尸进程：**

　　`ps -ef | grep java` (先查java进程ID)

　　`kill -9 PID` (生产环境谨慎使用)

**kill、killall、pkill命令的区别**

　　**kill**：通过pid来杀死进程

　　**killall （killall [参数] [进程名]）：** Linux系统中的killall命令用于杀死指定名字的进程（kill processes by name）。我们可以使用kill命令杀死指定进程PID的进程，如果要找到我们需要杀死的进程，我们还需要在之前使用ps等命令再配合grep来查找进程，而killall把这两个过程合二为一，是一个很好用的命令。 

　　**pkill：** pkill 和killall 应用方法差不多，也是直接杀死运行中的程式；如果你想杀掉单个进程，请用kill 来杀掉。例子： pkill -9 firefox

 

#### 1.查看日志常用命令

**tail:**  

-n  是显示行号；相当于nl命令；例子如下：

     tail -100f test.log    实时监控100行日志

     tail -n 10 test.log  查询日志尾部最后10行的日志;

     tail -n +10 test.log  查询10行之后的所有日志;

**head:** 

跟tail是相反的，tail是看后多少行日志；例子如下：

     head -n 10 test.log  查询日志文件中的头10行日志;

     head -n -10 test.log  查询日志文件除了最后10行的其他所有日志;

**cat：** 

tac是倒序查看，是cat单词反写；例子如下：

     **cat -n test.log |grep "debug"  查询关键字的日志**
     
#### 2. 应用场景一：按行号查看---过滤出关键字附近的日志

1）cat -n test.log |grep "debug" 得到关键日志的行号



2）通常查找出错误日志 cat error.log | grep 'nick' , 这时候我们还有个需求就是输出当前这个日志的前后几行：

    cat error.log | grep -B 5 'nick' 显示nick及前5行

    cat error.log | grep -A 5 'nick' 显示nick及后5行

    cat error.log | grep -C 5 'nick' 显示file文件里匹配nick字串那行以及上下5行

    cat error.log | grep -n -B10 -A10 5 'nick' 显示file文件里匹配nick字串前后10行

　　

#### 3. 应用场景二：选取日志中特定范围进行分析

1）cat -n test.log |tail -n +1000|head -n 20  从第1000行开始，显示20行

     tail -n +1000表示查询1000行之后的日志

     head -n 20 则表示**在前面的查询结果**里再查前20条记录

2）cat catalina.out | head -n 1400| tail -n +1350 显示1350行到1400行 （实现原理都差不多，就是通过语法糖）

　（1）按日期截取 ：一般在日志系统中都会记录打印日志的时间，通常我们非常需要查找指定时间端的日志：

    sed -n '/2014-12-17 16:17:20/,/2014-12-17 16:17:36/p' test.log

   　　特别说明:该命令中的两个日期值必须是日志文件中包含的值,否则该命令无效.； 先 grep '2014-12-17 16:17:20' test.log 来确定日志中是否有该 时间点

　（2）按行数截取

    sed -n ‘10000,20000p’ test.log         

    sed -i '/关键词/d' catalina.out 删除包含关键词的行

#### 4.应用场景三：日志内容特别多，打印在屏幕上不方便查看

(1)使用**more**和**less**命令,

     如： cat -n test.log |grep "debug" |more   这样就分页打印了,通过点击空格键翻页

(2)使用 >xxx.txt 将其保存到文件中,到时可以拉下这个文件分析

     如：cat -n test.log |grep "debug" >debug.txt

#### 5：使用管道进行and or条件处理

　　and 使用管道实现  例如： grep -n '日志排查' test.log | grep '日志'

　　or 用-E  例如：grep -n -E '日志排查|hello' test.log 满足两个关键字的都可以找出来

 

#### 6：如何看查占用cpu最多的进程？

**方法一**

**核心指令**：ps

**实际命令**：

　　ps H -eo pid,pcpu | sort -nk2 | tail

执行效果如下：

*[work@test01 ~]$ ps H -eo pid,pcpu | sort -nk2 | tail*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*31396  0.6*

*30904  1.0*

*30914  1.0*

**结果**：

瞧见了吧，最耗cpu的pid=30914。

*画外音：实际上是31396。*

 

**方法二**

**核心指令**：top

**实际命令**：

　　top

　　Shift + t

　　top 命令类似于 Windows 的任务管理器，能够显示 Linux 系统中运行的进程的动态实时视图。

　　默认情况下，top 输出结果是按 CPU 占用进行排序，每 5s 更新一次结果。我们可以使用 **`top-b|head-50`** 显示排前 50 的占用 CPU 最高的进程( Linux 中如何找出 CPU 占用高的进程

 )。 

![img](https://img2018.cnblogs.com/i-beta/885859/202002/885859-20200221225546812-1102947004.png)

上面的命令解释如下：

- -b：批次档模式
- head -50：显示输出结果的前 50 个
- PID：进程的 ID
- USER：进程的归属者
- PR：进程的等级
- NI：进程的 NICE 值
- VIRT：进程使用的虚拟内存
- RES：进程使用的物理内存
- SHR：进程使用的共享内存
- S：这个值表示进程的状态: S = 睡眠，R = 运行，Z = 僵尸进程
- %CPU：进程占用的 CPU 比例
- %MEM：进程使用的 RAM 比例
- TIME+：进程运行了多长时间
- COMMAND：进程名字

如果想看进程的完整信息，可以加 -c 参数，如 **`top-b-c|head-50`**

 

### 使用 ps

　　ps 就是进程状态的缩写，可以显示当前运行进程的详细信息，如用户名、用户 ID、CPU 使用率、内存使用、进程启动日期时间、命令名等等。

　　使用 **`ps-eo pid,ppid,%mem,%cpu,cmd--sort=-%cpu|head`** 可以显示占用 CPU 较高的进程信息（注意 `--sort=-%cpu`）。如下：

```
# ps -eo pid,ppid,%mem,%cpu,cmd --sort=-%cpu | head

PID PPID %MEM %CPU CMD

18527 1714 4.2 40.3 /usr/lib/firefox/firefox -contentproc -childID 18 -isForBrowser -prefsLen 10002 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab

1714 1152 5.6 8.0 /usr/lib/firefox/firefox --new-window

18324 1714 4.9 6.3 /usr/lib/firefox/firefox -contentproc -childID 16 -isForBrowser -prefsLen 10002 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab

3286 1714 2.0 5.1 /usr/lib/firefox/firefox -contentproc -childID 14 -isForBrowser -prefsLen 8078 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab

1783 1714 3.0 4.5 /usr/lib/firefox/firefox -contentproc -childID 1 -isForBrowser -prefsLen 1 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab

1227 1152 2.3 2.5 /usr/bin/gnome-shell

1170 1168 3.5 2.2 /usr/lib/Xorg vt2 -displayfd 3 -auth /run/user/1000/gdm/Xauthority -nolisten tcp -background none -noreset -keeptty -verbose 3

16865 1714 2.5 2.1 /usr/lib/firefox/firefox -contentproc -childID 15 -isForBrowser -prefsLen 10002 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab

2179 1714 2.7 1.8 /usr/lib/firefox/firefox -contentproc -childID 6 -isForBrowser -prefsLen 7821 -prefMapSize 213431 -parentBuildID 20191031132559 -greomni /usr/lib/firefox/omni.ja -appomni /usr/lib/firefox/browser/omni.ja -appdir /usr/lib/firefox/browser 1714 true tab
```

上命令的解释如下：

- -e：选择所有进程
- -o：自定义输出格式
- –sort=-%cpu：基于 CPU 使用率对输出结果排序
- head：显示结果的前 10 行
- PID：进程的 ID
- PPID：父进程的 ID
- %MEM：进程使用的 RAM 比例
- %CPU：进程占用的 CPU 比例
- Command：进程名字

如果想看命令名字而不是命令的绝对路径，可以：

![img](https://img2018.cnblogs.com/i-beta/885859/202002/885859-20200221230002358-1096245616.png)

 

 

#### 7：找到了最耗CPU的进程ID，对应的服务名是什么呢？

**方法一**

**核心指令**：ps

**实际命令**： `ps aux | fgrep pid`

执行效果如下：

*[work@test01 ~]$ ps aux | fgrep 30914*

*work 30914  1.0  0.8 309568 71668 ? Sl  Feb02 124:44 ./router2 –conf=rs.conf*

**结果**：

瞧见了吧，进程是./router2

画外音： grep 和fgrep的区别？

两者都是搜索工具，但功能上有区别。
　　1，首先，grep支持的是标准正则表达式。
　　2，fgrep，不支持正则表达式，只用于匹配固定字符串。

所以后者要比前者速度快，当然同时后者的搜索功能要弱于前者。

 

**方法二**

直接查proc即可。

**实际命令**：

ll /proc/pid

执行效果如下：

*[work@test01 ~]$ ll /proc/30914*

*lrwxrwxrwx  1 work work 0 Feb 10 13:27 cwd -> /home/work/im-env/router2*

*lrwxrwxrwx  1 work work 0 Feb 10 13:27 exe -> /home/work/im-env/router2/router2*

*画外音：这个好，全路径都出来了。*

 

#### 8：如何查看某个端口的连接情况？

**方法一**

**核心指令**：netstat

**实际命令**：

　　netstat -lap | fgrep port

执行效果如下：

*[work@test01 ~]$ netstat -lap | fgrep 22022*

*tcp     0    0 10.58.xxx.29:22022      \*:*             LISTEN    31396/imui*

*tcp     0    0 10.58.xxx.29:22022      10.58.xxx.29:46642      ESTABLISHED 31396/imui*

*tcp     0    0 10.58.xxx.29:22022      10.58.xxx.29:46640      ESTABLISHED 31396/imui*

 

**方法二**

**核心指令**：lsof

**实际命令**：

　　lsof -i :port

执行效果如下：

*[work@test01 ~]$ /usr/sbin/lsof -i :22022*

*COMMAND  PID USER  FD  TYPE  DEVICE SIZE NODE NAME*

*router  30904 work  50u  IPv4 69065770    TCP 10.58.xxx.29:46638->10.58.xxx.29:22022 (ESTABLISHED)*

*router  30904 work  51u  IPv4 69065772    TCP 10.58.xxx.29:46639->10.58.xxx.29:22022 (ESTABLISHED)*

*router  30904 work  52u  IPv4 69065774    TCP 10.58.xxx.29:46640->10.58.xxx.29:22022 (ESTABLISHED)*

 

#### 9：归档压缩文件导出指定内容到文件

**命令**：  zcat 压缩文件 |grep '关键词' > 111.txt

 

注：**>>** 为追加；**>** 为重定向，会覆盖原先的内容

 

 

#### 10：查找关键字及其前后的信息

 

- **根据关键字查看日志**

```
　　　　cat hrun.log | grep "新增用户"
```

- **根据关键字查看后10行日志**

```
　　　　cat hrun.log | grep "新增用户" -A 10
```

- **根据关键字查看前10行日志**

```
　　　　cat hrun.log | grep "新增用户" -B 10
```

- **根据关键字查看前后10行日志，并显示出行号**

```
　　　　cat -n hrun.log | grep "新增用户" -C 10
```

- **查看日志前 50 行**

```
　　　　cat hrun.log | head -n 50
```

- **查看日志后 50 行，并显示出行号**

```
　　　　cat -n hrun.log | tail -n 50
```

> **说明：**
> **-A** 表示关键字之后，After
> **-B** 表示关键字之前，Before
> **-C** 表示关键字前后，Context

#### 11: nohup的作用

　

**nohup**命令：如果你正在运行一个进程，而且你觉得在退出帐户时或者关闭客户端该进程还不会结束，那么可以使用nohup命令。该命令可以在你退出帐户/关闭终端之后继续运行相应的进程。在缺省情况下该作业的所有输出都被重定向到一个名为nohup.out的文件中。

```
nohup command > myout.file 2>&1 &  
```

在上面的例子中，**0 – stdin (standard input)，1 – stdout (standard output)，2 – stderr (standard error) ；**


2>&1是将标准错误（2）重定向到标准输出（&1），标准输出（&1）再被重定向输入到myout.file文件中。


**1、nohup和&的区别**

　　**&** ： 指在后台运行

　　**nohup** ： nohup运行命令可以使命令永久的执行下去，和用户终端没有关系，例如我们断开SSH连接都不会影响他的运行，注意了nohup没有后台运行的意思；&才是后台运行，

　　

　　&是指在后台运行，但当用户退出(挂起)的时候，命令自动也跟着退出

　　nohup可以使用Ctrl+C结束掉，而&使用Ctrl+C则结束不掉，nohup不受终端关闭，用户退出影响，而&则受终端关闭，用户退出影响

结合起来用就是

```
nohup COMMAND &
```

这样就能使命令永久的在后台执行

 

 

#### 12：Linux PATH环境变量及作用

 

　　在讲解 PATH 环境变量之前，首先介绍一下 which 命令，它用于查找某个命令所在的绝对路径。例如：

```
[root@localhost ~]# which rm
/bin/rm
[root@localhost ~]# which rmdir
/bin/rmdir
[root@localhost ~]# which ls
alias ls='ls --color=auto'
        /bin/ls
```

注意，ls 是一个相对特殊的命令，它使用 alias 命令做了别名，也就是说，我们常用的 ls 实际上执行的是 ls --color=auto。

通过使用 which 命令，可以查找各个外部命令（和 Shell 内置命令相对）所在的绝对路径。学到这里，读者是否有这样一个疑问，为什么前面在使用 rm、rmdir、ls 等命令时，无论当前位于哪个目录，都可以直接使用，而无需指明命令的执行文件所在的位置（绝对路径）呢？其实，这是 PATH 环境变量在起作用。

首先，执行如下命令：

```
[root@localhost ~]# echo $PATH
/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:/root/bin
```

这里的 echo 命令用来输出 PATH 环境变量的值（这里的 $ 是 PATH 的前缀符号），PATH 环境变量的内容是由一堆目录组成的，各目录之间用冒号“:”隔开。当执行某个命令时，Linux 会依照 PATH 中包含的目录依次搜寻该命令的可执行文件，一旦找到，即正常执行；反之，则提示无法找到该命令。

> 如果在 PATH 包含的目录中，有多个目录都包含某命令的可执行文件，那么会执行先搜索到的可执行文件。

从执行结果中可以看到，/bin 目录已经包含在 PATH 环境变量中，因此在使用类似 rm、rmdir、ls等命令时，即便直接使用其命令名，Linux 也可以找到该命令。

为了印证以上观点，下面举个反例，如果我们将 ls 命令移动到 /root 目录下，由于 PATH 环境变量中没有包含此目录，所有当直接使用 ls 命令名执行时，Linux 将无法找到此命令的可执行文件，并提示 No such file or directory，示例命令如下：

```
[root@localhost ~]# mv /bin/ls /root
[root@localhost ~]# ls
bash: /bin/ls: No such file or directory
```

 

此时，如果仍想使用 ls 命令，有 2 种方法，一种是直接将 /root 添加到 PATH 环境变量中，例如：

```
[root@localhost ~]# PATH=$PATH:/root
[root@localhost ~]# echo $PATH
/usr/local/sbin:/usr/sbin:/usr/local/bin:/usr/bin:/bin:/root/bin:/root
[root@localhost ~]# ls
Desktop    Downloads    Music    post-install     Public    Videos
Documents  ls           Pictures post-install.org Templates
```

> 注意，这种方式只是临时有效，一旦退出下次再登陆的时候，$PATH 就恢复成了默认值。


另一种方法是以绝对路径的方式使用此命令，例如：

```
[root@localhost ~]# /root/ls
Desktop    Downloads    Music    post-install     Public    Videos
Documents  ls           Pictures post-install.org Templates
```

为了不影响系统的正常使用，强烈建议大家将移动后的 ls 文件还原，命令如下：

```
[root@localhost ~]# mv /root/ls /bin
```

 