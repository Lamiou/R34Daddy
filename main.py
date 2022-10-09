import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # On ne veux pas que le bot se réponde a lui même
        if message.author.id == self.user.id:
            return

        """Début bloc debut Intégration """

        if message.content!= '!hello' :
            print('1')
            print(str(message.content))

        """Fin Bloc Intégration """

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            print(str(message.content))

client = MyClient(intents=discord.Intents.default())

client.run('MTAyMDM0ODcxODEwMjM1NjEwOQ.G_xNvi.Oe9UYG-kdAKa4cA4KTuNTwOTgnir3EkdcNaxIg')
