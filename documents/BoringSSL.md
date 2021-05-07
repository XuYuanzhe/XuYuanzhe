使用boringssl以及curl和nghttp2尝试获取 https://www.galerieslafayette.com/p/clavier+gamer+corsair+k55+rgb-corsair/300405645289/0 的页面内容

以下为研究过程：
首先安装golang的最新版本
编译boringssl

```
$ cd $HOME/src
$ git clone https://boringssl.googlesource.com/boringssl
$ cd boringssl
$ mkdir build
$ cd build
$ cmake -DCMAKE_POSITION_INDEPENDENT_CODE=1 .. 
$ make
```

创建软连接：

```
$ cd ..
$ mkdir lib
$ cd lib
$ ln -s ../build/ssl/libssl.a
$ ln -s ../build/crypto/libcrypto.a
```

从https://curl.haxx.se/download.html 下载源码包，解压并进入源码包根目录中
确保LD_LIBRARY_PATH环境变量中包含 /path/to/curl/tree/lib，且PATH环境变量中包含 /path/to/curl/tree/bin

```
$ echo $LD_LIBRARY_PATH
$ echo $PATH
```

若环境变量中未包含路径，则需要添加至环境变量，并用“ : ”隔开（注意不要覆盖环境变量中原有的路径）

```
$ export LD_LIBRARY_PATH=/path/to/curl/tree/lib
$ export PATH=/path/to/curl/tree/bin
```

`LIBS=-lpthread ./configure --prefix=/path/to/curl/tree --with-ssl=$HOME/src/boringssl`

`make && make install`

输入`which curl` 会提示 `/path/to/curl/tree/bin/curl`
输入`curl --version` 显示 `curl 7.75.0 (x86_64-pc-linux-gnu) libcurl/7.75.0 BoringSSL` 则boringssl已经被编译至curl

研究发现需要支持curl发送http2请求，而从刚才编译的curl信息里可以看到并未支持http2，想要支持http2需要依赖第三方库nghttp2

首先从 https://github.com/nghttp2/nghttp2/releases 下载nghttp2

```
$ tar xf nghttp2-1.43.0.tar.bz2
$ cd nghttp2-1.43.0
$ ./configure
$ make
```

在编译的时候遇到问题需要python3.8以上作为默认python版本才可以继续执行
选择pyenv控制python版本

安装

```
$ git clone git://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l
```

查看可安装的版本

```
$ pyenv install --list
```

选择一个版本安装

```
$ pyenv install 3.8.8 -v
```

更新数据库

```
$ pyenv rehash
```

查看当前已安装的py版本

```
$ pyenv versions
```

设置全局py版本

```
$ pyenv global 3.8.8
```

确认py版本

```
$ python
```

重新编译nghttp2并将boringssl编译进去