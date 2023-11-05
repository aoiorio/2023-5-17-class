# ubuntuの最新バージョンからという意味
FROM ubuntu:latest

# はじめに実行するコマンドたち
RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask

# app folderを作成
RUN mkdir /app
