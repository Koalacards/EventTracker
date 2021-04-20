import discord
import eventdbfunctions

def _checkChannelsSetUp(guild_id):
    return eventdbfunctions.get_approval_channel(guild_id) is not None and eventdbfunctions.get_events_channel(guild_id) is not None
    

def _welcomeEmbed():
    embed = discord.Embed(
        title="Set a Title",
        description="Welcome to the event creation process! First, please provide a title for your event.",
        colour=discord.Color.orange()
    )
    embed.set_footer(text="You can cancel this process at anytime by typing \"cancel\"! This process will timeout in 5 minutes if nothing is entered.")
    return embed

def _desciptionEmbed():
    embed = discord.Embed(
        title="Set a Description",
        description="Excellent! Now, give a description of your event! (Tell everyone what the event will be, what group it is part of, etc!)",
        colour=discord.Color.gold()
    )
    embed.set_footer(text="You can cancel this process at anytime by typing \"cancel\"! This process will timeout in 5 minutes if nothing is entered.")
    return embed

def _timeEmbed():
    embed = discord.Embed(
        title="Set a Date and Time",
        description="Awesome! Now, tell me when your event will happen, both the date and time with timezone included! For example: \"May 5th at 8 PM EST\".",
        colour=discord.Color.purple()
    )
    embed.set_footer(text="You can cancel this process at anytime by typing \"cancel\"! This process will timeout in 5 minutes if nothing is entered.")
    return embed

def _imageEmbed():
    embed = discord.Embed(
        title="Set an image",
        description="Fantastic! Now, add an event image by sending a URL below. This is heavily suggested but not required. If you would not like to add an image, type `skip`.",
        colour=discord.Color.blue()
    )
    embed.set_footer(text="You can cancel this process at anytime by typing \"cancel\"! This process will timeout in 5 minutes if nothing is entered.")
    return embed

def _allSetEmbed():
    embed = discord.Embed(
        title="All set?",
        description="If everything in the preview is to your liking, type in any message! If you would like to redo something, type \"cancel\".",
        colour=discord.Color.blue()
    )
    return embed

def _doneEmbed():
    embed = discord.Embed(
        title="All set!",
        description="You are all good to go! Your event details will be reviewed by a moderator and will be put in the events channel if approved!",
        colour=discord.Color.green()
    )
    return embed

