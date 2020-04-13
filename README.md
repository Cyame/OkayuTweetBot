## 小粥烤推BOT开发企划


### 须知：如果您是非企划所涉及人员

本仓库原则上公开源码，提供给更多想要使用CoolQ机器人的各位一个实例

但是个人水平有限，加上本身无意进行扩展，所以很多代码部分都涉及静态

如果您想要修改源码并自行部署使用，本仓库遵循MIT协议，

这意味着您可以在不与作者沟通的前提下，在表明原作者（即本仓库地址）的情况下自行使用

部分静态代码作为文件内全局变量声明，因此大量代码可以作为复用的选择

如果您想增强本仓库可扩展性加以二次开发，请fork本项目，对您的编辑感激不尽

### 如果您是企划所涉及人员或开发者

#### 关于本项目
##### 项目相关文档（待完善）
[工程说明](./project.md)

[Linux/服务器/UNIX上的部署文档](./部署coolQ.md)

[当前开发进度及潜在问题](./progress.md)

[测试文档](./test.md)

[MIT License](./LICENSE.md)

##### 依赖
本项目依赖于[nonebot](https://nonebot.cqp.moe/)与[twint](twintproject)，感谢二位开发者的贡献。

项目内使用定时监控，如需添加nonebot依赖，请使用
`pip install 'nonebot[scheduler]'`
安装相关扩展。

项目的获取由于暂时未申请到推特API，故使用twint爬虫项目
`pip install twint`

关于`\package\monitor.py` 亦可以作为独立模块使用，用于获取近两日更新的推特。
其中`main()`函数将返回(较上次运行)两日内新增推特与近两日完整推特列表，以twitterList类进行封装。
##### 关于API
恕本人才疏学浅，无法提供有效可用的API，大部分模块耦合较高，扩展性并不强。
如想了解所用扩展的完整API,请访问
> [nonebot](https://nonebot.cqp.moe/)
> [twint](twintproject)
