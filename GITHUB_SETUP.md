# 🔑 Настройка GitHub Actions для DucksNet

Этот документ описывает, как настроить автоматический деплой через GitHub Actions.

## 📋 Предварительные требования

1. ✅ GitHub репозиторий с кодом DucksNet
2. ✅ VPS сервер с Ubuntu/Debian
3. ✅ SSH доступ к серверу
4. ✅ Домен с настроенными DNS записями

## 🔐 Настройка GitHub Secrets

### 1. Перейдите в настройки репозитория

1. Откройте ваш GitHub репозиторий
2. Нажмите `Settings` (вкладка)
3. В левом меню выберите `Secrets and variables` → `Actions`
4. Нажмите `New repository secret`

### 2. Добавьте обязательные секреты

#### `SERVER_HOST`

- **Описание**: IP адрес или домен вашего сервера
- **Пример**: `123.456.789.123` или `your-server.com`
- **Важно**: Без `http://` или `https://`

#### `SERVER_USER`

- **Описание**: Имя пользователя для SSH доступа
- **Пример**: `ducksnet` или `root`
- **Важно**: Пользователь должен иметь права на выполнение Docker команд

#### `SERVER_SSH_KEY`

- **Описание**: Приватный SSH ключ для доступа к серверу
- **Как получить**:

  ```bash
  # На вашем локальном компьютере
  ssh-keygen -t rsa -b 4096 -C "your-email@example.com"

  # Скопируйте содержимое приватного ключа
  cat ~/.ssh/id_rsa
  ```

- **Важно**: Включайте ВСЕ содержимое файла, включая строки `-----BEGIN OPENSSH PRIVATE KEY-----` и `-----END OPENSSH PRIVATE KEY-----`

#### `SERVER_PORT`

- **Описание**: SSH порт сервера
- **Значение по умолчанию**: `22`
- **Пример**: `22` или `2222` (если изменен)

### 3. Добавьте дополнительные секреты (опционально)

#### `TELEGRAM_BOT_TOKEN`

- **Описание**: Токен бота для уведомлений о деплое
- **Как получить**: Создайте бота через @BotFather
- **Пример**: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

#### `TELEGRAM_CHAT_ID`

- **Описание**: ID чата для отправки уведомлений
- **Как получить**: Отправьте сообщение боту и проверьте в `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
- **Пример**: `123456789` или `-987654321` (для групп)

## 🚀 Настройка сервера

### 1. Подготовка сервера

```bash
# Подключитесь к серверу
ssh your-user@your-server

# Обновите систему
sudo apt update && sudo apt upgrade -y

# Установите необходимые пакеты
sudo apt install -y curl wget git unzip
```

### 2. Установка Docker

```bash
# Установка Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Добавьте пользователя в группу docker
sudo usermod -aG docker $USER

# Перезапустите сессию SSH или выполните
newgrp docker
```

### 3. Установка Docker Compose

```bash
# Установка Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Проверка установки
docker-compose --version
```

### 4. Создание пользователя для приложения

```bash
# Создание пользователя
sudo useradd -m -s /bin/bash ducksnet
sudo usermod -aG docker ducksnet

# Создание директории
sudo mkdir -p /opt/ducksnet
sudo chown ducksnet:ducksnet /opt/ducksnet
```

### 5. Настройка SSH ключей

```bash
# Переключитесь на пользователя ducksnet
sudo su - ducksnet

# Создайте .ssh директорию
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Создайте файл authorized_keys
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Добавьте ваш публичный ключ
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..." >> ~/.ssh/authorized_keys
```

## 📁 Настройка проекта на сервере

### 1. Клонирование репозитория

```bash
# Переключитесь на пользователя ducksnet
sudo su - ducksnet

# Перейдите в директорию проекта
cd /opt/ducksnet

# Клонируйте репозиторий
git clone https://github.com/your-username/DucksNet.git .
```

### 2. Настройка переменных окружения

```bash
# Скопируйте пример файла
cp env.example .env

# Отредактируйте файл
nano .env
```

**Важные переменные для настройки:**

```bash
# Bot Configuration
BOT_TOKEN=your_telegram_bot_token_here
BOT_DOMAIN=your-domain.com

# Database
DATABASE_URL=sqlite:///app/db/database.db

# Redis
REDIS_PASSWORD=your_secure_redis_password_here

# Let's Encrypt
LETSENCRYPT_EMAIL=your-email@example.com

# Traefik Dashboard Auth
# Генерируйте хеш: echo -n 'admin:password' | base64
TRAEFIK_AUTH=YWRtaW46cGFzc3dvcmQ=

