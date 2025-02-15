import json
import re
import requests
import sqlite3
import asyncio
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import nest_asyncio

nest_asyncio.apply()

user_id = None


def get_product_info(url):
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        original_price_element = soup.find("span", class_="prc-org")
        discounted_price_element = soup.find("span", class_="prc-dsc")

        original_price = original_price_element.text.strip() if original_price_element else None
        discounted_price = discounted_price_element.text.strip() if discounted_price_element else None

        if not original_price and not discounted_price:
            script_tags = soup.find_all("script", text=re.compile('"offers": {'))
            for script in script_tags:
                json_text = re.search(r'({.*"offers": {.*?}})', script.string, re.DOTALL)
                if json_text:
                    try:
                        json_data = json.loads(json_text.group(1))
                        price_info = json_data["offers"]["price"]
                        discounted_price = f"{price_info} TL"
                    except (KeyError, json.JSONDecodeError):
                        pass

        if discounted_price and not original_price:
            original_price = discounted_price
            discounted_price = None

        if original_price:
            original_price_num = float(original_price.replace("TL", "").replace(",", ".").strip())
            discounted_price_num = (float(discounted_price.replace("TL", "").replace(",", ".").strip())
                                    if discounted_price else original_price_num)
            discount_percentage = (((original_price_num - discounted_price_num) / original_price_num) * 100
                                   if discounted_price else 0)
            result = (
                f"📌 Ürün URL: {url}\n"
                f"💰 Orijinal Fiyat: {original_price} TL\n"
                f"🎉 İndirimli Fiyat: {discounted_price if discounted_price else 'İndirim Yok'} TL\n"
                f"📉 İndirim Oranı: %{discount_percentage:.2f}\n"
            )
            return original_price, discounted_price, result
        else:
            return None, None, "❌ Fiyat bilgisi bulunamadı, sayfa yapısını kontrol edin."
    except Exception as e:
        return None, None, f"❌ Bir hata oluştu: {str(e)}"

def create_database():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            url TEXT PRIMARY KEY,
            original_price TEXT,
            discounted_price TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_product_to_db(url, original_price, discounted_price):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO products (url, original_price, discounted_price)
        VALUES (?, ?, ?)
    ''', (url, original_price, discounted_price))
    conn.commit()
    conn.close()

def get_product_from_db(url):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT original_price, discounted_price FROM products WHERE url = ?", (url,))
    product = c.fetchone()
    conn.close()
    return product

async def check_price_changes(application: Application):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    c.execute("SELECT url FROM products")
    products = c.fetchall()
    for product in products:
        url = product[0]
        product_info = get_product_info(url)
        if product_info[0] is not None:
            original_price, discounted_price, _ = product_info
            old_product = get_product_from_db(url)
            if old_product:
                old_original_price, old_discounted_price = old_product
                if old_original_price != original_price or old_discounted_price != discounted_price:
                    message = (
                        f"🔔 Fiyat Değişikliği Bildirimi\n\n"
                        f"📌 Ürün URL: {url}\n"
                        f"💰 Eski Orijinal Fiyat: {old_original_price} TL\n"
                        f"💰 Yeni Orijinal Fiyat: {original_price} TL\n"
                        f"🎉 Eski İndirimli Fiyat: {old_discounted_price} TL\n"
                        f"🎉 Yeni İndirimli Fiyat: {discounted_price} TL\n"
                    )
                    try:
                        discount_percentage = (
                            ((float(original_price.replace("TL", "").strip()) -
                              float(discounted_price.replace("TL", "").strip())) /
                             float(original_price.replace("TL", "").strip())) * 100
                        )
                    except Exception:
                        discount_percentage = 0
                    message += f"📉 İndirim Oranı: %{discount_percentage:.2f}"
                    
                    if user_id:
                        await application.bot.send_message(chat_id=user_id, text=message)
            save_product_to_db(url, original_price, discounted_price)
    conn.close()

async def background_price_check(application: Application):
    while True:
        await check_price_changes(application)
        #debug_message = "Debug Log: Fiyat kontrolü yapıldı."
        #if user_id:
         #   await application.bot.send_message(chat_id=user_id, text=debug_message)
        await asyncio.sleep(60)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba, ben Tickreyiz! Bir ürün URL'si eklemek için /addproduct komutunu kullanın.")

async def add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_id
    if context.args:
        url = context.args[0]
        product_info = get_product_info(url)
        if product_info[0] is not None:
            original_price, discounted_price, result = product_info
            save_product_to_db(url, original_price, discounted_price)
        else:
            result = product_info[2]
        await update.message.reply_text(result)
        user_id = update.effective_chat.id
    else:
        await update.message.reply_text("Lütfen bir Trendyol ürün URL'si girin.")
async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    
    c.execute("DELETE FROM products")
    conn.commit()
    conn.close()

    await update.message.reply_text("Veritabanındaki tüm ürünler başarıyla silindi.")

async def main():
    create_database()

    application = Application.builder().token("YOUR TELEGRAM BOT TOKEN").build()
    application.add_handler(CommandHandler("clear", clear))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("addproduct", add_product))
    asyncio.create_task(background_price_check(application))
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
