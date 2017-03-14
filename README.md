# tornado-youdao    
   
### [vue.js] + [tornado] + [django] + [redis] 实现微型的网易云笔记   
   
   
   
```python
项目组织结构:

- handler: 存放handler相关逻辑
    base.py  = 基础BaseHandler
    index.py = 首页Handler

- lib
    query.py = 手写的ORM
    (application-db=>orm=>handler-logic)
```