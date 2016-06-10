# 介绍

项目后端使用了Gunicorn + Gevent + Django REST framework，数据库使用Redis和SQLite。

# 运行环境

先安装好Redis, Python2.7, PIP
然后执行pip install -r requirements.txt安装相关依赖

# 如何启动

```bash
python manage.py makemigrations
python manage.py migrate
sh run.sh
```

# 目录说明

源代码放在takeout中，lib存放公用的模块，admin对应的是管理员后台，bussiness对应的是商家版，customer对应的是顾客版
