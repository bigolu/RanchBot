import facebook
import requests
import sys
import config

"""
This function a permenant access_token for a facebook page of which the user is an admin by obtaining a series
of tokens with longer and longer expiration dates. It then writes the token to a file (perm_token.cfg)

param: access_token for the user
param: name of page
"""
def get_token(token, page_name):
    """ Extends the expiration date of the token """
    graph = facebook.GraphAPI(access_token=token)
    extended_token = graph.extend_access_token(app_id=config.app_id, app_secret=config.app_secret)['access_token']

    """ Extends the expiration date of the token even more"""
    url = 'https://graph.facebook.com/v2.2/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' %(config.app_id, config.app_secret, extended_token)
    longlive_token = requests.get(url)
    #remove extra text from around the access token
    longlive_token = longlive_token.text
    longlive_token = longlive_token.replace("access_token=", "")
    if(longlive_token.find("&") != -1): #sometimes token comes in the form 'access_token&extrastuff'
        index = longlive_token.find("&")
        longlive_token = longlive_token[:index]

    """ Get user id for the admin"""
    url = "https://graph.facebook.com/v2.2/me?access_token=%s" %(longlive_token)
    user = requests.get(url)
    user = user.json()
    user_id = user['id']

    """ Get all the pages the user is an admin of"""
    all_pages = requests.get("https://graph.facebook.com/v2.2/%s/accounts?access_token=%s" %(user_id, longlive_token))
    all_pages = all_pages.json()['data']

    """ Find the page specified by the user"""
    for page in all_pages:
        if page['name'] == page_name:
            with open("perm_token.cfg","a+") as f:
                f.write(page['access_token']) # writes permenant access_token to file
            return

    raise Exception('Could not find page with the name: ' + page_name)

if __name__ == "__main__":
    if len(sys.argv) != 3: #did not give specified number of arguments
        raise Exception('Invalid number of arguments')

    get_token(sys.argv[1], sys.argv[2])
