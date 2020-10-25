import os
import discord
import random

#Bot Version: v1.1.2
#Contributors: Emafire003, Emafir3

TOKEN=""

#dice imgs / immagini dadi
d4s = ["img/d4-1.png", "img/d4-2.png", "img/d4-3.png", "img/d4-4.png"]

d6s = ["img/d6-1.png", "img/d6-2.png", "img/d6-3.png", "img/d6-4.png", "img/d6-5.png", "img/d6-6.png"]

d8s = ["img/d8-1.png", "img/d8-2.png", "img/d8-3.png", "img/d8-4.png", "img/d8-5.png", "img/d8-6.png", "img/d8-7.png", "img/d8-8.png"]

d10s = ["img/d10-1.png", "img/d10-2.png", "img/d10-3.png", "img/d10-4.png", "img/d10-5.png", "img/d10-6.png", "img/d10-7.png",
        "img/d10-8.png", "img/d10-9.png", "img/d10-0.png"]

d12s = ["img/d12-1.png", "img/d12-2.png", "img/d12-3.png", "img/d12-4.png", "img/d12-5.png", "img/d12-6.png", "img/d12-7.png",
        "img/d12-8.png", "img/d12-9.png", "img/d12-10.png", "img/d12-11.png", "img/d12-12.png"]

d20s = ["img/d20-1.png", "img/d20-2.png", "img/d20-3.png", "img/d20-4.png", "img/d20-5.png", "img/d20-6.png", "img/d20-7.png",
        "img/d20-8.png", "img/d20-9.png", "img/d20-10.png", "img/d20-11.png", "img/d20-12.png", "img/d20-13.png", "img/d20-14.png",
        "img/d20-15.png", "img/d20-16.png", "img/d20-17.png", "img/d20-18.png", "img/d20-19.png", "img/d20-20.png"]

d100s = ["img/d100-00.png", "img/d100-10.png", "img/d100-20.png", "img/d100-30.png", "img/d100-40.png", "img/d100-50.png",
        "img/d100-60.png", "img/d100-70.png", "img/d100-80.png", "img/d100-90.png", ]

#those are the actual dice rollers / i generatori di dadi effettvi
def gen_d20():
    #random.randint genera un numero da 0 a 19, gli array iniziano da 0
    number = random.randint(0, 19)
    #this picks the image path from the arrays up there and returns it
    #Questo prende e ritorna il percorso dell'immagine dagli array là sopra
    return d20s[number]
def gen_d6():
    number = random.randint(0, 5)
    return d6s[number]
def gen_d8():
    number = random.randint(0, 7)
    return d8s[number]
def gen_d10():
    number = random.randint(0, 9)
    return d10s[number]
def gen_d4():
    number = random.randint(0, 3)
    return d4s[number]
def gen_d100():
    number = random.randint(0, 9)
    return d100s[number]
def gen_d12():
    number = random.randint(0, 11)
    return d12s[number]

#those are the dice's spirit reactions/queste sono le reazioni dello spirito dei dadi
def critic_fail():
    1_phrases = ["BWAHAHAHAAHAHAHAHAHAHAHAHAHAHAHAHAHAH", "finalmente", "* happy evil dice noises *", "* sad player noises *", "un goblin potrebbe farti uno sgambetto e ti romperesti una gamba, se non peggio", "OH SI’ SI’ ;}", "GODOOOOOOOOOOOOOO!1!1!", "Press F to pay respect"]
    reaction = random.randint(0, len(1_phrases)-1)
    return await message.channel.send(reaction)
def fails():
    fails_phrases = ["Che schifo", "Sorry ;>", "mi dispiace", "forse la prossima", "forse la prossima... ANDRA' PEGGIO AHAHAHAH", "ahah", "mi sa di NO!", "probabile fallimento", "fai qualcosa di importante, mi raccomando :}", "GODO!", "oh Sì :]", "F"]
    reaction = random.randint(0, len(fails_phrases)-1)
    return await message.channel.send(reaction)
