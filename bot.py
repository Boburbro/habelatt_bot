import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from flask import Flask, request, abort
import config

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Flask app
app = Flask(__name__)

# Echo message handler
@dp.message(F.text)
async def echo(message: types.Message):
    await message.answer(message.text)

# Process webhook calls
@app.route(config.WEBHOOK_PATH, methods=['POST'])
async def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_update = request.json
        update = types.Update.model_validate(json_update)
        await dp.feed_update(bot=bot, update=update)
        return '', 200
    else:
        abort(403)

@app.route("/", methods=['GET'])
async def webhook():
    return "WORKING !!"

# Setup webhook
async def on_startup():
    await bot.set_webhook(config.WEBHOOK_URL)
    
# Remove webhook
async def on_shutdown():
    await bot.delete_webhook()

# Start the Flask application
if __name__ == '__main__':
    # Start webhook setup first
    asyncio.run(on_startup())
    # Start Flask server
    app.run(host=config.WEBAPP_HOST, port=config.WEBAPP_PORT) 