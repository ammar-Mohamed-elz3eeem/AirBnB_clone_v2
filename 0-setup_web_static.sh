#!/usr/bin/env bash
# Script to configure nginx server to
# server static content
# - install nginx if it is not installed
# - create folders /data/web_static/releases/test/
# - create folders /data/web_static/shared/
# - create index.html inside /data/web_static/releases/test/
# - with fake html content on it
# - make /data/web_static/current symbolic link to
# 	/data/web_static/releases/test/

sudo apt-get update -y -qq;
sudo apt-get install nginx -y -qq;
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
