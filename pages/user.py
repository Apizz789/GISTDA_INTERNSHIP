from channels.generic.websocket import AsyncWebSocketConsumer

class TLE_user(AsyncWebSocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('TLE',self.channel_name)
        await self.accept()
    
    async def disconnect(self):
        await self.channel_layer.group_dicard('TLE',self.channel_name)
        await self.accept()
    
    async def send_TLE(self,event):
        text_massage=event['text']
        
        await self.send(text_massage)