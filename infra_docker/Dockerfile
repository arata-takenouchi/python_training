FROM python:3.6.9-slim-buster

RUN apt-get update 
RUN apt-get install -y vim
RUN apt-get install -y ssh sshpass openssh-server iputils-ping 
RUN apt-get install -y ssh wget net-tools curl
RUN echo "root:root" | chpasswd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN apt-get -y install build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev cargo
RUN pip3 install --upgrade pip
RUN pip3 install Fabric==1.14.0
RUN pip3 install Fabric3==1.14.post1
RUN pip3 install ansible==2.4.2.0
RUN pip3 install cryptography==36.0.0

ENTRYPOINT service ssh restart && tail -f /dev/null
