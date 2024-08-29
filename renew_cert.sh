#!/bin/bash

cd ./todo_app/
docker compose run --rm -d certbot renew
docker compose exec nginx nginx -s reload
