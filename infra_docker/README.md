上級者向けになりますが、Mac M1チープをお使いの方はVirtal boxが使用できませんので、以下のようにdockerを用いて実行することも可能です。

1. Dockerをインストールしてください

https://docs.docker.com/get-docker/

2. Docker composeをインストールしてください
https://docs.docker.jp/compose/install.html

3. Dockerをbuildしてください
docker build -t main .
docker build -t server1 .
docker build -t server2 .

4. Dockerを立ち上げてください
docker-compose up


5. Dockerの状態を確認してください
docker ps

CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                     NAMES
f793d2a21324   server1:latest   "/bin/sh -c 'service…"   10 minutes ago   Up 10 seconds   0.0.0.0:52184->1342/tcp   server1
0314b8ae9edc   main:latest      "/bin/sh -c 'service…"   10 minutes ago   Up 10 seconds   0.0.0.0:52183->1342/tcp   main
735d25fe5c03   server2:latest   "/bin/sh -c 'service…"   10 minutes ago   Up 10 seconds   0.0.0.0:52182->1342/tcp   server2

6. Docker mainにログインしてください
docker exec -it main bash

7. Dockerにはip addressではなく、hostnameで他のサーバーにsshできますので、ip addressではなく、以下のようにserver1としてログインしてください。
ssh root@server1
