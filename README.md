# Краткое описание приложения
Приложение написано на языке программирования Python с использованием фреймворков Django и Django REST Framework.

В качестве СУБД использована SQLite3 (По умолчанию).

# Установка и запуск приложения
Для запуска приложения должен быть установлен python3. <br><br>
Инструкция по установке:
1. Скачать файлы проекта с удаленного репозитория;
2. Открыть Django проект simple_project в папке fablite_test;
3. Создать виртуальное окружение: <br>
`python3 -m venv venv`
4. Активировать виртуальное окружение: <br> 
`source venv/bin/activate` (Linux / MacOS) <br>
`venv\Scripts\activate` (Windows)
5. Обновить setuptools: <br>
`pip install —upgrade setuptools`
6. Установить зависимости проекта (Django): <br> 
`pip install -r requirements.txt`
7. Создать файлы миграций: <br>
`python manage.py makemigrations`
8. Выполнить миграции: <br> 
`python manage.py migrate`
9. Создать суперпользователя: <br> 
`python manage.py createsuperuser`
10. Запустить локальный сервер (Django): <br> 
`python manage.py runserver`
