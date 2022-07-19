# yamdb_final

![example workflow](https://github.com/Konstantin8891/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание:
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.


## Ключевые функции:

- Работа с категориями (получение, создание, удаление)
- Работа с жанрами (получение, создание, удаление)
- Работа с произведениями (получение, создание, обновление, удаление)
- Работа с ревью (получение, создание, обновление, удаление)
- Работа с комментариями (получение, создание, обновление, удаление)
- Работа с пользователями (получение, создание, обновление, удаление)
- Создание, обновление и проверка JWT authentication токенов пользователей
- Для детального описания функционала API применена библиотека   [Redoc](https://github.com/Redocly/redoc)

## Минимальные требования:

Установка Docker 

Выполните установку docker для вашей операционной системы согласно инструкции на официальном сайте https://docs.docker.com/desktop/

### Windows

- Убедитесь, что ваша версия Windows соответствует минимальным требованиям:

Windows 11 64-bit: Home или Pro version 21H2 или выше или Enterprise или Education version 21H2 или выше.

Windows 10 64-bit: Home или Pro 21H1 (build 19043) или выше или Enterprise или Education 20H2 (build 19042) или выше.

- Убедитесь, что ваш ПК соответствует минимальным требованиям:

64-битный процессор с поддержкой SLAT

4 Гб ОЗУ

- Убедитесь, что в биос включена виртуализация

- Установите WSL 2 из терминала

wsl --install

- Проверьте установку 

wsl -l -v

- Скачайте и установите пакет обновления ядра Linux

https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

- Установите Docker Desktop

https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe

- Запустите Docker Desktop

### Ubuntu

Убедитесь, что ваш ПК соответствует минимальным требованиям:

- 64-битное ядро и CPU с поддержкой виртуализации

- поддержка KVM виртуализации. Откройте терминал и введите

modprobe kvm_intel # для процессоров Intel

modprove kvm_amd # для процессоров AMD

- QEMU версии 5.2 или выше
- система инициализации systemd
- графическое окружение Gnome или KDE 
- 4 ГБ ОЗУ
- установите curl

sudo apt install curl

- скачайте скрипт для установки docker

curl -fsSL https://get.docker.com -o get-docker.sh

- запустите скрипт

sh get-docker.sh

- удалите старые версии файлов

sudo apt remove docker docker-engine docker.io containerd runc 

- обновите список пакетов

sudo apt update

- установите пакеты для загрузки через https

sudo apt install \\
  
  apt-transport-https \\
  
  ca-certificates \\
  
  curl \\
  
  gnupg-agent \\
  
  software-properties-common -y 
  
- добавьте ключ gpg

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

- добавьте репозиторий Docker в пакеты

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 

- обновите индекс пакетов

sudo apt update

- установите docker и docker-compose

sudo apt install docker docker-compose -y 

- проверьте статус установки

sudo systemctl status docker 

## Шаблон env-файла

Secret - секрет Джанго

Данные БД Postgres: 

DB_ENGINE - движок postgres

DB_NAME - имя БД

POSTGRES_USER - пользователь БД

POSTGRES_PASSWORD - пароль БД

DB_HOST - название сервиса (контейнера)

DB_PORT - порт для подключения к БД 

## Запуск контейнеров:
Перед началом установки перейдите на компьютере в директорию с файлом docker-compose.yaml.

### 1. Клонируйте проект:
```sh
git@github.com:Konstantin8891/yamdb_final.git
```
### 2. Разверните проект:
```sh
docker-compose up -d
```
### 3. Создать суперпользователя:
```sh
docker-compose exec web python manage.py createsuperuser
```
### 4. Импорт базы данных:
```sh
docker-compose exec web python manage.py dumpdata > дамп_бд.json
```

## Примеры запросов:
> Полный перечень возможных запросов и ответов можно посмотреть после установки и запуска API на локальной машине по ссылке `http://127.0.0.1:8000/redoc/#tag/api`

Алгоритм регистрации пользователей
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт /api/v1/auth/signup/.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт /api/v1/auth/token/, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт /api/v1/users/me/ и заполняет поля в своём профайле (описание полей — в документации).

Пользовательские роли
Аноним — может просматривать описания произведений, читать отзывы и комментарии.
Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
Суперюзер Django — обладет правами администратора (admin)


### 1.`post` Добавление новой категории эндпоинт `api/v1/categories/`:
>Права доступа: Администратор.
```sh
{
    "name": "string",
    "slug": "string"
}
```
Пример успешного ответа:
```sh
{
    "name": "string",
    "slug": "string"
}
```
### 2.`get` Получение списка всех жанров эндпоинт `api/v1/genre/`:
>Права доступа: Доступно без токена.
Пример успешного ответа:
```sh
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": []
    }
]
```
### 3. `post` Добавление произведения эндпоинт `api/v1/titles/`:
>Права доступа: Администратор.
```sh
{
    "name": "string",
    "year": 0,
    "description": "string",
    "genre": [
        "string"
    ],
    "category": "string"
}
```
Пример успешного ответа:
```sh
{
    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": [
        {}
    ],
    "category": {
        "name": "string",
        "slug": "string"
    }
}
```
### 4. `post` Добавление нового отзыва эндпоинт `api/v1/titles/{title_id}/reviews/`:
>Права доступа: Аутентифицированные пользователи.
```sh
{
    "text": "string",
    "score": 1
}
```
Пример успешного ответа:
```sh
{
    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"
}
```
### 5. `post` Добавление комментария к отзыву эндпоинт `api/v1/titles/{title_id}/reviews/{review_id}/comments/`:
>Права доступа: Аутентифицированные пользователи.
```sh
{
    "text": "string"
}
```
Пример успешного ответа:
```sh
{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
```
### 6. `get` Получение списка всех пользователей эндпоинт `api/v1/users/`:
>Права доступа: Администратор.
Пример успешного ответа:
```sh
[
    {
        "count": 0,
        "next": "string",
        "previous": "string",
        "results": [
            {
                "username": "string",
                "email": "user@example.com",
                "first_name": "string",
                "last_name": "string",
                "bio": "string",
                "role": "user"
            }
        ]
    }
]
```
### 7. `post` Регистрация нового пользователя эндпоинт `api/v1/auth/signup/`:
>Права доступа: Доступно без токена.
```sh
{
    "email": "string",
    "username": "string"
}
```
Пример успешного ответа:
```sh
{
    "email": "string",
    "username": "string"
}
```

## Данные разработчиков:

- Владимирский Игорь [GitHub профиль](https://github.com/letulip)
- Ахметжанов Ильдар [GitHub профиль](https://github.com/ma9or)
- Васильев Константин [GitHub профиль](https://github.com/Konstantin8891)
