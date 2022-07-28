# Sharifullina_sber_test

### 1. Скачивание и установка необходимых пакетов  

1.1 Выполните 
```
git clone git@github.com:RamilyaSharifullina25/Sharifullina_sber_test.git
```
чтобы скачать репозиторий и перейдите в него с помощью 
```
cd Sharifullina_sber_test
```
.  
1.2. Внутри папки ```Sharifullina_sber_test``` выполните  
```
python -m venv sharifullina_env
```
 чтобы создать виртуальную среду программирования и 
```
source sharifullina_env/bin/activate
```
 чтобы его активировать.    
1.3 Далее выполните 
```
pip install -r requirements.txt
```
чтобы на вашу только что созданную среду скачать все необходимые библиотеки.   

2. Для того, чтобы протестить модель на веб странице выполните  
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
После запуска приложения, скопируйте URL ```http://127.0.0.1:5000/``` и откройте его в браузере.   

3. Выберите файл формата ...

### Создание образа (docker image):  
```
docker build -t your_dockerhub_id/sharifullina_sbeer_test .
docker run -p 8888:5000 your_dockerhub_id/sharifullina_sbeer_test
```  


### Описание репозитория  
1. ```app.py```, папки ```templates``` и ```static``` содержат файлы, необходимые для запуска веб клиента.  
2. ```dogs_classification.ipynb``` содержит пайплайн CV модели.
3. ```telegram_bot``` сожержит файлы, необходимые для запуска и работы телеграм бота.  
4.  ```requirements.txt``` содержит модули, необходимые для запуска модели и веб клиента.  
5.  ```Dockerfile``` для создания ```docker image``` (образа).
