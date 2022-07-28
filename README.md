# Sharifullina_sber_test

## 1. Скачивание и установка необходимых пакетов  

1.1 Выполните код ниже, чтобы скачать репозиторий на локальный компьютер и перейти в эту папку.
```
git clone git@github.com:RamilyaSharifullina25/Sharifullina_sber_test.git
cd Sharifullina_sber_test
```
1.2. Внутри папки ```Sharifullina_sber_test``` выполните код ниже чтобы создать новую виртуальную среду и его активировать.   
```
python -m venv sharifullina_env
source sharifullina_env/bin/activate
```
1.3 Далее выполните код ниже, чтобы на вашу только что созданную среду скачать все необходимые библиотеки.  
```
pip install -r requirements.txt
```
2. Для того, чтобы протестить модель на веб странице выполните  
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
После запуска приложения, скопируйте URL ```http://127.0.0.1:5000/``` и откройте его в браузере.   

3. Выберите файл формата ...
--- 

## Выполните код ниже, чтобы создать образ (docker image) при помощи ```Dockerfile```:  
```
docker build -t your_dockerhub_id/sharifullina_sbeer_test .
docker run -p 8888:5000 your_dockerhub_id/sharifullina_sbeer_test
```  

## Телеграм бот https://t.me/SberSharifullinaBot

1. Для того, чтобы установить нужные библиотеки из ```requirements2.txt``` выполните те же действия, описанные выше, для скачивания и установки необходимых пакетов.  

### Описание репозитория  
1. ```app.py```, папки ```templates``` и ```static``` содержат файлы, необходимые для запуска веб сайта.  
2. ```dogs_classification.ipynb``` содержит пайплайн CV модели.
3. ```telegram_bot``` сожержит файлы, необходимые для запуска и работы телеграм бота.  
4.  ```requirements.txt``` содержит модули, необходимые для запуска модели и веб клиента.  
5.  ```Dockerfile``` для создания ```docker image``` (образа).
