# Simple To Do app

<p align="center">
  <a href="https://github.com/j3rrryy/todo_app/actions/workflows/main.yml">
    <img src="https://github.com/j3rrryy/todo_app/actions/workflows/main.yml/badge.svg" alt="СI/CD">
  </a>
  <a href="https://www.python.org/downloads/release/python-3120/">
    <img src="https://img.shields.io/badge/Python-3.12-FFD64E.svg" alt="Python 3.12">
  </a>
  <a href="https://github.com/j3rrryy/todo_app/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
</p>

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

- Copy `.env` file from `examples/` to `docker/` folder fill it in

### :rocket: Start

  ```shell
  docker compose up --build -d
  ```

### :x: Stop

```shell
docker compose stop
```
