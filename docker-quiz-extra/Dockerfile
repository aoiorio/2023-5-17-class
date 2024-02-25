FROM node:6
FROM mysql:8.0

EXPOSE 8888
COPY init.sql /docker-entrypoint-initdb.d/init.sql
ENV MYSQL_ROOT_PASSWORD=root
VOLUME ./db_data:/var/lib/mysql

RUN pip3 install mysql
FROM ubuntu:latest

# excute commands by using apt-get
RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask

RUN mkdir /app