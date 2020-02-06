#### 怎样创建一个Telegram Bot



##### 什么是Telegram？

​	Telegram是一款优秀的跨平台即时通信软件，官方提供了手机版(Andorid, iOS, Windows Phone)、桌面版(Windows, Mac, Linux)以及网页版。由于一些特殊的原因，在中国大陆上并不能使用Telegram。因此，并不推荐使用Telegram作为日常的通讯工具。

##### 什么是Telegram Bot？

​	顾名思义，Telegram Bot就是Telegram机器人。在2015年6月24日，Telegram正式开始提供[Bot API](https://core.telegram.org/api#bot-api "国内无法访问，访问需要挂代理")。除了Bot API外，Telegram还开放了Telagram APIs，使用Telegram APIs可以开发属于自己的Telegram客户端。



[下载](https://telegram.org/ '点击下载Telegram')对应系统的Telegram，如果不想下载也可以使用[网页版](https://web.telegram.org/ '点击进入Telegram网页版')的Telegram，下面提供的是Windows版本的教程。



##### 一. 准备工作

​	安装好Telegram后打开的样子如下：

<img src="https://mmbiz.qpic.cn/mmbiz_jpg/icOqusCS0aibPkHibOicqjkeyl0GFELxsKfxaJKrHjcTC5keew7XsT4sOaaZ8ibUlUZ10ylVsgia8ibGxVrv4NpbnnibWw/0?wx_fmt=jpeg" alt="img" title="Telegram第一次打开的界面" >

​	如果没有正常的连接到Telegram的服务器左下角会有一个转动的小圆圈，点击小圆圈可以设置代理：

![img](https://mmbiz.qpic.cn/mmbiz_jpg/icOqusCS0aibPkHibOicqjkeyl0GFELxsKfxp9el2r6YPq7fqfrQ9fs1IZ9VUicj6WdPJZfGhzGdib1gKJqC2kthnhgg/0?wx_fmt=jpeg 'Telegram设置代理的界面')

​	翻译一下：

| 原文                        |    翻译后结果    |
| :-: | :-: |
| Try connecting through IPv6 | 尝试使用IPv6连接 |
| Disable proxy               |     关闭代理     |
| Use system proxy settings   |   使用系统代理   |
| Use custom proxy            |  使用自定义代理  |
| Use proxy for calls         | 使用代理进行通信 |


