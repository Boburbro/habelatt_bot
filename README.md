# Telegram Echo Bot with Webhook

A simple Telegram echo bot using aiogram and Flask webhooks.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure the bot:
   - Open `config.py` and replace `YOUR_TELEGRAM_BOT_TOKEN` with your actual Telegram bot token from BotFather
   - Update the `WEBHOOK_HOST` with your domain or public IP

3. Start the bot:
```bash
python bot.py
```

## Features

- Webhook-based Telegram bot
- Echo functionality (repeats back any messages received)
- Integrated Flask and aiogram 