# Домашнее задание №9

Flask-приложение запускается Gunicorn-ом и слушает порт 5000 в ожидании запросов на классификацию по датасету Spaceship Titanic https://www.kaggle.com/c/spaceship-titanic. 
Файл project/request.py содержит пример запроса на классификацию.

### Собрать образ:
```
./build.sh
```

### Запустить контейнер
```
docker run -it -p 5000:5000 ml4business_hw9
```

