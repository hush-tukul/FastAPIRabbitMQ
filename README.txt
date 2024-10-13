RabbitMQ с Python и Pika

Установка RabbitMQ

На Ubuntu (или Debian)

1. Обновите пакеты и установите необходимые зависимости:
   sudo apt update
   sudo apt install rabbitmq-server

2. Запустите RabbitMQ сервер:
   sudo systemctl start rabbitmq-server

3. Проверьте статус RabbitMQ сервера:
   sudo systemctl status rabbitmq-server

4. Включите автозапуск RabbitMQ при загрузке системы:
   sudo systemctl enable rabbitmq-server

На Windows

1. Скачайте и установите RabbitMQ.
2. После установки, откройте командную строку и выполните:
   rabbitmq-server.bat
3. Проверьте, что сервер запущен, открыв http://localhost:15672 (по умолчанию для доступа к веб-интерфейсу RabbitMQ) и введите имя пользователя и пароль (по умолчанию guest/guest).

Установка Pika

Убедитесь, что у вас установлен Python и pip, затем выполните следующую команду для установки библиотеки Pika:
pip install pika

Основные команды

Проверка работы RabbitMQ

1. Статус сервера:
   sudo systemctl status rabbitmq-server

2. Перезапуск RabbitMQ сервера:
   sudo systemctl restart rabbitmq-server
