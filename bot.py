# bot.py
# This file hold all of the bot's key functions.

# Imports
import discord
import responses
import random
import json
import os

CREDIT_DICT = {}

file_path = "data.json"

def is_file_empty(file_path):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    # Check if file exist and it is empty
    return os.path.exists(file_path) and os.stat(file_path).st_size == 0

if os.path.exists("data.json"):
    is_empty = is_file_empty(file_path)
    print("json file exists.")
    with open("data.json", "r") as json_file:
        if is_empty:
            pass
        else:
            CREDIT_DICT = json.load(json_file)
else:
    pass

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTExMzI1OTI3ODY1MjkzMjExNg.Guaq1R.n7UOwoS0zzzwjkKEk-GyD3kGpkPaM174EP5kQE"
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

        print(f"{username} said: {user_message}, {channel}")

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private = True)
        else:
            await send_message(message, user_message, is_private = False)

        # implementing credit system for users who interact with the bot
        if username not in CREDIT_DICT:
            CREDIT_DICT.update({username : 0})
            print(CREDIT_DICT)
        else:
            pass

        # credit algorithm
        for i in responses.good_master_list:
            if i in user_message.lower():
                add_list = [0, 10, 15, 50, 100]
                sc_number = random.choice(add_list)
                CREDIT_DICT[username] = CREDIT_DICT[username] + sc_number
                print(CREDIT_DICT[username])
                with open("data.json", "w") as json_file:
                    json.dump(CREDIT_DICT, json_file)
        for i in responses.bad_master_list:
            if i in user_message.lower():
                sub_list = [0, -10, -15, -50, -100]
                sc_subtract = random.choice(sub_list)
                CREDIT_DICT[username] = CREDIT_DICT[username] + sc_subtract
                print(CREDIT_DICT[username])
                with open("data.json", "w") as json_file:
                    json.dump(CREDIT_DICT, json_file)
            else:
                pass

    client.run(TOKEN)
