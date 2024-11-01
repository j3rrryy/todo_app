# Simple To Do app

## :book: Key features

- Token authentication (Djoser)
- Easy management of your tasks

## :page_with_curl: API

|Method|URL|Headers|Body|Description|
|:-:|:-:|:-:|:-:|:-:|
|`POST`|`/api/v1/auth/users/`|`-`|`email`, `username`, `password`|Register a new user|
|`POST`|`/api/v1/auth/token/login/`|`-`|`username`, `password`|Obtain the user authentication token|
|`GET`|`/api/v1/auth/users/me/`|`Authorization: Token <user_token>`|`-`|Get the user data|
|`POST`|`/api/v1/auth/users/set_username/`|`Authorization: Token <user_token>`|`new_username`, `current_password`|Change the username|
|`POST`|`/api/v1/auth/users/set_password/`|`Authorization: Token <user_token>`|`new_password`, `current_password`|Change the user password|
|`POST`|`/api/v1/auth/token/logout/`|`Authorization: Token <user_token>`|`-`|Logout the user (remove the user authentication token)|
|`DELETE`|`/api/v1/users/me/`|`Authorization: Token <user_token>`|`current_password`|Delete the user|
|`GET`|`/api/v1/tasks/`|`Authorization: Token <user_token>`|`-`|Get the user tasks|
|`POST`|`/api/v1/tasks/`|`Authorization: Token <user_token>`|`title`, `description` (str, default=blank), `priority` (float [0; 1], default=1), `completed` (bool, default=False)|Post a new task|
|`GET`|`/api/v1/tasks/<task_id>/`|`Authorization: Token <user_token>`|`-`|Get the task|
|`PATCH`|`/api/v1/tasks/<task_id>/`|`Authorization: Token <user_token>`|Any key (`title` / `description` / `priority` / `completed`)|Update the task|
|`DELETE`|`/api/v1/tasks/<task_id>/`|`Authorization: Token <user_token>`|`-`|Delete the task|

## :computer: Requirements

- Docker

## :hammer_and_wrench: Getting started

- Copy `.env.dev` file from `examples/docker/env/` to `docker/env/` folder fill it in

- **(For prod)** Copy `.env.prod` file from `examples/docker/env/` to `docker/env/` folder and fill it in

- **(For prod)** Copy `nginx.conf` file from `examples/docker/nginx/prod/` to `docker/nginx/prod` folder and fill it in

- **(For prod)** Copy `docker-compose.yml` file from `examples/` to `/` folder and fill it in

### :rocket: Start

- Run the **dev build**

  ```shell
  docker compose -f docker-compose.dev.yml up --build -d
  ```

- Run the **prod build** and get a SSL certificate

  - Build the project

    ```shell
    docker compose build
    ```

  - Start Docker and get a certificate

    ```shell
    docker compose up nginx certbot
    ```

  - Stop your containers to continue

    ```shell
    docker compose stop
    ```

  - Comment out the command in `docker-compose.yml`

    ```shell
    command: certonly --webroot --webroot-path=/var/www/certbot/ --email <your_email> --agree-tos --no-eff-email -d <domain (example.com)> -d <domain (www.example.com)>
    ```

  - Uncomment the part of nginx config in `docker/nginx/prod/django.conf`

  - Start Docker again

    ```shell
    docker compose up -d
    ```

  - Run the setup script

    ```shell
    bash setup.sh
    ```

### :x: Stop

```shell
docker compose stop
```
