#!/bin/bash
sudo docker stop minecraft_server
sudo docker rm minecraft_server
sudo docker pull mariano/minecraft_server

sudo docker run -d -p 25565:25565 \
  -v /home/minecraft/config:/home/minecraft/config \
  --name=minecraft_server mariano/minecraft_server 
