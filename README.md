# 🦆 DucksNet - Telegram VPN Shop Bot

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

### Environment Variables Configuration

| Variable                       | Required | Default                                                 | Description                                                                            |
| ------------------------------ | -------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| LETSENCRYPT_EMAIL              | 🔴       | -                                                       | Email for generating certificates                                                      |
|                                |          |                                                         |
| BOT_TOKEN                      | 🔴       | -                                                       | Telegram bot token                                                                     |
| BOT_ADMINS                     | ⭕       | -                                                       | List of admin IDs (e.g., 123456789,987654321)                                          |
| BOT_DEV_ID                     | 🔴       | -                                                       | ID of the bot developer                                                                |
| BOT_SUPPORT_ID                 | 🔴       | -                                                       | ID of the support person                                                               |
| BOT_DOMAIN                     | 🔴       | -                                                       | Domain of the bot (e.g., 3xui-shop.com)                                                |
| BOT_PORT                       | ⭕       | 8080                                                    | Port of the bot                                                                        |
|                                |          |                                                         |
| SHOP_EMAIL                     | ⭕       | support@3xui-shop.com                                   | Email for receipts                                                                     |
| SHOP_CURRENCY                  | ⭕       | RUB                                                     | Currency for buttons (e.g., RUB, USD, XTR)                                             |
| SHOP_TRIAL_ENABLED             | ⭕       | True                                                    | Enable trial subscription for new users                                                |
| SHOP_TRIAL_PERIOD              | ⭕       | 3                                                       | Duration of the trial subscription in days                                             |
| SHOP_REFERRED_TRIAL_ENABLED    | ⭕       | False                                                   | Enable extended trial period for referred users                                        |
| SHOP_REFERRED_TRIAL_PERIOD     | ⭕       | 7                                                       | Duration of the extended trial for referred users (in days)                            |
| SHOP_REFERRER_REWARD_ENABLED   | ⭕       | True                                                    | Enable the two-level referral reward system                                            |
| SHOP_REFERRER_LEVEL_ONE_PERIOD | ⭕       | 10                                                      | Reward in days for the first-level referrer (inviter)                                  |
| SHOP_REFERRER_LEVEL_TWO_PERIOD | ⭕       | 3                                                       | Reward in days for the second-level referrer (inviter of the inviter).                 |
| SHOP_BONUS_DEVICES_COUNT       | ⭕       | 1                                                       | Default Device Limit for Promocode, Trial, and Referral Users (Based on Plan Settings) |
| SHOP_PAYMENT_STARS_ENABLED     | ⭕       | True                                                    | Enable Telegram stars payment                                                          |
| SHOP_PAYMENT_CRYPTOMUS_ENABLED | ⭕       | False                                                   | Enable Cryptomus payment                                                               |
| SHOP_PAYMENT_HELEKET_ENABLED   | ⭕       | False                                                   | Enable Heleket payment                                                                 |
| SHOP_PAYMENT_YOOKASSA_ENABLED  | ⭕       | False                                                   | Enable Yookassa payment                                                                |
| SHOP_PAYMENT_YOOMONEY_ENABLED  | ⭕       | False                                                   | Enable Yoomoney payment                                                                |
|                                |          |                                                         |
| XUI_USERNAME                   | 🔴       | -                                                       | Username for authentication in the 3X-UI panel                                         |
| XUI_PASSWORD                   | 🔴       | -                                                       | Password for authentication in the 3X-UI panel                                         |
| XUI_TOKEN                      | ⭕       | -                                                       | Token for authentication (if configured in the panel)                                  |
| XUI_SUBSCRIPTION_PORT          | ⭕       | 2096                                                    | Port for subscription                                                                  |
| XUI_SUBSCRIPTION_PATH          | ⭕       | /user/                                                  | Path for subscription                                                                  |
|                                |          |                                                         |
| CRYPTOMUS_API_KEY              | ⭕       | -                                                       | API key for Cryptomus payment                                                          |
| CRYPTOMUS_MERCHANT_ID          | ⭕       | -                                                       | Merchant ID for Cryptomus payment                                                      |
|                                |          |                                                         |
| HELEKET_API_KEY                | ⭕       | -                                                       | API key for Heleket payment                                                            |
| HELEKET_MERCHANT_ID            | ⭕       | -                                                       | Merchant ID for Heleket payment                                                        |
|                                |          |                                                         |
| YOOKASSA_TOKEN                 | ⭕       | -                                                       | Token for YooKassa payment                                                             |
| YOOKASSA_SHOP_ID               | ⭕       | -                                                       | Shop ID for YooKassa payment                                                           |
|                                |          |                                                         |
| YOOMONEY_WALLET_ID             | ⭕       | -                                                       | Wallet ID for Yoomoney payment                                                         |
| YOOMONEY_NOTIFICATION_SECRET   | ⭕       | -                                                       | Notification secret key for Yoomoney payment                                           |
|                                |          |                                                         |
| LOG_LEVEL                      | ⭕       | DEBUG                                                   | Log level (e.g., INFO, DEBUG)                                                          |
| LOG_FORMAT                     | ⭕       | %(asctime)s \| %(name)s \| %(levelname)s \| %(message)s | Log format                                                                             |
| LOG_ARCHIVE_FORMAT             | ⭕       | zip                                                     | Log archive format (e.g., zip, gz)                                                     |

