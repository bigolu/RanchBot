import facebook
import config
import time
import platform
import requests, json

def ranch_it_up():
    with open('access_token.cfg','r') as f:
        access_token = f.read()

        

    graph = facebook.GraphAPI(access_token=access_token)
    access_token = graph.extend_access_token(app_id=config.app_id, app_secret=config.app_secret)['access_token']

    print access_token

    LongLive = requests.get("https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=1085977088086047&client_secret=9acda75c029a025ca020467a970fc14b&fb_exchange_token=%s" %(access_token))
    LongLive = LongLive.text

    LongLive = LongLive.replace("access_token=", "")
    print "testing: %s" %(LongLive)

    if(LongLive.find("&") != -1):
        index = LongLive.find("&")
        temp = LongLive[index:]
        LongLive = LongLive.replace(temp, "")
    
    print LongLive
    user_id = requests.get("https://graph.facebook.com/v2.2/me?access_token=%s" %(LongLive))
    user_id = user_id.json()

    user_id = user_id['id']
    print user_id

    page_token = requests.get("https://graph.facebook.com/v2.2/%s/accounts?access_token=%s" %(user_id, LongLive))
    page_token = page_token.json()

    page_token = page_token['data'][0]['access_token']
    print page_token

    attachment =  {
    'name': 'Link name',
    'link': 'google.com',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
    'picture': 'http://i.ytimg.com/vi/X6r0VQb1mqg/maxresdefault.jpg'
	}

    graph.put_wall_post(message='Check this out...', attachment=attachment)



ranch_it_up()