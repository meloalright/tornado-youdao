# tornado-youdao    
   
### [vue.js] + [tornado] + [手写orm] + [diff] + [redis] + [websocket] 实现微型的网易云笔记
   
   
   
```python
项目组织结构:

- handler: 存放handler相关逻辑
    base.py  = 基础BaseHandler
    index.py = 首页Handler

- lib
    query.py = 手写的ORM
    (application=>pysqlite3=>conn=>orm)
```
   
`cvt64`   
```python
>>> from lib.cvt64 import *
>>> encvt64(1)
'MQ=='
>>> decvt64('MQ==')
1
```      
   
   
`项目启动`   
`/usr/local/bin/redis-server /etc/redis.conf`   
`python3 init_db.py`   
`python3 application.py`   