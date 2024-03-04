server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By <%= @hostname %>;
    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        try_files $uri $uri/ =404;
    }
}

