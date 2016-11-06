#! /bin/bash

sudo apt-get install nginx
x=$(pwd)
cd /var/www/html
sudo wget -nH -p -E -H -k -K https://pybook.rocks/book#/slide0100
cd $x
sudo mv index.html /var/www/html/
sudo mv index.html.orig /var/www/html/
sudo mv editor.css /var/www/html/css/
sudo mv ace_edit.js /var/www/html/js/
