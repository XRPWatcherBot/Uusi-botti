import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# --- Päävalikko ---
def main_menu():
    keyboard = [
        [InlineKeyboardButton("📈 Price", callback_data="price"),
         InlineKeyboardButton("🔔 Set Alert", callback_data="alert")],
        [InlineKeyboardButton("💰 Balance", callback_data="balance"),
         InlineKeyboardButton("🧾 Trustlines", callback_data="trustlines")],
        [InlineKeyboardButton("📊 Top Gainers", callback_data="gainers"),
         InlineKeyboardButton("📉 Top Losers", callback_data="losers")],
        [InlineKeyboardButton("ℹ️ Token Info", callback_data="info"),
         InlineKeyboardButton("🔄 Trade", callback_data="trade")],
        [InlineKeyboardButton("🟢 Buy XRP", callback_data="buy"),
         InlineKeyboardButton("🔴 Sell XRP", callback_data="sell")],
        [InlineKeyboardButton("✏️ Custom Trade", callback_data="custom_trade")],
        [InlineKeyboardButton("⭐ Bookmark Token", callback_data="bookmark")],
        [InlineKeyboardButton("🔎 Search Token", callback_data="search")],
        [InlineKeyboardButton("🧾 Wallet Overview", callback_data="overview"),
         InlineKeyboardButton("📊 PnL", callback_data="pnl")],
        [InlineKeyboardButton("🌐 Open Portal", url="https://firstledger.xyz")],
        [InlineKeyboardButton("👛 Open Wallet", callback_data="wallet")]
    ]
    return InlineKeyboardMarkup(keyboard)

# --- Start-komento ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to **XRPL Watcher Bot**!\nChoose an action below:",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# --- Napinpainallusten käsittely ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    response_map = {
        "price": "Usage: /price CULT",
        "alert": "Set alert with: `/setalert CULT 0.01`",
        "balance": "Balance coming soon.",
        "trustlines": "Trustlines info coming soon.",
        "gainers": "Top Gainers:\nTOKEN1 +50%, TOKEN2 +30%",
        "losers": "Top Losers:\nTOKEN3 -40%, TOKEN4 -20%",
        "info": "Token info here.",
        "trade": "Trading UI coming soon.",
        "buy": "Choose amount to buy: 10 / 25 / 50 XRP",
        "sell": "Choose amount to sell: 10 / 25 / 50 XRP",
        "custom_trade": "Send amount manually. Ex: /buy CULT 17",
        "bookmark": "Token added to bookmarks.",
        "search": "Send token name or address to search.",
        "overview": "Wallet Overview:\nXRP: 35\nCULT: 1982\nXEN: 45000",
        "pnl": "Realized PnL: +23%\nUnrealized PnL: -5%",
        "wallet": "Your address:\nrDijigo1MiY18TVVQzHqZg2JBXWgf5kQKV"
    }

    msg = response_map.get(data, "Unknown action.")
    await query.edit_message_text(text=msg, parse_mode="Markdown")

# --- Botin käynnistys ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    print("✅ XRPL Watcher Bot is running...")
    app.run_polling()
