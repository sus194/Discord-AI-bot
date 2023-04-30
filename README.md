README.md:

# Discord-AI-bot

This is a simple chatbot that can perform a few different tasks based on the user's input.

## Dependencies

The following dependencies are required to run this chatbot:

- Python 3.7 or higher
- SymPy library
- OpenAI library
- Requests library

## Installation

1. Clone this repository onto your local machine.
2. Install the required dependencies using pip:

```
pip install sympy openai requests
```

3. Make sure you have the Stock API key and AI API key. 
4. Set environment variables named `STOCK_API_KEY` and `AI_API_KEY` with your keys.

## Usage

Run the `sukhrajai.py` script to start the chatbot. 

The discordbot can perform the following tasks:

- **Chess moves**: The discordbot can suggest the best move in a given chess position. It uses the Stockfish chess engine for this task. This functionality is provided by `chess_response.py`.
- **Math calculations**: The discordbot can solve simple math expressions. This functionality is provided by `math_response.py`.
- **Stock prices**: The chatbot can retrieve the current stock price for a given stock symbol. It uses the Alpha Vantage API for this task. This functionality is provided by `response_stock.py`.
- **AI-generated responses**: The discordbot can generate a response to a prompt using OpenAI's GPT-3 model. This functionality is provided by `responseai.py`.
- **Weather responses**: The discordbot can retrieve the current weather of any location given the name of the city and the country.

### How to use

To use the bot, you must invite it to your Discord server and provide an environment variable `DISCORD_TOKEN` which contains the Discord bot token. 

You can interact with the bot using the following commands:

* `!chess [move]` - Play chess with the bot. Replace `[move]` with the move you want to make. You can also resign by typing `!chess resign`.
* `!math [expression]` - Perform a mathematical calculation. Replace `[expression]` with the expression you want to evaluate.
* `!weather [city] [country]` - Get the temperature for a city in a given country. Replace `[city]` with the name of the city and `[country]` with the name of the country.
* `!stock [symbol]` - Get the current stock price for a given symbol. Replace `[symbol]` with the stock symbol.
* `!chat [message]` - Chat with the bot. Replace `[message]` with the message you want to send.
* `!zeus [command]` - Admin-only command for managing messages. Replace `[command]` with one of the following:
  * `delete` - Deletes the most recent message in the channel and the bot's two previous messages.
  * `edit [message ID] [new content]` - Edits the message with the specified ID to have the specified content.


## Code Structure

The code is structured as follows:

- `chatbot.py`: This is the main script that handles user input and dispatches tasks to the appropriate response module.
- `chess_response.py`: This module provides the functionality for suggesting chess moves using the Stockfish chess engine.
- `math_response.py`: This module provides the functionality for solving math expressions.
- `response_stock.py`: This module provides the functionality for retrieving stock prices using the Alpha Vantage API.
- `responseai.py`: This module provides the functionality for generating AI-generated responses using OpenAI's GPT-3 model.

## Contributors

- Sukhraj Purewal
- Your Name Here (Feel free to add yourself if you make a contribution!)

