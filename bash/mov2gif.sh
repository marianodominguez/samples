#!/bin/bash

SRC=$1
DST="${SRC%.mov}.gif"

echo $SRC
echo $DST

mkdir /tmp/gifs
mkdir /tmp/pngs
ffmpeg -i ${SRC} -r 10 /tmp/pngs/out%04d.png
sips -s format gif /tmp/pngs/*.png --out /tmp/gifs
gifsicle /tmp/gifs/*.gif --optimize=3 --colors 256 --delay=10 --loopcount --resize 640x480 > ${DST}
rm -rf /tmp/gifs
rm -rf /tmp/pngs

