FROM ubuntu:14.04
RUN apt-get -qq update && apt-get -qq install wget
ENV HOME=/home/minecraft
RUN useradd -s /bin/bash -d ${HOME} minecraft
RUN mkdir -p ${HOME}/server

WORKDIR ${HOME}
RUN wget --quiet --no-check-certificate --no-cookies \
  --header "Cookie: oraclelicense=accept-securebackup-cookie" \
  http://download.oracle.com/otn-pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz && \
  tar -xzf jdk-8u101-linux-x64.tar.gz && mv jdk1.8.0_101 java && rm jdk-8u101-linux-x64.tar.gz
RUN wget --quiet https://s3.amazonaws.com/Minecraft.Download/versions/1.10.2/minecraft_server.1.10.2.jar -O ./server/minecraft_server.jar
ENV JAVA_HOME=${HOME}/java
ENV PATH=$PATH:$JAVA_HOME/bin
RUN echo "eula=true" > ${HOME}/server/eula.txt
ADD jars/ server
ADD config/ server
RUN chown -R minecraft ${HOME}

USER minecraft

WORKDIR ${HOME}/server
CMD $JAVA_HOME/bin/java -Xms1024M -Xmx1024M -jar ${HOME}/server/minecraft_server.jar -nogui
