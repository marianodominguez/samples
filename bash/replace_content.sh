#!/bin/bash

awk 'BEGIN {getline l < "contents.txt"}/#CONTENT_REPLACE/{gsub("#CONTENT_REPLACE",l)}1' templ.txt 
