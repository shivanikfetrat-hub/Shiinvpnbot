from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 خرید VPN", callback_data='buy')],
        [InlineKeyboardButton("📦 پلن‌ها", callback_data='plans')],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data='support')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "به فروشگاه Shinvpn خوش آمدید 🌐\nیکی از گزینه‌ها را انتخاب کنید:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(8042783458:AAH4Hds3HswTws5BSMu1cCR9A0Y4wyNFIPw).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
