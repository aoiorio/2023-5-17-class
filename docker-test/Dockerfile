# 一番最初に実行するコマンドたち
FROM node:6
# mysql のversion 8.0から読み込む
FROM mysql:8.0

EXPOSE 8888
COPY init.sql /docker-entrypoint-initdb.d/init.sql
# mysqlに入るためのパスワードをrootにしている
ENV MYSQL_ROOT_PASSWORD=root
VOLUME ./db_data:/var/lib/mysql

# I have a yellow error of below code
ENTRYPOINT ['/bin/bash']