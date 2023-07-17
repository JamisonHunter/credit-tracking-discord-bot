# credit-tracking-discord-bot

Based on an already established Discord chatbot tutorial, I created a bot which can track credits based on what users say in a Discord server. Below is the tutorial I used in order to create the basic framework. The point tracking algorithm is a feature I added overtop. I have the original tutorial posted below for anybody interested. 

https://www.youtube.com/watch?v=1yLfjMtsV9s

The features I added overtop allow for a number of points to be allocated to a username depending on the keyword used. Some words can take points while others can add points. Some words can recieve a response from the bot while giving, taking, or not interacting with points at all. Once points are allocated, they are automatically saved to a local .json file created by the bot. The file saves a dictionary of usernames, their points, and the list can be called by typing "sc" into the chat while the bot is running.
