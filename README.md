# Short_url

Short_url - учебный проект, клон [clck.ru](http://clck.ru),
в проекте за основу взяты такие библиотеки, как Flask и Flask-SQLAlchemy.

## Краткое описание функционала

Генерация коротких ссылок на основе предоставленной пользователем ссылки,
запись в базу таких данных, как время создания короткой ссылки, длинная ссылка,
короткая ссылка, счетчик переходов (изменяется при каждом переходе по короткой ссылке).
Перед записью в базу выполняется проверка на коллизии.
При генерации короткой ссылки используются ASCII символы: заглавные и строчные
латинские буквы, цифры и символ '_'.

## Туториал по установке

```bash
$ python3 -m venv venv

$ source venv/bin/activate  # Для Windows используйте venv\Scripts\activate

$ pip install -r requirements.txt

$ mkdir -p instance

$ sqlite3 instance/shorturl.db < schema.sql

```