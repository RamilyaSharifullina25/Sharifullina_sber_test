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
## 2. Веб приложение.  
Для того, чтобы протестить модель на веб странице выполните  
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
После запуска приложения, скопируйте URL ```http://127.0.0.1:5000/``` и откройте его в браузере.   


## 3. ```Dockerfile```
Выполните код ниже, чтобы создать образ (docker image)   
```
docker build -t your_dockerhub_id/sharifullina_sbeer_test .
docker run -p 8888:5000 your_dockerhub_id/sharifullina_sbeer_test
```  

## 4. Телеграм бот https://t.me/SberSharifullinaBot

Для того, чтобы установить нужные библиотеки из ```requirements_telegram_bot.txt``` выполните те же действия, описанные выше, для скачивания и установки необходимых пакетов.  После, выполните ```python telegram_bot.py``` чтобы запустить бот.    

## 5. Описание репозитория  
1. ```app.py```, папки ```templates``` и ```static``` содержат файлы, необходимые для запуска веб сайта.  
2. ```dogs_classification.ipynb``` содержит пайплайн CV модели.
3. ```telegram_bot.py``` необходим для запуска и работы телеграм бота.  
4. ```requirements.txt``` и ```requirements_telegram_bot.txt```  содержат модули, необходимые для запуска модели, веб клиента и телеграм бота.  
5. ```Dockerfile``` для создания ```docker image``` (образа).  
6. ```resnet_pretrained.pt``` сохраненная модель.  
7. ```examples``` содержит картинки для примера датастеа.  
