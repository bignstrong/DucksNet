#!/usr/bin/env python3
"""
Диагностика и получение ID канала для принудительной подписки.
"""
import asyncio
import sys
from pathlib import Path

# Добавляем путь к приложению
app_path = Path(__file__).parent.parent
sys.path.insert(0, str(app_path))

async def main():
    print("🔍 Диагностика системы принудительной подписки")
    print("=" * 60)
    
    # Проверяем актуальную проблему из логов
    print("❌ ОБНАРУЖЕНА ПРОБЛЕМА:")
    print("   Bad Request: chat not found для канала -1002636737929")
    print()
    
    print("🛠️ ВОЗМОЖНЫЕ ПРИЧИНЫ И РЕШЕНИЯ:")
    print()
    
    print("1️⃣ Неправильный ID канала:")
    print("   • ID в .env: -1002636737929")
    print("   • Нужно получить правильный ID для @DucksNet")
    print()
    
    print("2️⃣ Бот не добавлен в канал:")
    print("   • Добавьте бота в канал @DucksNet как администратора")
    print("   • Дайте права на чтение сообщений")
    print()
    
    print("3️⃣ Канал приватный:")
    print("   • Убедитесь, что канал публичный или")
    print("   • Бот имеет доступ к приватному каналу")
    print()
    
    print("=" * 60)
    print("📋 ПЛАН ИСПРАВЛЕНИЯ:")
    print()
    
    print("Шаг 1: Получите правильный ID канала @DucksNet")
    print("  а) Добавьте @userinfobot в канал @DucksNet как админа")
    print("  б) Отправьте любое сообщение в канал")
    print("  в) @userinfobot покажет ID в формате -100XXXXXXXXX")
    print()
    
    print("Шаг 2: Добавьте бота в канал")
    print("  а) Перейдите в канал @DucksNet")
    print("  б) Нажмите 'Администраторы' → 'Добавить администратора'")
    print("  в) Найдите вашего бота и добавьте")
    print("  г) Дайте права: 'Чтение сообщений' (обязательно)")
    print()
    
    print("Шаг 3: Обновите конфигурацию")
    print("  а) Откройте файл .env на сервере")
    print("  б) Замените -1002636737929 на правильный ID")
    print("  в) Перезапустите бота: docker compose restart ducksnet-bot")
    print()
    
    print("Шаг 4: Проверьте работу")
    print("  а) Создайте тестовый аккаунт")
    print("  б) НЕ подписывайтесь на канал")
    print("  в) Запустите бота - должна показаться блокировка")
    print("  г) Подпишитесь на канал и нажмите 'Проверить подписку'")
    print()
    
    print("=" * 60)
    print("🚨 ВРЕМЕННОЕ ОТКЛЮЧЕНИЕ:")
    print()
    print("Если нужно срочно отключить проверку подписки:")
    print("1. В файле .env установите:")
    print("   SHOP_FORCE_SUBSCRIPTION_ENABLED=false")
    print("2. Перезапустите бота:")
    print("   docker compose restart ducksnet-bot")
    print()
    
    print("💡 ПОЛЕЗНЫЕ КОМАНДЫ:")
    print("• Просмотр логов: docker compose logs ducksnet-bot")
    print("• Перезапуск бота: docker compose restart ducksnet-bot")
    print("• Редактирование .env: nano .env")
    print()
    
    # Создаем образец правильной конфигурации
    print("📝 ОБРАЗЕЦ ПРАВИЛЬНОЙ КОНФИГУРАЦИИ (.env):")
    print("-" * 40)
    print("SHOP_FORCE_SUBSCRIPTION_ENABLED=true")
    print("SHOP_FORCE_SUBSCRIPTION_CHANNEL_ID=-100ПРАВИЛЬНЫЙ_ID")  
    print("SHOP_FORCE_SUBSCRIPTION_CHANNEL_USERNAME=DucksNet")
    print("-" * 40)
    print()

if __name__ == "__main__":
    asyncio.run(main())
