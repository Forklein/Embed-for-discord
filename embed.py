from discord_webhook import DiscordWebhook, DiscordEmbed
import sys

licenze = input('Inserisci la licenza ')
if licenze == ('betaforklein'):
    print('La licenza è corretta')
else:
    print('La licenza inserita non è corretta')
    sys.exit()


print(r'''Embed Sender made by Forklein''')

ollare = input('Inserisci il tuo webhook: ')
print('Il tuo webhook è ' + ollare )
hex_list = input('Inserisci un colore ad 8 cifre: ')
print('Il colore scelto è ' + hex_list )
titolo = input('Inserisci il titolo: ')
print('Il titolo è ' + titolo )
descrizione = input('Inserisci la descrizione: ')
print('La descrizione è ' + descrizione )
autore = input('Inserisci autore: ')
print('Autore è ' + autore )
immagine = input('Inserisci url dell immagine: ')
print('Immagine è ' + immagine)
foter = input('Inserisci il testo del footer: ')
print('Il footer è ' + foter)
campo = input('Inserisci il nome del campo: ')
test = input('Inserisci la descrizione del campo: ')

webhook = DiscordWebhook(url= ollare)
embed = DiscordEmbed(title= titolo, description= descrizione, color= hex_list)
embed.set_author(name= autore, icon_url='')
embed.set_image(url='')
embed.set_thumbnail(url= immagine)
embed.set_footer(text= foter, icon_url= immagine)
embed.set_timestamp()
embed.add_embed_field(name= campo, value= test, inline='false')
webhook.add_embed(embed)
response = webhook.execute()
print('Embed inviato correttamente')
