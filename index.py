import discord
from python_aternos import Client
from python_aternos import Client, atserver

token = "YOUR_TOKEN"


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        aternos = Client.from_credentials('USERNAME', 'PASSWORD')
        servs = aternos.list_servers()
        myserv = servs[0]

        role = ""

        for r in message.author.roles:
            if str(r) == "Admin":
                role = str(r)

        if message.content == '!launch':
            aternos = Client.from_credentials('USERNAME', 'PASSWORD')
            servs = aternos.list_servers()
            myserv = servs[0]

            if myserv.status == 'online':
                return await client.get_channel(message.channel.id).send('The server is already launched / in launch!')

            myserv.start()
            await client.get_channel(message.channel.id).send("The server is starting! To know more about the progress made !info!")
            await client.get_channel(message.channel.id).send("It should launch in 2-5 minutes ;)")
            for srv in servs:
                await client.get_channel(message.channel.id).send(f"*** {srv.domain} ***\n{srv.motd}\n*** Status: {srv.status}\n*** Full address: {srv.address}\n*** Port: {srv.port}\n*** Name: {srv.subdomain}\n*** Minecraft: {srv.software, srv.version}\n*** IsBedrock: {srv.edition == atserver.Edition.bedrock}\n*** IsJava: {srv.edition == atserver.Edition.java}***")

        if message.content == '!info':
            aternos = Client.from_credentials('USERNAME', 'PASSWORD')
            servs = aternos.list_servers()
            myserv = servs[0]

            print(myserv.status)
            for srv in servs:
                await client.get_channel(message.channel.id).send(f"*** {srv.domain} ***\n{srv.motd}\n*** Status: {srv.status}\n*** Full address: {srv.address}\n*** Port: {srv.port}\n*** Name: {srv.subdomain}\n*** Minecraft: {srv.software, srv.version}\n*** IsBedrock: {srv.edition == atserver.Edition.bedrock}\n*** IsJava: {srv.edition == atserver.Edition.java}***")
        
        if message.content == '!stop':         

            if role == 'Admin':

                if myserv.status == 'offline' or myserv.status == 'loading' or myserv.status == 'stopping' or myserv.status == 'saving':
                    return await client.get_channel(message.channel.id).send("The server is already stopped/stopping :/")
                else:
                    myserv.stop()
                    await client.get_channel(message.channel.id).send("The server is shutting down...")
            else:
                await client.get_channel(message.channel.id).send("You do not have access to this command...")

        if message.content == '!status':

            await client.get_channel(message.channel.id).send(myserv.status)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
