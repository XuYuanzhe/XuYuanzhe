# Trick 

## Ubuntu

```
date -R     # 查看时区
sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime    # 修正时区
```


## Python

```
uv python list            # 列出安装过的 python 版本
uv python install 3.13    # 安装 python 3.13
uv init . -p 3.13         # 初始化当前文件夹为 3.13 版本
uv init . --package -p 3.13     # 初始化当前文件夹为 3.13 版本 以 python 包的形式
uv add "mcp[cli]"        # 安装 mcp 包
uv build                 # 打包 python 包
```

## Macbook

想让 chrome 在全屏和隐藏工具栏之间来回切换时使用

> Shift + command + f

![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507110912560.png) 

![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507110915659.png)