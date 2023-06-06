# responses.py
# This file holds lists of responses and lists of words that the bot searches for. 

import random
import bot

# The following are two lists; one for wors that increase points and one for decreasing points.
good_admin_list = ["good"]
bad_admin_list = ["bad"]

# The following two lists will add and subtract points but will also get a reply from the bot.
best_admin_list = ["best"]
worst_admin_list = ["worst"]

# The master lists are established below. 
good_master_list = good_admin_list + best_admin_list
bad_master_list = bad_admin_list + worst_admin_list

def get_response(message: str) -> str:
    p_message = message.lower()
    
    # If a user types "sc" then the bot will state the current scores. 
    if p_message == "sc":
        return str(bot.CREDIT_DICT)
      
    # The bot will send a reply if the word was in the best_admin_list.
    for i in best_admin_list:
        if i in p_message:
            return "YOu have gained credits!"
          
    for i in worst_admin_list:
        if i in p_message:
            return "YOu have lost credits!"
    
    # This will return a link to the tutorial used as a framework for this bot.
    if p_message == "tutorial":
        return "https://www.youtube.com/watch?v=1yLfjMtsV9s"
    
    if p_message == "rolld4":
        return str(random.randint(1, 4))

    if p_message == "rolld6":
        return str(random.randint(1, 6))

    if p_message == "rolld10":
        return str(random.randint(1, 10))

    if p_message == "rolld20":
        return str(random.randint(1, 20))
