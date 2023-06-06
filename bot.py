# bot.py
# This file hold all of the bot's key functions.

import discord
import responses
import random


# This is a dictionary that will update with a username and an initial score of zero as users interact with the bot.
CREDIT_DICT = {}


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "YOURTOKENHERE"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # This print statement exists for the purposes of debugging.
        print(f"{username} said: {user_message}, {channel}")

        # When a user message begins with "?" the bot will send a private message as a response.
        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)

        # The username and a score of zero is appended to CREDIT_DICT.
        if username not in CREDIT_DICT:
            CREDIT_DICT.update({username : 0})
            print(CREDIT_DICT)
        else:
            pass

        # This algorithm scans through a list of responses and will assign points depending on if the word or phrase used is in the good master list or bad master list.
        for i in responses.good_master_list:
            if i in user_message.lower():
                # Points can be assigned randomly here
                add_list = [0, 10, 15, 50, 100]
                sc_number = random.choice(add_list)
                CREDIT_DICT[username] = CREDIT_DICT[username] + sc_number
                print(CREDIT_DICT[username])
        for i in responses.bad_master_list:
            if i in user_message.lower():
                sub_list = [0, -10, -15, -50, -100]
                sc_subtract = random.choice(sub_list)
                CREDIT_DICT[username] = CREDIT_DICT[username] + sc_subtract
                print(CREDIT_DICT[username])
            else:
                pass

    client.run(TOKEN)
