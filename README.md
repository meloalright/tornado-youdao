# tornado-youdao    
   
### [vue.js] + [tornado] + [手写orm] + [diff] + [redis] + [websocket] 实现微型的网易云笔记
   
   
   
```python
项目组织结构:

- db:
    youdao.db

+ diff-note: diff算法测试用例

- handler: 存放handler相关逻辑
    api.py  = 笔记相关API
    base.py  = 基础BaseHandler
    history.py = 版本记录Handler
    home.py = Home页Handler
    index.py = 首页Handler
    note.py = 笔记页Handler(spa)
    signup.py = 注册页Handler
    usi.py = 用户注册登录相关Api

- lib
    cvt64.py = 手动封装的一个base64转换
    diff.py = 手写的diff算法
    loader.py = 引用来自F2E.im项目的动态引入库
    query.py = 手写的ORM
    security.py = 引用来自Google的bcrypt封装函数

- note
	note.py = 笔记类的方法
	user.py = 用户类的方法

+ my-project: vue项目文件

+ templates: 模板目录

application.py: 入口文件

diff_demo.py: diff算法调用示例

init_db.py: 初始化数据库

mv.sh: shell脚本 = 迁移vue-build文件至模板目录的脚本

```
   
   
`cvt64`   
```python
>>> from lib.cvt64 import *
>>> encvt64(1)
'MQ=='
>>> decvt64('MQ==')
1
```      
   
   
`diff算法`
```
['+ @0 完整版\n', '\n', '- @2 煮豆燃豆萁\n', '+ @2 煮豆持作羹\n', '+ @2 漉菽以为汁\n', '+ @2 萁在釜下燃\n', '豆在釜中泣\n', '- @4 本是同根生\n', '+ @4 本自同根生\n', '相煎何太急\n', '\n', '曹植']
[[{'pos': 0, 'type': '+', 'str': '完整版\n'}], [], [{'pos': 2, 'type': '-', 'str': '煮豆燃豆萁\n'}, {'pos': 2, 'type': '+', 'str': '煮豆持作羹\n'}, {'pos': 2, 'type': '+', 'str': '漉菽以为汁\n'}, {'pos': 2, 'type': '+', 'str': '萁在釜下燃\n'}], [], [{'pos': 4, 'type': '-', 'str': '本是同根生\n'}, {'pos': 4, 'type': '+', 'str': '本自同根生\n'}], [], [], [], []]
[[{'pos': 0, 'type': '-', 'str': '七步诗\n'}, {'pos': 0, 'type': '+', 'str': '情绪版\n'}, {'pos': 0, 'type': '+', 'str': '七步诗~\n'}], [], [], [], [{'pos': 4, 'type': '-', 'str': '本是同根生\n'}, {'pos': 4, 'type': '+', 'str': '本是同根生!!\n'}, {'pos': 4, 'type': '+', 'str': '相煎何太急?!\n'}], [{'pos': 5, 'type': '-', 'str': '相煎何太急\n'}], [], [{'pos': 7, 'type': '-', 'str': '曹植'}, {'pos': 7, 'type': '+', 'str': '曹植~'}], []]
======merge======
完整版
情绪版
七步诗~

煮豆持作羹
漉菽以为汁
萁在釜下燃
豆在釜中泣
-CONFLCIT-
source:本是同根生
-本是同根生
+本自同根生
-本是同根生
+本是同根生!!
+相煎何太急?!
--------

曹植~
```   
   
   
`项目启动`   
`/usr/local/bin/redis-server /etc/redis.conf`   
`python3 init_db.py`   
`python3 application.py`   