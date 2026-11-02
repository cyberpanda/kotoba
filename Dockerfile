# Kotoba web server image:  docker build -t kotoba . && docker run -p 8080:80 kotoba
FROM python:3.12-alpine AS build
WORKDIR /app
COPY package.json ./
COPY src ./src
COPY tools/build.py ./tools/build.py
COPY deploy ./deploy
RUN python3 tools/build.py

FROM nginx:1.27-alpine
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/web /var/www/kotoba
EXPOSE 80
HEALTHCHECK CMD wget -qO- http://localhost/version.json || exit 1
