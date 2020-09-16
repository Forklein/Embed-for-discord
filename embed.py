from discord_webhook import DiscordWebhook, DiscordEmbed
import sys

licenze = input('Inserisci la licenza ')
if licenze == ('betaforklein'):
    print(' La licenza è corretta')
else:
    print(' La licenza inserita non è corretta')
    sys.exit()


print(r'''Apuliaresell Embed made by Forklein''')

ollare = input('Inserisci il tuo webhook: ')
print('Il tuo webhook è ' + ollare )
hex_list = input('Inserisci un colore ad 8 cifre: ')
print('Il colore scelto è ' + hex_list )
webhook = DiscordWebhook(url= ollare)
embed = DiscordEmbed(title='',
                     description='**EMBED SENDER**\n\n[***APULIARESELL***](https://www.apuliaresell.com)',
                     color=(hex_list)
                     )
embed.set_author(name='Forklein Bot',icon_url='')
embed.set_image(url='')
embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/649901064472100874/696424164503847052/Logo_Circle.png')
embed.set_footer(text=f'Apulia Resell',icon_url='https://cdn.discordapp.com/attachments/649901064472100874/696424164503847052/Logo_Circle.png')
embed.set_timestamp()
embed.add_embed_field(name='[TEST]', value='Test', inline='false')
embed.add_embed_field(name='[TEST]', value='Test [[**Test**]](https://www.apuliaresell.com)', inline='false')
webhook.add_embed(embed)
response = webhook.execute()
print('Embed inviato correttamente')