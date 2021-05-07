# Git 工作流规范
版本控制有三种，第一种是本地式版本控制，也就是在本地的硬盘上用数据库记录历代文件；第二种是集中式版本控制，通过一个服务器，多个用户连接到服务器进行文件的记录。而第三种是我们着重介绍的分布式版本控制，它将前两种结合起来，在本地和服务器都建立数据库，每次工作时从服务器克隆（clone）下来，同时又与服务器交互，从而兼顾协同性和安全性。

我们所说的git就是一个分布式版本控制软件，GitHub就是一个git的托管服务。

一. 分支要求
1. feature 分支、bug 修复分支等【具体功能分支】，开发人员自行维护
2. 除非紧急修复线上重大bug，具体功能分支原则上都【不能直接并入 master 主分支】
3. 暂定具体功能分支【都向 dev 分支合并】（1.实现开发者都面向一致的代码环境，2.保护主分支）

二. 新增 Code review 代码复查环节，复查【目标】：
1. 检查 bug，避免 bug 被合并到主分支
2. 代码优化 （包括：代码可读性、变量名易识别等）

三. 复查流程说明：
1. 先由开发者向 dev 分支【提交合并请求】
2. 代码复查人员【复查具体功能分支后】再合并 dev 分支。（避免dev带 bug 干扰其他开发者）
3. 复查完毕，dev 分支合并到主分支，完成合并

-----
其他补充、插件资源：
VScode 编辑器可用 gitlens 插件，便捷对比本地代码版本对比（类似github版本对比）。 
Commit 命名规范
Commit 的命名参照如下格式：
[commit type]: commit title，一句话讲清楚这个 commit 要做什么
commit content，详细说明这个 commit 都有哪些改动

commit type:
- :bugfix：测试、研发过程中发现的 bug
- :hotfix：线上发现的 bug
- :feat：需求迭代
- :refactor：不涉及功能变更的代码重构 
- :doc：文档补充
-  fix: 修改问题
-  refactor: 代码重构
-  docs: 文档修改
-  style: 代码格式修改
-  test: 测试用例修改


分支命名规范
- feature/*
- hotfix/*
- bugfix/*
- refactor/*
- doc/*

>Git神器: https://mp.weixin.qq.com/s/f-sg2KCApKbxxSV6tD-W8w