# Tkinter Application

Приложение предназначено для обработки служебной информации, хранящейся в БД приложения и текстовых файлах. Использует MySQL в качестве базы данных, Tkinter.

Перед тем как начать, убедитесь, что у вас установлены следующие компоненты:

- **Python** (версия 3.11 или старше)
- **MySQL** (версия 15 или старше)
- **pip** 
- **virtualenv** (опционально)

## Установка

python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows

## Установите зависимости:
pip install -r requirements.txt

Настройте базу данных:
Создайте базу данных в MySQL и обновите настройки в .env вашего проекта:

database_url = "mysql+asyncmy://user:password@host/database"

##Запуск приложения
Чтобы запустить приложение, выполните следующую команду:
python3 main.py

