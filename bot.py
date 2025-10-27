import os
import logging
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎉 Бот работает! Финал!")

def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN не найден")
        return
    
    logger.info("✅ BOT_TOKEN найден")
    
    while True:
        try:
            updater = Updater(BOT_TOKEN, use_context=True)
            dispatcher = updater.dispatcher
            
            dispatcher.add_handler(CommandHandler("start", start))
            
            logger.info("🚀 Запускаем бота...")
            updater.start_polling()
            updater.idle()
            
        except Exception as e:
            logger.error(f"❌ Ошибка: {e}")
            logger.info("🔄 Перезапуск через 5 секунд...")
            time.sleep(5)

if __name__ == '__main__':
    main()
