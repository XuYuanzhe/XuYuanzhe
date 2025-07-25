# Github Pages + Jekyll

Jekyll有很多主题可以使用，下面是一些常用的主题：
> https://github.com/topics/jekyll-theme

本人使用的是al-folio主题，主题地址在这里：
> https://github.com/alshedivat/al-folio

## 1. 基于模板创建 Github Pages 仓库

### step1
使用下面的链接创建一个新的仓库：
https://github.com/new?template_name=al-folio&template_owner=alshedivat
注意：仓库名称必须为 `<your-github-username>.github.io` 或 `<your-github-orgname>.github.io`
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251033900.png)


### step2
进入新仓库依次找到 `Settings -> Actions -> General -> Workflow permissions` 授予读写权限
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251038571.png)


### step3
修改 `_config.yml` 文件中的 `url` 和 `baseurl` 字段：
1. 把 url 设置成 `<your-github-username>.github.io`
2. 把 baseurl 设置成空字符串
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251043363.png)


### step4
进入 `Actions -> Deploy site` 等待 `Update_config.yml` 完成从橙黄色变成绿色
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251049557.png)
现在除了 `main` 分支还自动创建了一个 `gh-pages` 分支


### step5
进入 `Settings -> Pages -> Build and deployment` 修改 branch 从 `main` 切换到 `gh-pages` 点击 save 保存


### step6
进入 `Actions -> pages-build-deployment` 等待 `pages-build-deployment` 完成从橙黄色变成绿色
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251058972.png)
进入 `pages-build-deployment` 可以看到网站已经生成了
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507251102553.png)
现在可以 clone 项目到本地进行编辑了
```shell
$ git clone git@github.com:<your-username>/<your-repo-name>.git
```

## 2. 本地编辑

官方建议使用 docker 环境 我这里使用的本地环境

al-folio 的官方文档参考：
> https://github.com/alshedivat/al-folio/blob/main/INSTALL.md

我这里使用 mac 电脑演示

### step1 Ruby
安装 ruby
```shell
brew install ruby
```

查看安装信息
```shell
brew install info
```

执行这个语句将我们自己安装的 ruby 添加到环境变量中（macOS 系统自带 ruby 我们用自己安装）
![](https://raw.githubusercontent.com/XuYuanzhe/Figurebed/master/img/202507241740123.png)

查看 ruby 版本
```shell
ruby -v
```

### step2 Jekyll
安装 jekyll
```shell
gem install --user-install bundler jekyll
```

添加到环境变量中 我这里使用的是 zsh
```shell
echo 'export PATH="$HOME/.gem/ruby/3.4.0/bin/"' >> ~/.zshrc
source ~/.zshrc
```


查看 jekyll 版本
```shell
jekyll -v
```

### step3 Start
进入项目目录
```shell    
cd <your-username>.github.io
```

启动项目
```shell
bundle exec jekyll serve
```

注意：官方模板里支持 RSS 订阅 这可能导致项目无法启动，我的解决方法是注释掉 `_config.yml` 中的 `external_sources` 相关代码

项目启动后可以在浏览器中访问 `http://localhost:4000` 查看效果，修改样式可以实时看到效果。

enjoy ✌︎(ツ)ɔ
