from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
• 𝙑𝙘 𝙋𝙡𝙖𝙮𝙚𝙧 • 𝙄𝙨 𝙎𝙪𝙥𝙚𝙧 𝘿𝙪𝙥𝙚𝙧 𝘽𝙤𝙩 𝙁𝙤𝙧 𝙑𝙘 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮. 𝙁𝙚𝙚𝙡 𝙏𝙝𝙚 𝙎𝙤𝙣𝙜 𝙌𝙪𝙖𝙡𝙞𝙩𝙮 𝙒𝙞𝙩𝙝 𝙃𝙞𝙜𝙝 𝘿𝙚𝙛𝙞𝙣𝙖𝙩𝙞𝙤𝙣𝙨. [𝙂𝙧𝙤𝙪𝙥](https://t.me/Pyar_China_Ka_Maal_Hai).
𝘼𝙙𝙙 𝙈𝙚 𝙏𝙤 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 𝘼𝙣𝙙 𝙋𝙡𝙖𝙮 𝙈𝙪𝙨𝙞𝙘 𝙁𝙧𝙚𝙚 𝙊𝙛 𝘾𝙤𝙨𝙩 💜🤞**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝙊𝙬𝙣𝙚𝙧❱", url="https://t.me/its_Nitric")
                  ],[
                    InlineKeyboardButton(
                        "❰𝙎𝙪𝙥𝙥𝙤𝙧𝙩❱", url="https://t.me/Pyar_China_Ka_Maal_Hai"
                    ),
                    InlineKeyboardButton(
                        "❰𝙂𝙧𝙤𝙪𝙥❱", url="https://t.me/Pyar_China_Ka_Maal_Hai"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥❱", url="https://t.me/TgVcPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝙊𝙣𝙡𝙞𝙣𝙚 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝙐𝙥𝙙𝙖𝙩𝙚𝙨", url="https://t.me/Pyar_China_Ka_Maal_Hai")
                ]
            ]
        )
   )
