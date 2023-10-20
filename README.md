# Telegram Bot Reminders

Это простой [Telegram-бот]((https://t.me/CleaningYSBot), который поможет вам организовать график уборки, напоминая о ежедневных задачах. Для каждого дня недели прописаны определенные действия. Он написан на Python 3 и использует библиотеку aiogram для взаимодействия с Telegram API.


## Некоторые функции:

- Получение расписания уборки на каждый день недели.
- Подсказки и рекомендации по уборке для разных комнат.
- Простой и интуитивно понятный интерфейс.


## Как использовать

1.  Запустите бота, отправив команду /start.
2.  Бот ответит клавиатурой с кнопками для каждого дня недели.
3.  Нажмите на день, для которого вы хотите увидеть расписание уборки.
4.  В ответ бот покажет задания по уборке на этот день.

## Зависимости

-   Python 3
-   aiogram

## Установка

1.  Клонируйте этот репозиторий.
2.  Установите зависимости с помощью следующей команды:
```bash
pip3 install -r requirements.txt
```
 
3.  Создайте бота в Telegram и получите его API-токен. [Здесь](https://core.telegram.org/bots#creating-a-new-bot) вы можете найти инструкции по созданию бота и получению его API-токена.
    
4.  Создайте файл `.env` в корневом каталоге проекта и добавьте в него следующую строку:
```shell
TELEGRAM_API_TOKEN=<your-telegram-api-token> 
```
Замените `<your-telegram-api-token>` на API-токен, который вы получили в шаге 3.
    

## Запуск бота

Чтобы запустить бота, выполните следующую команду в корневом каталоге проекта:
```shell
python3 bot.py
```

Вы можете остановить бота в любой момент, нажав `Ctrl+C`.
