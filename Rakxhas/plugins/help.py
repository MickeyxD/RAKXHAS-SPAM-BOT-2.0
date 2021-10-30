from OpUstad import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS
from telethon import events, Button

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

@UstaD.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.inline("🔰HELP MENU🔰",data="help")]
                    ])

@UstaD.on(events.callbackquery.CallbackQuery(data="help"))
async def ex(event):
    await event.edit("HERE IS HELP MENU OF DEADLY SPAM BOT 2.0",
                    buttons=[
                        [Button.inline("🔰SPAM🔰",data="spam")],
                        [Button.inline("🔰BIGSPAM🔰",data="help")],
                        [Button.inline("🔰RAID🔰",data="help")]
                    ])

@UstaD.on(events.callbackquery.CallbackQuery(data="spam"))
async def ok(event):
    await event.reply("spam", "<number> <text>", "Sends the text 'X' number of times.", "spam 99 Hello")
