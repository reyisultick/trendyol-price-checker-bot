---

Trendy - Trendyol Fiyat Takip Botu

📌 Proje Açıklaması | 📌 Project Description

Trendy, Telegram üzerinden çalışan bir Trendyol fiyat takip botudur. Kullanıcılar, bir ürünün URL'sini ekleyerek fiyat değişikliklerinden haberdar olabilirler. Bot, belirli aralıklarla fiyatları kontrol eder ve bir değişiklik olduğunda kullanıcıya bildirim gönderir. | Trendy is a Telegram-based Trendyol price tracking bot. Users can add a product URL to stay informed about price changes. The bot checks prices at regular intervals and notifies users when changes occur.


---

🚨 Yasal Uyarılar | Legal Notice 🚨

Bu botun kullanımı, Trendyol’un hizmet şartlarına ve ilgili yasalara tabidir. Web kazıma (scraping) yapmak, birçok e-ticaret platformunun kullanım koşullarına aykırıdır ve yasal sonuçlar doğurabilir. Aşağıdaki uyarılara dikkat etmeniz önemlidir:
The use of this bot is subject to Trendyol's terms of service and applicable laws. Web scraping may violate the terms of use of many e-commerce platforms and can lead to legal consequences. Please pay attention to the following warnings:

Hizmet Şartları İhlali: Bu bot, Trendyol'un kullanım şartlarını ihlal edebilir. Trendyol, otomatik veri çekme işlemleri için erişimi kısıtlayabilir veya engelleyebilir. Botu kullanmadan önce Trendyol'un hizmet şartlarını dikkatlice okumanız gerekmektedir. | Violation of Terms of Service: This bot may violate Trendyol's terms of service. Trendyol may restrict or block access for automated data scraping. Please read Trendyol's terms of service carefully before using the bot.

Yasal Sorumluluk: Bu bot, sadece eğitim amaçlı sunulmaktadır. Kullanıcılar, botu kullanırken yasalara uygun hareket etmelidir. Verilerin toplandığı siteye zarar vermek veya telif hakkı ihlali oluşturmak gibi faaliyetler, yasal sorumluluk doğurabilir. | Legal Responsibility: This bot is provided for educational purposes only. Users must comply with applicable laws when using the bot. Activities such as causing harm to the website or violating copyright laws can lead to legal responsibility.

Veri Koruma ve Gizlilik: Eğer bot, kişisel veriler veya kullanıcı yorumları gibi özel veriler topluyorsa, bu durum veri gizliliği yasalarına (örneğin GDPR) aykırı olabilir. Kişisel verilerin toplanması ve işlenmesiyle ilgili olarak yerel yasalara dikkat edilmelidir. | Data Protection and Privacy: If the bot collects personal data or user comments, it may violate data protection laws (such as GDPR). Users should comply with local laws related to the collection and processing of personal data.

Alternatif Yöntemler: Eğer Trendyol, botlar için bir API sunuyorsa, bu API kullanılarak veri çekmek, hem yasal hem de etik olarak daha güvenli bir yöntemdir. | Alternative Methods: If Trendyol offers an API for bots, using the API to collect data is a safer and more ethical method.



---

🚀 Kurulum ve Çalıştırma | 🚀 Installation and Execution

1️⃣ Gereksinimler | 1️⃣ Requirements

Bu botu çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir: | The following libraries must be installed to run this bot:

pip install requests beautifulsoup4 python-telegram-bot nest_asyncio

Ayrıca, SQLite veritabanı kullanılmaktadır. Python'da varsayılan olarak gelir, ek bir yükleme gerektirmez. | Additionally, SQLite is used as the database, which comes pre-installed with Python.


---

2️⃣ Telegram Bot Token Alma | 2️⃣ Obtaining Telegram Bot Token

1. Telegram'da @BotFather ile yeni bir bot oluşturun. | Create a new bot via @BotFather on Telegram.


2. /newbot komutunu kullanarak yeni bir bot oluşturun. | Use the /newbot command to create a new bot.


3. Bot'unuz için bir isim ve kullanıcı adı belirleyin. | Choose a name and username for your bot.


4. BotFather size bir API Token verecektir. Bu token'ı YOUR TELEGRAM BOT TOKEN ile değiştirin. | BotFather will provide an API Token. Replace YOUR TELEGRAM BOT TOKEN with this token.




---

3️⃣ Botu Çalıştırma | 3️⃣ Running the Bot

Python dosyanızı çalıştırarak botu başlatabilirsiniz: | Run your Python file to start the bot:

python bot.py

Bot çalıştığında /start komutu ile başlatabilir ve /addproduct <ürün_url> komutu ile takip etmek istediğiniz ürünleri ekleyebilirsiniz. | Once the bot is running, use the /start command to initialize it and /addproduct <product_url> to start tracking a product.


---

🛠 Özellikler | 🛠 Features

✅ Fiyat Takibi: Trendyol'daki ürünlerin fiyatlarını düzenli aralıklarla kontrol eder. | ✅ Price Tracking: Monitors product prices on Trendyol at regular intervals.

✅ Otomatik Bildirim: Fiyat değişiklikleri olduğunda Telegram üzerinden bildirim gönderir. | ✅ Automatic Notifications: Sends notifications via Telegram when price changes occur.

✅ SQLite Veritabanı: Takip edilen ürünlerin bilgilerini saklar. | ✅ SQLite Database: Stores tracked product information.

✅ Kolay Kullanım: /addproduct komutu ile ürün ekleyebilir, /clear komutu ile tüm kayıtları silebilirsiniz. | ✅ Easy to Use: Add products with /addproduct, clear all records with /clear.


---

📜 Kullanım Komutları | 📜 Usage Commands


---

📌 Çalışma Mantığı | 📌 Working Mechanism

1. /addproduct <ürün_url> komutu ile bir ürün eklenir. | A product is added using the /addproduct <product_url> command.


2. Bot, ürünü SQLite veritabanına kaydeder. | The bot saves the product to the SQLite database.


3. background_price_check fonksiyonu, her 60 saniyede bir kayıtlı ürünlerin fiyatlarını kontrol eder. | The background_price_check function checks the prices of saved products every 60 seconds.


4. Eğer fiyat değişmişse, kullanıcıya Telegram üzerinden bildirim gönderilir. | If a price change is detected, a notification is sent to the user via Telegram.




---

💡 Geliştirme Fikirleri | 💡 Future Development Ideas

🔹 Fiyat değişim geçmişinin kaydedilmesi: Kullanıcılar, geçmiş fiyat değişimlerini inceleyebilir. | 🔹 Storing price change history: Users can review the historical price changes.

🔹 Kullanıcının takip ettiği ürünleri listeleme komutu: Kullanıcılar, takip ettikleri ürünlerin listesini görebilir. | 🔹 Command to list tracked products: Users can view a list of their tracked products.

🔹 Daha fazla e-ticaret sitesinin desteklenmesi: Bot, başka e-ticaret sitelerinden de veri çekebilir. | 🔹 Support for more e-commerce websites: The bot could support tracking prices from additional e-commerce platforms.


---

📌 Lisans | 📌 License

Bu proje açık kaynaklıdır. İstediğiniz gibi geliştirebilir ve paylaşabilirsiniz. | This project is open-source. You are free to modify and share it as you wish.


---
