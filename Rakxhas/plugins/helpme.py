from telethon import events, Button
from OpUstad import UstaD

BOT_T = '1915833103:AAHmiMi1rcBxP245np1WX_rSF10ygf10-1w'

@UstaD.on(events.NewMessage(pattern="/helpme"))
async def helpme(event):
  try:
    tgbotusername = BOT_T
    is BOT_T is not None:
      results = await event.client.inline_query(tgbotusername, '@xDSmex_bot')
      await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
      else:
        event.reply('The bot is not working! Please set Bot Token and Username correctly. The module has been discontinued.')
        
