# Tickreyiz - Trendyol Fiyat Takip Botu

## 📌 Proje Açıklaması | 📌 Project Description
Tickreyiz, Telegram üzerinden çalışan bir Trendyol fiyat takip botudur. Kullanıcılar, bir ürünün URL'sini ekleyerek fiyat değişikliklerinden haberdar olabilirler. Bot, belirli aralıklarla fiyatları kontrol eder ve bir değişiklik olduğunda kullanıcıya bildirim gönderir. | Tickreyiz is a Telegram-based Trendyol price tracking bot. Users can add a product URL to stay informed about price changes. The bot checks prices at regular intervals and notifies users when changes occur.

---

## 🚀 Kurulum ve Çalıştırma | 🚀 Installation and Execution

### 1️⃣ Gereksinimler | 1️⃣ Requirements
Bu botu çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir: | The following libraries must be installed to run this bot:

```bash
pip install requests beautifulsoup4 python-telegram-bot nest_asyncio
```

Ayrıca, SQLite veritabanı kullanılmaktadır. Python'da varsayılan olarak gelir, ek bir yükleme gerektirmez. | Additionally, SQLite is used as the database, which comes pre-installed with Python.

---

### 2️⃣ Telegram Bot Token Alma | 2️⃣ Obtaining Telegram Bot Token
1. [@BotFather](https://t.me/BotFather) ile Telegram'da bir bot oluşturun. | Create a bot via [@BotFather](https://t.me/BotFather) on Telegram.
2. `/newbot` komutunu kullanarak yeni bir bot oluşturun. | Use the `/newbot` command to create a new bot.
3. Bot'unuz için bir isim ve kullanıcı adı belirleyin. | Choose a name and username for your bot.
4. BotFather size bir **API Token** verecektir. Bu token'ı `YOUR TELEGRAM BOT TOKEN` ile değiştirin. | BotFather will provide an **API Token**. Replace `YOUR TELEGRAM BOT TOKEN` with this token.

---

### 3️⃣ Botu Çalıştırma | 3️⃣ Running the Bot

Python dosyanızı çalıştırarak botu başlatabilirsiniz: | Run your Python file to start the bot:

```bash
python bot.py
```

Bot çalıştığında `/start` komutu ile başlatabilir ve `/addproduct <ürün_url>` komutu ile takip etmek istediğiniz ürünleri ekleyebilirsiniz. | Once the bot is running, use the `/start` command to initialize it and `/addproduct <product_url>` to start tracking a product.

---

## 🛠 Özellikler | 🛠 Features

✅ **Fiyat Takibi:** Trendyol'daki ürünlerin fiyatlarını düzenli aralıklarla kontrol eder. | ✅ **Price Tracking:** Monitors product prices on Trendyol at regular intervals.

✅ **Otomatik Bildirim:** Fiyat değişiklikleri olduğunda Telegram üzerinden bildirim gönderir. | ✅ **Automatic Notifications:** Sends notifications via Telegram when price changes occur.

✅ **SQLite Veritabanı:** Takip edilen ürünlerin bilgilerini saklar. | ✅ **SQLite Database:** Stores tracked product information.

✅ **Kolay Kullanım:** `/addproduct` ile ürün ekleyebilir, `/clear` ile tüm kayıtları silebilirsiniz. | ✅ **Easy to Use:** Add products with `/addproduct`, clear all records with `/clear`.

---

## 📜 Kullanım Komutları | 📜 Usage Commands

| Komut | Açıklama | Command | Description |
|--------|---------|---------|------------|
| `/start` | Botu başlatır ve temel bilgileri verir. | `/start` | Starts the bot and provides basic information. |
| `/addproduct <ürün_url>` | Belirtilen Trendyol ürününün fiyatını takip etmeye başlar. | `/addproduct <product_url>` | Starts tracking the specified Trendyol product's price. |
| `/clear` | Veritabanındaki tüm ürünleri temizler. | `/clear` | Clears all products from the database. |

---

## 📌 Çalışma Mantığı | 📌 Working Mechanism
1. `/addproduct <ürün_url>` komutu ile bir ürün eklenir. | A product is added using the `/addproduct <product_url>` command.
2. Bot, ürünü SQLite veritabanına kaydeder. | The bot saves the product to the SQLite database.
3. **background_price_check** fonksiyonu, her 60 saniyede bir kayıtlı ürünlerin fiyatlarını kontrol eder. | The **background_price_check** function checks the prices of saved products every 60 seconds.
4. Eğer fiyat değişmişse, kullanıcıya Telegram üzerinden bildirim gönderilir. | If a price change is detected, a notification is sent to the user via Telegram.

---

## 💡 Geliştirme Fikirleri | 💡 Future Development Ideas
🔹 Fiyat değişim geçmişinin kaydedilmesi. | 🔹 Storing price change history.

🔹 Kullanıcının takip ettiği ürünleri listeleme komutu. | 🔹 Command to list tracked products.

🔹 Daha fazla e-ticaret sitesinin desteklenmesi. | 🔹 Support for more e-commerce websites.

---

## 📌 Lisans | 📌 License
Bu proje açık kaynaklıdır. İstediğiniz gibi geliştirebilir ve paylaşabilirsiniz. | This project is open-source. You are free to modify and share it as you wish.

