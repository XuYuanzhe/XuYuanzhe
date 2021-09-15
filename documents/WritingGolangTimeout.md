当然，go语言的超时控制肯定不止4种方法，起这个标题是自嘲，让我想起了孔乙己说的茴香的茴有4种写法。

以下的4种方式都借助于同一个套路：

    workDoneCh := make(chan struct{}, 1)
    go func() {
        LongTimeWork()  //这是我们要控制超时的函数
        workDoneCh <- struct{}{}
    }()
     
    select { //下面的case只执行最早到来的那一个
    case <-workDone: //LongTimeWork运行结束
        fmt.Println("LongTimeWork return")
    case <-timeoutCh:    //timeout到来
        fmt.Println("LongTimeWork timeout")
    }

比如我们希望100ms超时，那么100ms之后<-timeoutCh这个读管道的操作需要解除阻塞，而解除阻塞有2种方式，要么有人往管道里写入了数据，要么管道被close了。下面的4种方法就围绕<-timeoutCh如何解除阻塞展开。

式一：

这种方式最简单直接

    timeoutCh := make(chan struct{}, 1)
    go func() {
        time.Sleep(100 * time.Millisecond)
        timeoutCh <- struct{}{}
    }()

式二：

不需要像方式一那样显式地创建一个timeoutCh管道，借助于time.After(duration)，这个函数会返回一个管道，并且经过一段时间duration后它还会自动向管道send一个数据。

    select { //下面的case只执行最早到来的那一个
    case <-workDone: //LongTimeWork运行结束
        fmt.Println("LongTimeWork return")
    case <-time.After(100 * time.Millisecond):   //timeout到来
        fmt.Println("LongTimeWork timeout")
    }

比式一优雅简洁了不少。　

式三：

go语言Context是一个接口，它的Done()成员方法返回一个管道。

    type Context interface {
        Deadline() (deadline time.Time, ok bool)
        Done() <-chan struct{}
        Value(key interface{}) interface{}
    }

cancelCtx是Context的一个具体实现，当调用它的cancle()函数时，会关闭Done()这个管道，<-Done()会解除阻塞。

    ctx, cancel := context.WithCancel(context.Background())
    go func() {
        time.Sleep(100 * time.Millisecond)
        cancel()
    }()
    select { //下面的case只执行最早到来的那一个
    case <-workDone:
        fmt.Println("LongTimeWork return")
    case <-ctx.Done(): //ctx.Done()是一个管道，调用了cancel()都会关闭这个管道，然后读操作就会立即返回
        fmt.Println("LongTimeWork timeout")
    }

式四：

跟式三类似，timerCtx也是Context的一个具体实现，当调用它的cancle()函数或者到达指定的超时时间后，都会关闭Done()这个管道，<-Done()会解除阻塞。

    ctx, _ := context.WithTimeout(context.Background(), time.Millisecond*100)
    select { //下面的case只执行最早到来的那一个
    case <-workDone:
        fmt.Println("LongTimeWork return")
    case <-ctx.Done(): //ctx.Done()是一个管道，context超时或者调用了cancel()都会关闭这个管道，然后读操作就会立即返回
        fmt.Println("LongTimeWork timeout")
    }

我在腾讯课堂开设了一门**9.9元**的Go语言的实战课《[Go语言实现工业级搜索引擎](https://link.zhihu.com/?target=https%3A//ke.qq.com/course/3617680)》，欢迎过来一起交流。

总体来看，式二和式四的代码量是最少的。最后附上完整代码：

    package main
     
    import (
        "context"
        "fmt"
        "time"
    )
     
    const (
        WorkUseTime = 500 * time.Millisecond
        Timeout     = 100 * time.Millisecond
    )
     
    //模拟一个耗时较长的任务
    func LongTimeWork() {
        time.Sleep(WorkUseTime)
        return
    }
     
    //模拟一个接口处理函数
    func Handle1() {
        deadline := make(chan struct{}, 1)
        workDone := make(chan struct{}, 1)
        go func() { //把要控制超时的函数放到一个协程里
            LongTimeWork()
            workDone <- struct{}{}
        }()
        go func() { //把要控制超时的函数放到一个协程里
            time.Sleep(Timeout)
            deadline <- struct{}{}
        }()
        select { //下面的case只执行最早到来的那一个
        case <-workDone:
            fmt.Println("LongTimeWork return")
        case <-deadline:
            fmt.Println("LongTimeWork timeout")
        }
    }
     
    //模拟一个接口处理函数
    func Handle2() {
        workDone := make(chan struct{}, 1)
        go func() { //把要控制超时的函数放到一个协程里
            LongTimeWork()
            workDone <- struct{}{}
        }()
        select { //下面的case只执行最早到来的那一个
        case <-workDone:
            fmt.Println("LongTimeWork return")
        case <-time.After(Timeout):
            fmt.Println("LongTimeWork timeout")
        }
    }
     
    //模拟一个接口处理函数
    func Handle3() {
        //通过显式sleep再调用cancle()来实现对函数的超时控制
        ctx, cancel := context.WithCancel(context.Background())
     
        workDone := make(chan struct{}, 1)
        go func() { //把要控制超时的函数放到一个协程里
            LongTimeWork()
            workDone <- struct{}{}
        }()
     
        go func() {
            //100毫秒后调用cancel()，关闭ctx.Done()
            time.Sleep(Timeout)
            cancel()
        }()
     
        select { //下面的case只执行最早到来的那一个
        case <-workDone:
            fmt.Println("LongTimeWork return")
        case <-ctx.Done(): //ctx.Done()是一个管道，调用了cancel()都会关闭这个管道，然后读操作就会立即返回
            fmt.Println("LongTimeWork timeout")
        }
    }
     
    //模拟一个接口处理函数
    func Handle4() {
        //借助于带超时的context来实现对函数的超时控制
        ctx, cancel := context.WithTimeout(context.Background(), Timeout)
        defer cancel() //纯粹出于良好习惯，函数退出前调用cancel()
        workDone := make(chan struct{}, 1)
        go func() { //把要控制超时的函数放到一个协程里
            LongTimeWork()
            workDone <- struct{}{}
        }()
        select { //下面的case只执行最早到来的那一个
        case <-workDone:
            fmt.Println("LongTimeWork return")
        case <-ctx.Done(): //ctx.Done()是一个管道，context超时或者调用了cancel()都会关闭这个管道，然后读操作就会立即返回
            fmt.Println("LongTimeWork timeout")
        }
    }
     
    func main() {
        Handle1()
        Handle2()
        Handle3()
        Handle4()
    }