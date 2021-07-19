#!/usr/bin/python

#print(ord('°'))
#print(chr(176))
import random
custom_excuse={}
data_excuses = {
	"Intros": [
		"Sorry I can't come",
		"Please forgive my absence",
		"This is going to sound crazy but",
		"Get this:",
		"I can't go because",
		"I know you're going to hate me but",
		"I was minding my own business and boom!",
		"I feel terrible but",
		"I regretfully cannot attend,",
		"This is going to sound like an excuse but"
	],
	"Scapegoat": [
		"my nephew",
		"the ghost of Hitler",
		"the Pope",
		"my ex",
		"high school marching band",
		"Dan Rather",
		"a sad clown",
		"the kid from Air Bud",
		"a professional cricket team",
		"my Tinder date"
	],
	"Delay": [
		"just shit the bed",
		"died in front of me",
		"won't stop telling me knock knock jokes",
		"is having a nervous breakdown",
		"gave me syphilis",
		"poured lemonade in my gas tank",
		"stabbed me",
		"found my box of human teeth",
		"stole my bicycle",
		"posted my nudes on Instagram"
	]
}
name_custom = "Falko"
#for i in range(len(data_excuses["Intros"])):
#  print(data_excuses["Intros"][i])

custom_excuse['excuse'] = f'Dear {name_custom}, {data_excuses["Intros"][random.randint(0, len(data_excuses["Intros"])-1)]} {data_excuses["Scapegoat"][random.randint(0, len(data_excuses["Scapegoat"])-1)]} {data_excuses["Delay"][random.randint(0, len(data_excuses["Delay"])-1)]}'
print(custom_excuse)