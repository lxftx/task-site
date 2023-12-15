Для работы проекта, требуется:
1) ПРОЕКТ ДОЛЖЕН НАХОДИТСЯ НА ДИСКЕ С, просто перекиньте папку task-server на диск С.
1) Установленный MySQL на ПК (На диске C) - так как Django будет искать его
2) Созданая база данных - "tasks" в MySQL - если называете по-другому, то в настройках проекта task-server\tasksite\tasksite\settings.py 
найдите модуль DATABASES. Меняем NAME - имя базы данных, на свою базу данных. В этом проекте использовалась база с именем "tasks". 
3) Далее поменяйте имя USER и PASSWORD - для входа в MySQL.

ПОСЛЕ ТОГО, КАК ВСЕ НАСТРОЙКИ БЫЛИ ЗАЙДЕСТВОВАНЫ ПОД ВАШУ БД, ЗАПУСКАЕМ ФАЙЛ RunProject.bat
"СКРИПТ ФАЙЛА RunProject.bat"
@echo off


cd C:\task-server

rem Создание виртуального окружения
py -m venv venv

rem Активация виртуального окружения (если используется)
call C:\task-server\venv\Scripts\activate

rem Установка необходимых библиотек
pip install -r requirements.txt

rem Переход в директорию с вашим Django проектом
cd C:\task-server\tasksite

rem Запуск миграций (если необходимо)
py manage.py makemigrations
py manage.py migrate

rem Запуск сервера Django
py manage.py runserver

pause