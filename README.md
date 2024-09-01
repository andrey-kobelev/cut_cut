# YaCut
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
git clone https://github.com/andrey-kobelev/yacut.git
```  
  
```  
cd yacut
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

## Команды запуска

Корневой директории проекта выполните команду запуска проекта

```
flask run
```

В терминале должно появиться примерно такое сообщение

```
 * Serving Flask app 'yacut'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: <pin>

```


## Справка

```bash
flask --help
```

```
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  An application to load must be given with the '--app' option, 'FLASK_APP'
  environment variable, or with a 'wsgi.py' or 'app.py' file in the current
  directory.

Options:
  -e, --env-file FILE   Load environment variables from this file. python-
                        dotenv must be installed.
  -A, --app IMPORT      The Flask application or factory function to load, in
                        the form 'module:name'. Module can be a dotted import
                        or file path. Name is not required if it is 'app',
                        'application', 'create_app', or 'make_app', and can be
                        'name(args)' to pass arguments.
  --debug / --no-debug  Set debug mode.
  --version             Show the Flask version.
  --help                Show this message and exit.

Commands:
  db      Perform database migrations.
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.


```