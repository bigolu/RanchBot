import facebook
import config
import time
import platform
import requests, json
import random

def wall_post():

    quotes = ['"Hit this ranch"','"Sup Mellow Mike?"','"Hey, hey, hey smoke ranch everyday"','"And on the seventh day he ranched"','"And we know that in all things Ranch works for the good of those who love it, who have been called according to its purpose." - Rom 8:28','"May the ranch be with you"','"Check it out! Ranch is what its about"','"And the peace of Ranch, which transcends all understanding, will guard your hearts and your minds" - Phil 4:7','"Everybody wants to ranch the world"',
    '"I dont deserve any ranch for turning the other cheek as my tongue is always in it."','"They say marriages are made in heaven, but so is ranch." - Clint Eastwood']
    randQuote = quotes[random.randint(0, len(quotes) - 1)]

    pic = requests.get("http://api.tumblr.com/v2/tagged?tag=ranch%20dressing&api_key=U74eP3r3GYK3rm94ngtkV2w5csBoHLKriUGpnNh89yApV8VCqB")
    pic = pic.json()


    while(True):
        randResponse = random.randint(0, len(pic['response']) - 1)
        if(pic['response'][randResponse].has_key('photos')):
            pic = pic['response'][randResponse]['photos'][0]['original_size']['url']
            break

    access_token = config.access_token

    attachment =  {
    'name': '%s' %(randQuote),
    'caption': '',
    'picture': pic
	}

    graph = facebook.GraphAPI(access_token=access_token)

    graph.put_wall_post(message='The Daily Ranch', attachment=attachment)


if __name__ == "__main__":
    wall_post()
