![foodgram workflow](https://github.com/TimofeiLytkin/foodgram-project/workflows/foodgram%20workflow/badge.svg)
# foodgram-project
### Сайт ["Продуктовый помощник FoodGram"](http://178.154.235.251/recipes/)

Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять 
понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для 
приготовления одного или нескольких выбранных блюд, совпадающие ингредиенты блюд суммируются. На страницах со списками рецептов
работает фильтрация по тегам (завтрак, обед, ужин). В базу редварительно загружен большой список ингредиентов для рецептов.

#### Инфраструктура

 - Проект работает с СУБД PostgreSQL.
 - Проект запущен на сервере в Яндекс.Облаке в трёх контейнерах: nginx, PostgreSQL и Django+Gunicorn.
 - Контейнер с проектом обновляется на Docker Hub.
 - В nginx настроена раздача статики, остальные запросы переадресуются в Gunicorn.
 - Данные сохраняются в volumes.

#### Стек

 - Python 3.9, Django 3, PostgreSQL, Gunicorn, Nginx, Docker, Яндекс.Облако(Ubuntu 20.04)

### Установка

#### Установка docker и docker-compose:

Если у вас уже установлены docker и docker-compose, этот шаг можно пропустить, иначе можно воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Создайте файл .env с данным содержимым:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
#### Запуск контейнера:
```bash
docker-compose up
```
#### Выключение контейнера:
```bash
docker-compose down
```

### Использование

#### Применение миграции:
```bash
docker-compose run web python manage.py migrate
```
#### Сбор статических файлов:
```bash
docker-compose run web python manage.py collectstatic --noinput
```
#### Инициализация стартовых данных:
```bash
docker-compose run web python manage.py loaddata fixtures.json
```
#### Создание суперпользователя Django:
```bash
docker-compose run web python manage.py createsuperuser
```