# VPN Configuration
XUI_PANEL_URL=https://your-xui-panel.com
XUI_USERNAME=your_username
XUI_PASSWORD=your_password
```

### 3. Создание systemd сервиса

```bash
# Создайте файл сервиса
sudo nano /etc/systemd/system/ducksnet.service
```

**Содержимое файла:**

```ini
[Unit]
Description=DucksNet Bot
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/ducksnet
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0
User=ducksnet
Group=ducksnet

[Install]
WantedBy=multi-user.target
```

**Активация сервиса:**

```bash
# Перезагрузите systemd
sudo systemctl daemon-reload

# Включите автозапуск
sudo systemctl enable ducksnet.service
```

## 🔒 Настройка безопасности

### 1. Настройка firewall

```bash
# Установка UFW
sudo apt install -y ufw

# Настройка правил
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Включение firewall
sudo ufw --force enable

# Проверка статуса
sudo ufw status
```

### 2. Настройка fail2ban (опционально)

```bash
# Установка fail2ban
sudo apt install -y fail2ban

# Включение автозапуска
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## 🧪 Тестирование настройки

### 1. Проверка SSH подключения

```bash
# С вашего локального компьютера
ssh ducksnet@your-server

# Или с GitHub Actions (проверьте логи)
```

### 2. Проверка Docker

```bash
# На сервере
docker --version
docker-compose --version
docker ps
```

### 3. Первый запуск

```bash
# Запуск сервисов
sudo systemctl start ducksnet

# Проверка статуса
sudo systemctl status ducksnet
docker-compose ps
```

## 📱 Настройка уведомлений в Telegram

### 1. Создание бота для уведомлений

1. Напишите @BotFather в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям
4. Сохраните токен бота

### 2. Получение Chat ID

1. Добавьте бота в нужный чат
2. Отправьте любое сообщение
3. Откройте в браузере:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. Найдите `chat.id` в ответе

### 3. Добавление в GitHub Secrets

- `TELEGRAM_BOT_TOKEN`: токен вашего бота
- `TELEGRAM_CHAT_ID`: ID чата

## 🔄 Автоматический деплой

### 1. Принцип работы

После настройки, при каждом push в ветку `main`:

1. ✅ Запускаются тесты
2. 🔍 Проверяется качество кода
3. 🐳 Собирается Docker образ
4. 🚀 Код деплоится на сервер
5. 📱 Отправляется уведомление в Telegram

### 2. Ручной запуск

1. Перейдите в `Actions` → `Deploy to Server`
2. Нажмите `Run workflow`
3. Выберите окружение (`production` или `staging`)
4. Нажмите `Run workflow`

### 3. Мониторинг деплоя

- GitHub Actions логи: `Actions` → `Deploy to Server` → `Run ID`
- Логи сервера: `docker-compose logs -f [service_name]`
- Статус сервисов: `docker-compose ps`

## 🚨 Устранение неполадок

### Проблемы с SSH:

```bash
# Проверка подключения
ssh -v ducksnet@your-server

# Проверка прав на ключи
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub

# Проверка authorized_keys
cat ~/.ssh/authorized_keys
```

### Проблемы с Docker:

```bash
# Перезапуск Docker
sudo systemctl restart docker

# Проверка прав пользователя
groups ducksnet
sudo usermod -aG docker ducksnet
```

### Проблемы с GitHub Actions:

1. Проверьте логи в `Actions` → `Deploy to Server`
2. Убедитесь, что все секреты настроены правильно
3. Проверьте права доступа к репозиторию
4. Убедитесь, что workflow файл находится в `.github/workflows/`

## 📚 Полезные команды

### Управление сервисами:

```bash
# Запуск
sudo systemctl start ducksnet

# Остановка
sudo systemctl stop ducksnet

# Перезапуск
sudo systemctl restart ducksnet

# Статус
sudo systemctl status ducksnet

# Логи
sudo journalctl -u ducksnet -f
```

### Управление Docker:

```bash
# Статус контейнеров
docker-compose ps

# Логи сервиса
docker-compose logs -f bot

# Перезапуск сервиса
docker-compose restart bot

# Обновление и пересборка
docker-compose up -d --build
```

### Мониторинг:

```bash
# Использование ресурсов
docker stats

# Дисковое пространство
df -h

# Память
free -h

# Сетевые соединения
netstat -tulpn
```

## 🎯 Следующие шаги

После успешной настройки:

1. ✅ Проверьте работу бота
2. 🔒 Настройте дополнительные меры безопасности
3. 📊 Настройте мониторинг
4. 🔄 Протестируйте автоматический деплой
5. 📚 Изучите документацию проекта

## 📞 Поддержка

При возникновении проблем:

1. Проверьте логи GitHub Actions
2. Проверьте логи сервера
3. Убедитесь, что все секреты настроены правильно
4. Создайте issue в репозитории с подробным описанием проблемы

---

**Удачной настройки! 🚀**
