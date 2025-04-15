import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import xml.etree.ElementTree as ET

intents=discord.Intents.default()
intents.message_content=True
intents.members = True  # 👈 required for on_member_join

Gojo= commands.Bot(command_prefix="",intents=intents,case_insensitive=True)

@Gojo.event
async def on_ready():
    print(f"Gojo is On {Gojo.user}!")
    
@Gojo.command()
async def joke(ctx):
     import requests
     joke = "https://official-joke-api.appspot.com/random_joke"
     response = requests.get(joke)

     if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data.get("setup", "")
        punchline = joke_data.get("punchline", "")
        await ctx.send(f"{setup} 😂\n{punchline}")
     else:
        await ctx.send("Oops! Couldn't fetch a joke right now. Try again later.")
    
@Gojo.command()
async def hi(ctx):
    await ctx.send("Im your Sexy Bot 😂")
@Gojo.command()
async def hey(ctx):
    await ctx.send("Hey Babe! 😎")   
          
@Gojo.command()
async def loveyou(ctx):
    await ctx.send("Bitch Shut The FUck UP! 😂")        

@Gojo.command(aliases=["howru", "hru", "hru1", "hrubot"])
async def howareyou(ctx):
    await ctx.send("I'M FREAKIN' AWESOME, BABE 😎")
    
@Gojo.command()
async def oilup(ctx):
     await ctx.send("Ready to heat up😏 ")  
        
@Gojo.event
async def on_member_join(member):
    channel = Gojo.get_channel(1360665306397413487)
    if channel:
        await channel.send(f"Welcome Dumbass Kiddo {member.mention}! 😂")
        
@Gojo.event
async def on_member_remove(member):
    channel=Gojo.get_channel(1360665306397413487)
    await channel.send(f"Bye AssHole{member.mention}!😂")       
    
    
    
@Gojo.command()
async def define(ctx, word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', 'No example provided.')
        part_of_speech = data[0]['meanings'][0]['partOfSpeech']

        embed = discord.Embed(
            title=f"Definition of '{word}'",
            description=f"**{part_of_speech}**: {meaning}\n\n*Example:* {example}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Sorry, I couldn't find a definition for **{word}**.")

# Replace this with your actual bot token

@Gojo.command(pass_content=True)
async def join(ctx):
    if (ctx.author.voice):
        channel=ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Im Here")
    else:
        await ctx.send("FUCK JOIN!!!")   


@Gojo.command(pass_content=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I fuckin left channel")
    else:
        await ctx.send("IM STILL HERE BABE")

Token = os.getenv("Token")            
Gojo.run(Token)       