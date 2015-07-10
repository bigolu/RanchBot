import facebook
import config
import time
import platform
import requests, json
import random
import nltk

""" Makes wall post to facebook page"""
def wall_post():
    quote = get_ranch_quote() #get a ranch quote
    pic_url = get_pic() #get url of ranch related image
    token = config.perm_token

    attachment =  { #setup body of the wall post
    'name': quote,
    'caption': '',
    'picture': pic_url
	}

    graph = facebook.GraphAPI(access_token=token)
    graph.put_wall_post(message='The Daily Ranch', attachment=attachment) #ranch it up!


""" Searches tumblr for a random picture related to ranch and returns its url"""
def get_pic():
    url = 'http://api.tumblr.com/v2/tagged?tag=ranch%20dressing&api_key=' + config.tumblr_key
    pic = requests.get(url)
    pic = pic.json()

    """ Select a random picture """
    while(True):
        r = random.randint(0, len(pic['response']) - 1) #random number used to select picture
        if(pic['response'][r].has_key('photos')):
            return pic['response'][r]['photos'][0]['original_size']['url'] #return url of image


""" Gets a random quote, replaces all nouns with ranch, and returns it"""
def get_ranch_quote():
    nltk.download('punkt')  #needed for proccessing words
    nltk.download('maxent_treebank_pos_tagger') #also needed for processing words
    quote = requests.get('http://quotesondesign.com/api/3.0/api-3.0.json').json()['quote']
    words = nltk.word_tokenize(quote) #split quote into seperate words

    """ nltk.pos_tag returns a list of lists where the
    0 index is the word and the 1st index the its part of speech
    """
    word_types = nltk.pos_tag (words)

    """ rebuild quote replacing all nouns with ranch"""
    quote = ''
    for word in word_types:
        if word[1] == 'NN': #if the word is noun
            quote += ' ' + 'ranch'
        else:
            if (word[0] in '.,:!\'?') or ('\'' in word[0]): #dont wanna add space before punctuation or before the "n't" in contractions
                quote += word[0]
            else:
                quote += ' ' + word[0]
    quote = quote[1:] #get rid of inital extra space

    return quote


if __name__ == "__main__":
    wall_post()
