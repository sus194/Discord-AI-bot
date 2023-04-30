
import os
import math_response
import response_stock
import chess_response
import responseai

import discord
import requests
from discord.ext import commands
import chess
import chess.svg

import svgwrite


intents = discord.Intents().default()
intents.members = True
intents.message_content = True
intents.guild_messages = True
intents.guild_typing = True
SQUARE_SIZE = 50
BOARD_SIZE = SQUARE_SIZE * 8
bot = commands.Bot(command_prefix='!',intents=intents)
chess_start = False
board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
svg_document = svgwrite.Drawing(filename="chess.svg", size=(BOARD_SIZE, BOARD_SIZE))
svg_document.save()

@bot.command(name='chess')
async def math(ctx,move:str):
    global chess_start
    global board
    if(move == "resign"):
        await ctx.send("good game")
        chess_start = False
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    else:
        print(chess_start)
        if( not chess_start):
            if(move == "white"):
                chess_start = True
                botmove = chess.Move.from_uci(chess_response.make_move(board.fen()))
                board.push(botmove)
                await ctx.send("lets start")

                await ctx.send(botmove)
        
            elif move == "black":
                chess_start = True
                await ctx.send("lets start")

            else:
                await ctx.send("please make the correct moves")
        
        else:
            urmove = chess.Move.from_uci(move)
            if(board.is_legal(urmove)):
                board.push(urmove)
                if(not board.is_game_over()):
                    botmove = chess.Move.from_uci(chess_response.make_move(board.fen()))
                    board.push(botmove)
                    
                    
                    await ctx.send(botmove)
                    if(board.is_game_over()):
                        await ctx.send("well checkmate")
                        
                        chess_start = False
                        
                        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
                
                else:
                    await ctx.send("good.....very good")
                    
                    chess_start = False
                    
                    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

            else:
                await ctx.send("put the right input please")
        
    
    
        
    return
    
@bot.command(name='weather')
async def weather(ctx,city:str,country:str):
        url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

        querystring = {"city":city,"country":country}

        headers = {
            "X-RapidAPI-Key": os.environ['Weather_API_KEY'],
            "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()

            
            temperature = data['temp']

            
            await ctx.send(f'The temperature in {city} is {temperature}°C')
        else:
            await ctx.send(f'Failed to retrieve weather information for {city}')


@bot.command(name= 'math')
async def math(ctx,*,expression:str):
        expression = math_response.parse_expression(expression)
        if expression:
            result = math_response.perform_calculation(expression)
            await ctx.send(result)
        else:
            await ctx.send("Invalid expression.")

@bot.command(name= 'chat')
async def chat(ctx,*,chat:str):
    if ctx.message.author.id == os.environ['AUTH_ID']:
        response = responseai.get_response("!chat "+chat)
        await ctx.send(response)
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command(name='stock')
async def stock(ctx, symbol:str):
    price = response_stock.get_stock_price(symbol)
    await ctx.send(f"The current price of {symbol} is {price}")

@bot.command(name="zeus")
async def my_command(ctx,*,command:str):
    
    if ctx.message.author.id == os.environ['AUTH_ID']:
        
        if command == "delete":
            await ctx.message.delete()
            async for msg in ctx.message.channel.history(limit=3):
                if msg.id != ctx.message.id:
                    await msg.delete()
        
        if command[:4] == "edit":
            print("hi")
            async for msg in ctx.message.channel.history(limit=5):
                print(msg.id)
                if str(msg.id) == command[5:len(str(msg.id))+5]:
                    print(msg.content)
                    await msg.edit(content='New content!')
                    #await msg.edit(content= command[len(str(msg.author))+6:])
                    break

    else:
        await ctx.send("You do not have permission to use this command.")


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

@bot.event
async def on_message(message):
    '''
    if message.content == "!chess":
                new_worker = multiprocessing.Process(target=start_bot_process, args=(queue,))
                new_worker.start()
                global workers
                workers[message.author.id] = new_worker
                await message.channel.send("ok lets start tell me which side I am playing")
    '''
    substring = message.content.lower().split()
    single = "".join(substring)
    if "andrew" in single or "tate" in single:    
        await message.delete()
    elif message.content.startswith('!'):
        await bot.process_commands(message)
    
           

   

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Please try again.")



bot.run(os.environ['BOT_KEY'])