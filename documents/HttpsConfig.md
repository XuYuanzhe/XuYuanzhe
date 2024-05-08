# Nginx编译与安装以及自签名SSL证书生成与配置

## 环境准备
Linux环境：CentOS 7.6

## Nginx的编译与安装
### 依赖包下载
- 安装gcc环境
```
yum install -y gcc-c++
```
- openssl下载解压
```
cd /home/
wget https://www.openssl.org/source/openssl-1.1.1n.tar.gz
tar -zxvf  openssl-1.1.1n.tar.gz 
```
- pcre下载解压
cd /home/
```
wget https://github.com/PCRE2Project/pcre2/releases/download/pcre2-10.39/pcre2-10.39.tar.gz
tar -zxvf pcre2-10.39.tar.gz
```
- zlib下载解压
```
cd /home/
wget https://github.com/madler/zlib/archive/refs/tags/v1.2.11.tar.gz
tar -zxvf v1.2.11.tar.gz
```
- nginx headers-more-nginx-module下载解压
```
cd /home/
wget https://github.com/openresty/headers-more-nginx-module/archive/refs/tags/v0.33.tar.gz
tar -zxvf v0.33.tar.gz
```
- 安装GeoIP库
```
yum install -y GeoIP-devel.x86_64
```

### Nginx编译安装
```
cd /home/
wget https://nginx.org/download/nginx-1.21.6.tar.gz 
tar -zxvf nginx-1.21.6.tar.gz && cd nginx-1.21.6 && ./configure --prefix=/home/nginx --with-pcre=/home/pcre2-10.39 --with-zlib=/home/zlib-1.2.11 --with-openssl=/home/openssl-1.1.1n --add-module=/home/headers-more-nginx-module-0.33 --with-stream --with-stream_ssl_module --with-http_gzip_static_module --with-http_stub_status_module --with-http_ssl_module --with-http_mp4_module --with-http_flv_module --with-http_v2_module --with-file-aio --with-http_geoip_module --with-stream && make && make install
```

## openssl自签名生成私钥和证书
```
root@yunzhi-virtual-machine:/home/yunzhi# mkdir /home/nginx-certs
root@yunzhi-virtual-machine:/home/yunzhi# cd /home/nginx-certs/
root@yunzhi-virtual-machine:/home/nginx-certs# openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /home/nginx-certs/www.yunzong.com.key -out /home/nginx-certs/www.yunzong.com.crt
......+...+.........+...+.....+.+.....+....+...+.....+...+.+...+..+....+.....+......+.........+......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+......+..+.......+.....+.........+.+...+...........+......+.+............+..+..........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+........+...+....+......+......+...+.....+.......+......+..+...+............+......+.+......+.....+.........+.+.....+.......+.....+...+.......+...+...+......+.....+....+.....+.+....................+.+..................+..+...+..........+..+............+.......+......+........+.+...+......+............+...+..+...+.+........+..........+..+.............+..+...+.+..............+.......+.........+..............+.+...........+......+...+.+...+.....+.............+...+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
....+..+....+..+....+...+.....+...+..........+........+.+...+..+...+.+............+..+..........+..+...+...+.......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*........+.+...+..+...+...+...+....+...+...............+..+...+.......+.....+.+..+.......+...+..+...+.............+......+......+.....+.......+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.....+......+.+........+................+...+.....+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CN
State or Province Name (full name) [Some-State]:HeNan
Locality Name (eg, city) []:ZhengZhou
Organization Name (eg, company) [Internet Widgits Pty Ltd]:demo
Organizational Unit Name (eg, section) []:demo
Common Name (e.g. server FQDN or YOUR name) []:www.yunzong.com
Email Address []:12345@qq.com
root@yunzhi-virtual-machine:/home/nginx-certs# ll
总计 16
drwxr-xr-x 2 root root 4096  4月 25 18:04 ./
drwxr-xr-x 7 root root 4096  4月 25 18:01 ../
-rw-r--r-- 1 root root 1424  4月 25 18:04 www.yunzong.com.crt
-rw------- 1 root root 1704  4月 25 18:03 www.yunzong.com.key
root@yunzhi-virtual-machine:/home/nginx-certs# cd /etc/nginx/
root@yunzhi-virtual-machine:/etc/nginx# ll
total 8
-rw-r--r-- 1 root root 1424  4月 25 18:04 www.yunzong.com.crt
-rw------- 1 root root 1704  4月 25 18:03 www.yunzong.com.key
```

## 配置并启动nginx
修改nginx.conf配置
```
cd /home/nginx/conf
vim nginx.conf
```
配置示例如下
```
user root;
worker_processes  1;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    client_max_body_size 1024m;
    keepalive_timeout  65;

    server {
        listen 443 ssl;
        server_name  localhost;
        ssl_certificate /home/nginx-certs/www.yunzong.com.crt;
        ssl_certificate_key /home/nginx-certs/www.yunzong.com.key;
        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        # 指定密码为openssl支持的格式
        ssl_protocols  SSLv2 SSLv3 TLSv1.2;

        ssl_ciphers  HIGH:!aNULL:!MD5;  # 密码加密方式
        ssl_prefer_server_ciphers  on;   # 依赖SSLv3和TLSv1协议的服务器密码将优先于客户端密码

        location / {
            root   /home/workspace/dist/user_dist;
            try_files $uri $uri/ /index.html;
            index  index.html index.htm;
        }
        
        location /system/ {
            proxy_set_header X-Forward-For $remote_addr;
            proxy_set_header X-real-ip $remote_addr;
            proxy_set_header X-Appengine-Remote-Addr $remote_addr;
            proxy_pass http://127.0.0.1:20201/;
            proxy_set_header Host $host:20201;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For  $proxy_add_x_forwarded_for;
            proxy_set_header HTTP_X_FORWARDED_FOR $remote_addr;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Origin "";
            proxy_read_timeout 7200s;
        }

        location /captcha {
                proxy_pass http://127.0.0.1:20201/captcha;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
                root html;
        }
    }
}
```

## 解决 nginx 配置证书后无法访问 websocket
nginx 默认情况下只允许 HTTP 和 HTTPS 协议，而 websocket 需要使用 wss 或 ws 协议。

- 前端使用 HTTPS 则 WebSocket 必须要使用 wss 协议
```
const host = envConfig.get(process.env.UMI_ENV).split('https://')[1]
const url = `wss://${host}/system/ws`
```

- 在 nginx 中配置专门的路由
```
location /system/ws {
            proxy_pass http://localhost:20201;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
```