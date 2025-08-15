# 🦆 DucksNet - Telegram VPN Магазин Бот

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.15+-green.svg)](https://aiogram.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**DucksNet** - это мощный Telegram бот для продажи VPN подписок с интеграцией 3X-UI панели. Бот предоставляет полный функционал для управления VPN сервисом через удобный Telegram интерфейс.

## ✨ Основные возможности

### 🛒 **Система продаж**

- Автоматическая продажа VPN подписок
- Поддержка множественных платежных систем
- Система промокодов и скидок
- Автоматическое создание и управление VPN аккаунтами

### 💳 **Платежные системы**

- **Telegram Stars** ⭐ (встроенная валюта Telegram)
- **Cryptomus** 🏦 (криптоплатежи)
- **Heleket** 💰 (альтернативная платежная система)
- **YooKassa** 🏪 (российская платежная система)
- **YooMoney** 💳 (электронные кошельки)

### 👥 **Реферальная система**

- Многоуровневая реферальная программа
- Автоматические награды за приглашения
- Статистика и аналитика рефералов
- Система приглашений с отслеживанием

### 🎯 **Пользовательский опыт**

- Многоязычная поддержка (русский/английский)
- Интуитивный интерфейс с inline-клавиатурами
- Система уведомлений
- Автоматические напоминания

### 🔧 **Административные функции**

- Панель администратора
- Статистика и аналитика
- Управление серверами
- Система резервного копирования
- Управление промокодами
- Система уведомлений

### 🛡️ **VPN интеграция**

- Полная интеграция с 3X-UI панелью
- Автоматическое создание пользователей
- Управление трафиком и лимитами
- Мониторинг состояния серверов

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.12+
- Docker и Docker Compose
- 3X-UI панель
- Telegram Bot Token
- Домен с SSL сертификатом

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/ducksnet.git
cd ducksnet
```

### 2. Настройка переменных окружения

Создайте файл `.env` в корневой директории:

```env
# Конфигурация бота
BOT_TOKEN=your_telegram_bot_token
BOT_DOMAIN=your-domain.com
BOT_ADMINS=123456789,987654321
BOT_DEV_ID=123456789
BOT_SUPPORT_ID=123456789
BOT_PORT=8080

# Конфигурация магазина
SHOP_EMAIL=support@ducksnet.com
SHOP_CURRENCY=RUB
SHOP_TRIAL_ENABLED=true
SHOP_TRIAL_PERIOD=3
SHOP_REFERRER_REWARD_ENABLED=true
SHOP_REFERRER_LEVEL_ONE_PERIOD=10
SHOP_REFERRER_LEVEL_ONE_RATE=50

# Конфигурация 3X-UI
XUI_USERNAME=your_xui_username
XUI_PASSWORD=your_xui_password
XUI_TOKEN=your_xui_token
XUI_SUBSCRIPTION_PORT=2096
XUI_SUBSCRIPTION_PATH=/user/

# Платежные шлюзы
SHOP_PAYMENT_STARS_ENABLED=true
SHOP_PAYMENT_CRYPTOMUS_ENABLED=false
SHOP_PAYMENT_HELEKET_ENABLED=false
SHOP_PAYMENT_YOOKASSA_ENABLED=false
SHOP_PAYMENT_YOOMONEY_ENABLED=false

# Cryptomus (если включено)
CRYPTOMUS_API_KEY=your_cryptomus_api_key
CRYPTOMUS_MERCHANT_ID=your_cryptomus_merchant_id

# Heleket (если включено)
HELEKET_API_KEY=your_heleket_api_key
HELEKET_MERCHANT_ID=your_heleket_merchant_id

# YooKassa (если включено)
YOOKASSA_TOKEN=your_yookassa_token
YOOKASSA_SHOP_ID=your_yookassa_shop_id

# YooMoney (если включено)
YOOMONEY_NOTIFICATION_SECRET=your_yoomoney_secret
YOOMONEY_WALLET_ID=your_yoomoney_wallet_id

# База данных
DB_NAME=ducksnet_database

# Redis
REDIS_HOST=ducksnet-redis
REDIS_PORT=6379
REDIS_DB_NAME=0

# Let's Encrypt
LETSENCRYPT_EMAIL=your-email@example.com
```

### 3. Запуск с Docker

```bash
# Запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f bot
```

### 4. Ручная установка

```bash
# Установка зависимостей
pip install poetry
poetry install

# Компиляция переводов
poetry run pybabel compile -d app/locales -D bot

# Применение миграций базы данных
poetry run alembic -c app/db/alembic.ini upgrade head

# Запуск бота
poetry run python app/__main__.py
```

## 📁 Структура проекта

```
ducksnet/
├── app/                          # Основное приложение
│   ├── bot/                      # Telegram бот
│   │   ├── filters/              # Фильтры для обработчиков
│   │   ├── middlewares/          # Промежуточное ПО
│   │   ├── models/               # Модели данных
│   │   ├── payment_gateways/     # Платежные шлюзы
│   │   ├── routers/              # Маршрутизаторы (хендлеры)
│   │   ├── services/             # Бизнес-логика
│   │   ├── tasks/                # Фоновые задачи
│   │   └── utils/                # Утилиты
│   ├── config.py                 # Конфигурация
│   ├── data/                     # Данные (изображения, планы)
│   ├── db/                       # База данных
│   │   ├── models/               # Модели БД
│   │   └── migration/            # Миграции
│   ├── locales/                  # Переводы
│   └── logs/                     # Логи
├── scripts/                      # Скрипты развертывания
├── docker-compose.yml            # Docker Compose конфигурация
├── Dockerfile                    # Docker образ
├── pyproject.toml               # Зависимости Python
└── README.md                    # Документация
```

## 🔧 Конфигурация

### Настройка 3X-UI

1. Убедитесь, что ваша 3X-UI панель доступна
2. Создайте API токен в панели администратора
3. Настройте параметры подключения в `.env`

### Настройка платежных систем

#### Telegram Stars

```env
SHOP_PAYMENT_STARS_ENABLED=true
```

#### Cryptomus

```env
SHOP_PAYMENT_CRYPTOMUS_ENABLED=true
CRYPTOMUS_API_KEY=your_api_key
CRYPTOMUS_MERCHANT_ID=your_merchant_id
```

#### YooKassa

```env
SHOP_PAYMENT_YOOKASSA_ENABLED=true
YOOKASSA_TOKEN=your_token
YOOKASSA_SHOP_ID=your_shop_id
```

### Настройка реферальной системы

```env
SHOP_REFERRER_REWARD_ENABLED=true
SHOP_REFERRER_LEVEL_ONE_PERIOD=10
SHOP_REFERRER_LEVEL_ONE_RATE=50
SHOP_REFERRER_LEVEL_TWO_PERIOD=3
SHOP_REFERRER_LEVEL_TWO_RATE=5
```

## 📊 Административные команды

### Основные команды бота

- `/start` - Главное меню
- `/profile` - Профиль пользователя
- `/subscription` - Управление подпиской
- `/referral` - Реферальная программа
- `/support` - Поддержка

### Административные команды

- `/admin` - Панель администратора
- `/stats` - Статистика
- `/backup` - Создание резервной копии
- `/maintenance` - Режим обслуживания

## 🛠️ Разработка

### Установка для разработки

```bash
# Клонирование репозитория
git clone https://github.com/your-username/ducksnet.git
cd ducksnet

# Установка зависимостей
poetry install

# Установка pre-commit хуков
poetry run pre-commit install

# Настройка базы данных для разработки
poetry run alembic -c app/db/alembic.ini upgrade head
```

### Структура кода

Проект использует современные практики разработки:

- **Async/Await** - Асинхронное программирование
- **Dependency Injection** - Внедрение зависимостей
- **Repository Pattern** - Паттерн репозитория для работы с БД
- **Service Layer** - Слой сервисов для бизнес-логики
- **Middleware Pattern** - Промежуточное ПО для обработки запросов

### Тестирование

```bash
# Запуск тестов
poetry run pytest

# Запуск с покрытием
poetry run pytest --cov=app
```

## 📈 Мониторинг и логирование

### Логи

Логи сохраняются в директории `app/logs/`:

- `bot.log` - Основные логи бота
- `payment.log` - Логи платежей
- `vpn.log` - Логи VPN операций

### Метрики

Бот предоставляет следующие метрики:

- Количество активных пользователей
- Статистика платежей
- Использование трафика
- Реферальная статистика

## 🔒 Безопасность

### Рекомендации по безопасности

1. **Храните токены в безопасном месте**
2. **Используйте HTTPS для всех соединений**
3. **Регулярно обновляйте зависимости**
4. **Настройте firewall**
5. **Используйте сильные пароли**

### Переменные окружения

Никогда не коммитьте файл `.env` в репозиторий. Используйте `.env.example` для примера конфигурации.

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! Пожалуйста, ознакомьтесь с нашими правилами:

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

### Требования к коду

- Следуйте PEP 8
- Добавляйте типизацию
- Пишите документацию
- Добавляйте тесты для новой функциональности

## 📄 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

## 🆘 Поддержка

### Полезные ссылки

- [Документация Aiogram](https://aiogram.dev/)
- [3X-UI Документация](https://github.com/alireza0/x-ui)
- [Docker Документация](https://docs.docker.com/)

### Сообщество

- [Telegram Канал](https://t.me/ducksnet_support)
- [GitHub Issues](https://github.com/your-username/ducksnet/issues)
- [Discord Сервер](https://discord.gg/ducksnet)

## 🙏 Благодарности

- [Aiogram](https://aiogram.dev/) - Отличная библиотека для Telegram ботов
- [3X-UI](https://github.com/alireza0/x-ui) - Панель управления Xray
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM для Python
- [Alembic](https://alembic.sqlalchemy.org/) - Миграции базы данных

---

**DucksNet** - Создано с ❤️ для сообщества VPN провайдеров
