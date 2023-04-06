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

function install() {
	command -v "$1" > /dev/null;

	if [[ $EXITCODE -ne 0 ]]; then
		sudo apt-get update -y -qq;
		sudo apt-get install "$1" -y -qq;
	fi;
}

install nginx

sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

html=\
"
<html>
  <head>
  </head>
  <body>
    Hello From static side
  </body>
</html>
"

echo "$html" | sudo dd status=none of=/data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_nginx=\
"
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        server_name _;

        add_header X-Served-By \$hostname;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }

        rewrite ^/redirect_me$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

		location /hbnb_static { 
			alias /data/web_static/current; 
		}

        error_page 404 /error_404.html;

        location = /error_404.html {
                internal;
        }
}
"

echo "$config_nginx" | sudo dd status=none of=/etc/nginx/sites-enabled/default
