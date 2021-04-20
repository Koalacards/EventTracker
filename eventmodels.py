from peewee import *

database = SqliteDatabase('eventdata.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class EventData(BaseModel):
    approval_channel_id = IntegerField(null=True)
    event_channel_id = IntegerField(null=True)
    guild_id = AutoField(null=True)

    class Meta:
        table_name = 'EventData'

