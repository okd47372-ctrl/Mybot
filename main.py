import telebot

TOKEN = "8612665593:AAHpwY_m-QBOumai8GKG7E_GkVmvViMuUM8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎮 *Crash Game Assistant*\n\n/predict <পয়েন্ট>\n/risk <ব্যালেন্স>\n/strategy", parse_mode="Markdown")

@bot.message_handler(commands=['predict'])
def predict_crash(message):
    input_text = message.text.split()[1:]
    if not input_text:
        bot.reply_to(message, "❌ পয়েন্ট দাও। যেমন: /predict 1.8 2.5")
        return
    try:
        points = [float(x) for x in input_text]
        avg = sum(points) / len(points)
        safe_target = round(1.1 + (avg * 0.1), 2)
        if safe_target > 1.45: safe_target = 1.45
        bot.reply_to(message, f"🎯 *Safe Cashout:* `{safe_target}x`", parse_mode="Markdown")
    except ValueError:
        bot.reply_to(message, "❌ শুধু সংখ্যা দাও।")

@bot.message_handler(commands=['risk'])
def risk_calculator(message):
    input_text = message.text.split()[1:]
    if not input_text:
        bot.reply_to(message, "❌ ব্যালেন্স দাও। যেমন: /risk 500")
        return
    try:
        balance = float(input_text[0])
        bot.reply_to(message, f"🟢 *Low Risk (2%):* `{round(balance * 0.02, 2)}` (Target: 1.5x)", parse_mode="Markdown")
    except ValueError:
        bot.reply_to(message, "❌ সঠিক সংখ্যা দাও।")

@bot.message_handler(commands=['strategy'])
def send_strategy(message):
    bot.reply_to(message, "🧠 Auto-Cashout (1.3x/1.5x) ব্যবহার করো। টানা ৩ বার হারলে বিরতি নাও।")

print("লাইটওয়েট বট চালু হয়েছে...")
bot.infinity_polling()
