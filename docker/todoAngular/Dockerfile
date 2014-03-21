FROM mariano/centos_updated

RUN yum update


RUN     rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

RUN	yum install -y npm

#mount source directory

ADD . /src
RUN cd /src; npm install

EXPOSE 8080

#add user

CMD ["node", "/src/index.js"]
