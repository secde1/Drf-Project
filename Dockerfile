# Используем официальный образ Python
FROM python:3.10

# Установка переменных среды для Django
ENV DJANGO_SETTINGS_MODULE=RestProject.settings
ENV DEBUG=False

# Создание и переключение в рабочий каталог внутри контейнера
WORKDIR /app

# Копирование файла requirements.txt в контейнер
COPY requirments.txt /app/
# Установка зависимостей из requirements.txt
RUN pip install --no-cache-dir -r /app/requirments.txt

# Копирование всего проекта в контейнер
COPY . /app/

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