### Subscription Plans Configuration

```json
{
	"durations": [30, 60, 180, 365], // Available subscription durations in days

	"plans": [
		{
			"devices": 1, // Number of devices supported by the plan
			"prices": {
				"RUB": {
					// Prices for Russian rubles (RUB)
					"30": 70, // Price for 30 days
					"60": 120, // Price for 60 days
					"180": 300, // Price for 180 days
					"365": 600 // Price for 365 days
				},
				"USD": {
					// Prices for US dollars (USD)
					"30": 0.7, // Price for 30 days
					"60": 1.2, // Price for 60 days
					"180": 3, // Price for 180 days
					"365": 6 // Price for 365 days
				},
				"XTR": {
					// Prices for Telegram stars (XTR)
					"30": 60, // Price for 30 days
					"60": 100, // Price for 60 days
					"180": 250, // Price for 180 days
					"365": 500 // Price for 365 days
				}
			}
		},
		{
			// Next plan
		}
	]
}
```

### YooKassa Configuration

1. **Webhook Setup:**

   - Visit the [HTTP Notifications](https://yookassa.ru/my/merchant/integration/http-notifications) page.
   - Enter the bot’s domain in the notification URL, ending with `/yookassa` (e.g., `https://3xui-shop.com/yookassa`).
   - Select the following events:
     - `payment.succeeded`
     - `payment.waiting_for_capture`
     - `payment.canceled`

2. **Environment Variables Setup:**
   - Set the following environment variables:
     - `YOOKASSA_TOKEN`: Your secret key
     - `YOOKASSA_SHOP_ID`: Your shop ID

### YooMoney Configuration

1. **Webhook Setup:**

   - Visit the [HTTP Notifications](https://yoomoney.ru/transfer/myservices/http-notification) page.
   - Enter the bot’s domain in the notification URL, ending with `/yoomoney` (e.g., `https://3xui-shop.com/yoomoney`).
   - Copy the notification secret key.
   - Check the box for `sending HTTP-notifications`.
   - Save the changes.

2. **Environment Variables Setup:**
   - Set the following environment variables:
     - `YOOMONEY_WALLET_ID`: Your wallet ID
     - `YOOMONEY_NOTIFICATION_SECRET`: Your notification secret key

### 3X-UI Configuration

To ensure the bot functions correctly, you must configure the 3X-UI panel:

- [Set up SSL certificate.](https://github.com/MHSanaei/3x-ui?tab=readme-ov-file#ssl-certificate)
- Set up an Inbound **(the first one will be used)** for adding clients.
- Enable the subscription service with port `2096` and path `/user/`.
  > **Don’t forget to specify certificate for the subscription.**
- Disabling configuration encryption is recommended.

<a id="bugs-and-feature-requests"></a>

### Referral and Trial Rewards Configuration

Bot now supports **trial subscriptions** and a **two-level referral reward system**. Here’s how it works:
All configuration is available via `.env` [(see it above)](#environment-variables-configuration).

| Type of reward                     | How it works                                                                                                                                                                            |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Trial period                       | A trial subscription is available by 'TRY FOR FREE' button at start menu to any user who opens the bot and does not have an active subscription.                                        |
| Extended Trial period              | This option is just like previous 'trial period', but allows to configure **extended trial period** for an invited user.                                                                |
| Two-Level Referral Payment Rewards | When a referred user pays for a subscription, the referrer and the second-level referrer (the user who invited the referrer) receive fixed count of days at the moment fore each level. |

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
