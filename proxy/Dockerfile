FROM nginx:stable-alpine

COPY index.html /usr/share/nginx/html/
COPY etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
