from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
โข ๐๐ ๐๐ก๐๐ฎ๐๐ง โข ๐๐จ ๐๐ช๐ฅ๐๐ง ๐ฟ๐ช๐ฅ๐๐ง ๐ฝ๐ค๐ฉ ๐๐ค๐ง ๐๐ ๐๐ช๐จ๐๐ ๐๐ก๐๐ฎ. ๐๐๐๐ก ๐๐๐ ๐๐ค๐ฃ๐ ๐๐ช๐๐ก๐๐ฉ๐ฎ ๐๐๐ฉ๐ ๐๐๐๐ ๐ฟ๐๐๐๐ฃ๐๐ฉ๐๐ค๐ฃ๐จ. [๐๐ง๐ค๐ช๐ฅ](https://t.me/Pyar_China_Ka_Maal_Hai).
๐ผ๐๐ ๐๐ ๐๐ค ๐๐ค๐ช๐ง ๐๐ง๐ค๐ช๐ฅ ๐ผ๐ฃ๐ ๐๐ก๐๐ฎ ๐๐ช๐จ๐๐ ๐๐ง๐๐ ๐๐ ๐พ๐ค๐จ๐ฉ ๐๐ค**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โฐ๐๐ฌ๐ฃ๐๐งโฑ", url="https://t.me/its_Nitric")
                  ],[
                    InlineKeyboardButton(
                        "โฐ๐๐ช๐ฅ๐ฅ๐ค๐ง๐ฉโฑ", url="https://t.me/Pyar_China_Ka_Maal_Hai"
                    ),
                    InlineKeyboardButton(
                        "โฐ๐๐ง๐ค๐ช๐ฅโฑ", url="https://t.me/Pyar_China_Ka_Maal_Hai"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "โฐ๐ผ๐๐ ๐๐ ๐๐ฃ ๐๐ค๐ช๐ง ๐๐ง๐ค๐ช๐ฅโฑ", url="https://t.me/TgVcPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**๐๐ฃ๐ก๐๐ฃ๐ โ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ ๐๐ฅ๐๐๐ฉ๐๐จ", url="https://t.me/Pyar_China_Ka_Maal_Hai")
                ]
            ]
        )
   )
