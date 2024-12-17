# CutCut
>Проект CutCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Автор 
- Кобелев Андрей Андреевич  
    - [email](mailto:andrey.pydev@gmail.com)
  
## Технологии  
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

## Как запустить проект: 
  
Клонировать репозиторий и перейти в него в командной строке:  
  
```  
git clone https://github.com/andrey-kobelev/cut_cut.git
```  
  
```  
cd cut_cut
```  
  
Cоздать и активировать виртуальное окружение:  
  
```  
python3 -m venv env  
```  
  
```  
source env/bin/activate  
```  
  
Установить зависимости из файла requirements.txt:  
  
```  
python3 -m pip install --upgrade pip  
```  
  
```  
pip install -r requirements.txt  
```

**Создать базу данных**

Убедитесь, что виртуальное окружение проекта what_to_watch активировано, и из директории _what_to_watch_ запустите интерактивную оболочку:

```
..$ flask shell
Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:09:00) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
App: cut_cut [development]
Instance: /Users/username/dev/what_to_watch/instance
>>> from opinions_app import db
>>> db.create_all()
```

**Применить миграции:**

```
flask db upgrade
```

## Команды запуска

Корневой директории проекта выполните команду запуска проекта

```
flask run
```

В терминале должно появиться примерно такое сообщение

```
 * Serving Flask app 'cut_cut'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: <pin>

```


## Справка

### Инструкции для пользователя сайта

Пользовательский интерфейс сервиса — одна страница с формой. Форма должна состоит из двух полей:

- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.

Пользовательский вариант короткой ссылки не должен превышать 16 символов.
Формат для короткой ссылки — символы, в качестве которых можно использовать:

- большие латинские буквы,
- маленькие латинские буквы,
- цифры в диапазоне от 0 до 9.

Если вы не заполните поле со своим вариантом короткой ссылки, то сервис сгенирирует её автоматически. Например, сервис может предложить вот такой вариант: http://127.0.0.1:5000/4GhKH3.


### Инструкции для использования API

Сервис обслуживает только два эндпоинта:

- _/api/id/_ — POST-запрос на создание новой короткой ссылки;
- _/api/id/<short_id>/_ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

##### Пример POST-запроса

**Request body:**

```json
{
  "url": "string",
  "custom_id": "string"
}
```

**Responses:**

```json
{
  "url": "string",
  "short_link": "string"
}
```