def limit_numbers():
    limits_phrases = ["buona fortuna", "auguri", "scelta del DM", "confine", "stai passando tra due territori nemici in lotta: uno amico dei PG e uno loro nemico (inutile dire che lo spirito che muove i dadi è tuo acerrimo nemico BWAHAHA)", "DM tira una monetina"]
    reaction = random.randint(0, len(limits_phrases)-1)
    return await message.channel.send(reaction)
def success_numbers():
    success_phrases = ["not bad", "okay", "okkidoki", "sei passato… rimedieremo alla prossima BWAHAHA", "complimenti", "successo", "uffa -_-", "non ti emozionare perché è una ruota, o meglio un dado che gira"]
    reaction = random.randint(0, len(success_phrases)-1)
    return await message.channel.send(reaction)
def max_number():
    max_phrases = ["come?!?", "NANI", "DA FUCK", "WTF", "WHAT THE FUCK","COSA?", "stai cheattando", "non ho parole", "complimenti", "fantastico", "gli dei ti hanno aiutato", "gli dei ti hanno conferito il potere di modellare le terre, aprire  le acque, spostare montagne o distruggiore un esercito", "gli dei ti hanno conferito il potere di modellare le terre, aprire  le acque, spostare montagne o distruggiore un esercito, ma tu...","potresti provare a volare e non morire, é un consiglio dal mio cuore di ossidiana :}", "non gasarti-_-"]
    reaction = random.randint(0, len(max_phrases)-1)
    return await message.channel.send(reaction)
	
simplemode = False

def run():
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

    @client.event
    async def on_member_join(member):
            await member.create_dm()
            await member.dm_channel.send(
            f'Hi {member.name}, welcome to my Discord server!'
            )

    @client.event
    async def on_message(message):
        global simplemode
        #check to prevent the bot triggering itself
        if message.author == client.user:
            return
        #check for the debug command
        if message.content.startswith("!dndebug"):
            await message.channel.send("client.user ="+str(client.user)+"Message.author ="+str(message.author)+"\n\n"+str(simplemode))

        #Checks if the command !dsimple gets executed and chages the mode accordingly
        if message.content.startswith('!dsimple'):
            if(simplemode):
                simplemode = False
            else:
                simplemode = True
            await message.channel.send("Modalità semplice:"+str(simplemode))

        #Checks the mode. If true, then it doesn't use imgs / Controlla la mode. Se vera, non userà le immagini
        if(not simplemode):
            #checks for the dice rolls and calls the relative function / controlla per i roll dei dadi tramite i comandi !d<> e chiama la relativa funzione
            if message.content.startswith('!d20'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d20()))
                    num = random.randint(1,20)
                if(num == 1):
                        critic_fail() 
                        if(num > 1 && num < 11):
                                fails_numbers()
                                if(num >=11 && num < 15):
                                        limits_numbers()
                                        if(num >=15 and num <20):
                                                success_numbers()
                                                if(num == 20):
                                                        max_number()
            elif message.content.startswith('!d4'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d4()))
            elif message.content.startswith('!d6'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d6()))
            elif message.content.startswith('!d8'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d8()))
            elif message.content.startswith('!d10'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d10()))
            elif message.content.startswith('!d12'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d12()))
            elif message.content.startswith('!d%'):
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", file=discord.File(gen_d100()))
        else:
            if message.content.startswith('!d20'):
                #random.randint genera un numero casuale tra quelli.
                #Anzichè metterlo direttamente nell'argomento, crea prima una varibile uguale a quello.
                #Tipo num = random.randint(1,20) e usa quel numero per determinare cosa è uscito dal dado
                e = discord.Embed(title=str(random.randint(1,20)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d4'):
                e = discord.Embed(title=str(random.randint(1,4)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d6'):
                e = discord.Embed(title=str(random.randint(1,6)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d8'):
                e = discord.Embed(title=str(random.randint(1,8)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d10'):
                e = discord.Embed(title=str(random.randint(1,10)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d12'):
                e = discord.Embed(title=str(random.randint(1,4)))
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)
            elif message.content.startswith('!d100') or message.content.startswith('!d%'):
                e = discord.Embed(title=str(random.randint(1,10))+"0")
                await message.channel.send(str(message.author)+" il dado ha per te deciso:", embed=e)

    client.run(TOKEN)
run()
