import peewee
from eventmodels import *

def set_events_channel(guild_id:int, channel_id:int):
    guild_query=EventData.select().where(EventData.guild_id == guild_id)
    if len(guild_query) == 0:
        EventData.create(guild_id=guild_id, event_channel_id=channel_id)
    elif len(guild_query) == 1:
        for query in guild_query:
            query.event_channel_id = channel_id
            query.save()
    else:
        print('There is more than one result for the guild')

def set_approval_channel(guild_id:int, channel_id:int):
    guild_query=EventData.select().where(EventData.guild_id == guild_id)
    if len(guild_query) == 0:
        EventData.create(guild_id=guild_id, approval_channel_id=channel_id)
    elif len(guild_query) == 1:
        for query in guild_query:
            query.approval_channel_id = channel_id
            query.save()
    else:
        print('There is more than one result for the guild')

def get_events_channel(guild_id:int):
    guild_query=EventData.select().where(EventData.guild_id == guild_id)
    if len(guild_query) == 0:
        return None
    elif len(guild_query) == 1:
        for query in guild_query:
            return query.event_channel_id

def get_approval_channel(guild_id:int):
    guild_query=EventData.select().where(EventData.guild_id == guild_id)
    if len(guild_query) == 0:
        return None
    elif len(guild_query) == 1:
        for query in guild_query:
            return query.approval_channel_id