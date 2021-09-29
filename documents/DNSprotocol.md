# DNS

## DNS协议

> DNS是域名系统（Domain Name System）的简称，因特网上作为域名和IP地址相互映射的一个分布式数据库，能够使用户更方便的访问互联网，而不用去记住能够被机器直接读取的IP地址。

以访问www.baidu.com为例，看下DNS会进行哪些操作：

<font color=#00fcff>主机名</font>.<font color=#00d100>次级域名</font>.<font color=#ff6827>顶级域名</font>.<font color=#0052ff>根域名</font>

<font color=#00fcff>www</font>.<font color=#00d100>baidu</font>.<font color=#ff6827>com</font>.<font color=#0052ff>root</font>


1. 首先查找电脑上的DNS缓存列表，如果有记录，那么直接返回对于IP地址，否则进行下一步；
2. 查找电脑上的HOST文件的映射关系，如果有记录，那么返回对于IP地址，否则进行下一步；
3. 查找互联网线路供应商的本地DNS服务器（即中国电信、中国移动或中国联通），本地DNS服务器先查找自己的缓存记录，如果有记录，那么返回对于IP地址，否则本地DNS服务器向根域名服务器发生请求；
4. 根域名服务器收到请求后，查看是.com顶级域名，于是返回.com顶级域名服务器的IP地址给到本地DNS服务器；
5. 本地DNS服务器收到回复后，向.com顶级域名服务器发起请求；
6. .com顶级域名服务器收到请求后，查看是.baidu.com次级域名，于是返回.baidu.com次级域名服务器的IP地址给到DNS服务器；
7. 本地DNS服务器收到回复后，向.baidu.com次级域名服务器发起请求；
8. .baidu.com次级域名服务器收到请求后，查看是自己管理的域名，于是查看域名和IP地址映射表，把www.baidu.com的IP地址返回给本地DNS服务器；
9. 本地DNS服务器收到回复后，向电脑回复域名对应IP地址，并把记录写入本地DNS服务器的缓存里；
10. 电脑收到回复后，使用IP地址访问网站，并把记录写入电脑DNS缓存中。

![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/20210929095944.png)

DNS缓存可以提高查询效率，但是当域名和IP地址映射关系发生变化时，或者缓存的IP地址对应的服务器故障时，使用DNS缓存就不能正常访问网站了，因此DNS缓存默认也是有时间限制的。

## DNS代理

> DNS代理（DNS Proxy）用于在DNS Client和DNS Server之间转发DNS请求和应答报文。局域网内的DNS Client把DNS Proxy当作DNS Server，将DNS请求报文发送给DNS Proxy。DNS Proxy将该请求报文转发至DNS Server，并将DNS Server的应答报文返回给DNS Client，从而实现域名解析。

使用DNS Proxy功能后，当DNS Server的地址发生变化时，只需改变DNS Proxy上的配置，无需改变局域网内每个DNS Client的配置，从而简化了网络管理。

## DNS劫持

> DNS劫持，是把目标网站域名解析到错误的IP地址上。这时可以把DNS地址设置成运营商提供的IP地址，或者设置成公共DNS服务器IP地址。就像买衣服一样的，去商场买名牌，尽量不去买质量和服务都不靠谱的地摊货。