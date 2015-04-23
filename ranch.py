#!/usr/bin/python
import facebook
import config
import time
import platform
import requests, json
import random

def ranch_it_up():
    
    quotes = ['"Hit this ranch"','"Sup Mellow Mike?"','"Hey, hey, hey smoke ranch everyday"','"And on the seventh day he ranched"','"And we know that in all things Ranch works for the good of those who love it, who have been called according to its purpose." - Rom 8:28','"May the ranch be with you"','"Check it out! Ranch is what its about"','"And the peace of Ranch, which transcends all understanding, will guard your hearts and your minds" - Phil 4:7','"Everybody wants to ranch the world"',
    '"I dont deserve any ranch for turning the other cheek as my tongue is always in it."','"They say marriages are made in heaven, but so is ranch." - Clint Eastwood']
    randQuote = quotes[random.randint(0, len(quotes))]    

    pic = requests.get("http://api.tumblr.com/v2/tagged?tag=ranch%20dressing&api_key=U74eP3r3GYK3rm94ngtkV2w5csBoHLKriUGpnNh89yApV8VCqB")
    pic = pic.json()


    while(True):
        randResponse = random.randint(0, len(pic['response']))
        if(pic['response'][randResponse].has_key('photos')):
            pic = pic['response'][randResponse]['photos'][0]['original_size']['url']
            break

    with open('access_token.cfg','r') as f:
        access_token = f.read()

    """This was what we did to get the permanent key

        graph = facebook.GraphAPI(access_token=access_token)
    access_token = graph.extend_access_token(app_id=config.app_id, app_secret=config.app_secret)['access_token']

    LongLive = requests.get("https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=1085977088086047&client_secret=9acda75c029a025ca020467a970fc14b&fb_exchange_token=%s" %(access_token))
    LongLive = LongLive.text

    LongLive = LongLive.replace("access_token=", "")

    if(LongLive.find("&") != -1):
        index = LongLive.find("&")
        temp = LongLive[index:]
        LongLive = LongLive.replace(temp, "")
    
    user_id = requests.get("https://graph.facebook.com/v2.2/me?access_token=%s" %(LongLive))
    user_id = user_id.json()

    user_id = user_id['id']

    page_token = requests.get("https://graph.facebook.com/v2.2/%s/accounts?access_token=%s" %(user_id, LongLive))
    page_token = page_token.json()

    print page_token

    page_token = page_token['data'][0]['access_token']
    print page_token """

    attachment =  {
    'name': '%s' %(randQuote),
    'caption': '',
    'picture': pic
	}

    graph = facebook.GraphAPI(access_token=access_token)

    graph.put_wall_post(message='The Daily Ranch', attachment=attachment)


if __name__ == "__main__":
    ranch_it_up()