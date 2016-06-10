# 外卖订餐系统

本项目是使用前后端分离模式开发的WEB外卖订餐系统。

项目后端使用了Gunicorn + Gevent + Django REST framework，数据库使用Redis和SQLite。

项目前端使用了Foundation, Vuejs, Webpack 和 Gulp等。

# 部署流程
1. 修改hosts文件，加入一行`127.0.0.1   takeout.com`记录
2. 安装nginx，然后在nginx配置中添加以下记录:
server {
    listen 80;

    server_name takeout.com www.takeout.com;

    location /api/ {
        proxy_pass http://localhost:8000/;
    }

    location /customer/ {
        proxy_pass http://localhost:8080/;
    }

    location /business/ {
        proxy_pass http://localhost:8081/;
    }

    location /admin/ {
        proxy_pass http://localhost:8082/;
    }
}
3. 重启nginx
4. 启动后台服务器和前端服务器,后台和前端的启动方法见/backend/README.md和/frontend/README.md
5. API通过takeout.com/api访问，顾客端通过takeout.com/customer访问，商家端通过takeout.com/business访问，管理员端通过takeout.com/admin访问

# License

MIT
