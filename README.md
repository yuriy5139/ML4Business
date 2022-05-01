# Домашнее задание №9

Flask-приложение запускается Gunicorn-ом и слушает порт 5000 в ожидании запросов на классификацию по датасету Spaceship Titanic https://www.kaggle.com/c/spaceship-titanic. 
Файл project/request.py содержит пример запроса на классификацию. Чтобы не формировать вручную json, request.py ждет в качестве единственного параметра номер строки датасета X_test, который хранится в формате pickle в папке project/models. Например: python3 request.py 10

Натренированная модель на основе catboost находится здесь project/models/model.pickle
Ноутбук тренировки модели: project/models/ML4Business.ipynb

### Собрать образ:
```
./build.sh
```

### Запустить контейнер
```
docker run -it -p 5000:5000 ml4business_hw9
```

