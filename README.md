# SkyChat
## Чат для переписок

Данный проект представляет базовую реализацию чата переписок по комнатам(тематикам). Тематические чаты создаются администратором,
 все желающие зарегистрированные пользователи могут туда заходить и переписываться. Чат работает на вебсокетах в асинхронном режиме.
___
## Требования

Для запуска проекта Django убедитесь, что у вас есть:

- Установленный Python 3 на вашей системе
- Установщик пакетов Pip
- Виртуальная среда (необязательно, но рекомендуется)

___
##  Настройка проекта

1. Клонируйте репозиторий проекта на ваш компьютер.
2. Перейдите в директорию проекта.
3. Создайте виртуальную среду (необязательно):
___
### 1. Установка venv
Если у вас еще не установлен модуль venv, выполните следующую команду в командной строке, чтобы установить его:
```
pip install venv
```

### 2. Установка зависимостей
**1. Перейдите в корневую папку проекта.**

**2. Активируйте виртуальное окружение venv следующей командой:**
```
source venv/bin/activate
```
 
  или для Windows:
```
venv\Scripts\activate**
```

**3. Установите зависимости, указанные в файле requirements.txt, выполнив следующую команду:**
```
pip install -r requirements.txt
```

**4. Создайте суперпользователя. Комнаты чата может добавить администратор в админ панели.**
```
cd src
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```
Переходим в админку `http://localhost:8000/admin/` добавляем комнаты чата.

Далее переходим на `http://localhost:8000/` - в шапки сайти выбираем команаты -> нужную комнату и переписываемся.
