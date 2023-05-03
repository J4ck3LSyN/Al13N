# Python GHDB Tool
import googlesearch
import os,time,sys,json

class search:
    def __init__(self):
        self.searchConfig = {
            'inputPath':None,
            'inputString':None,

            'resultMax':15,

            'randomUserAgent':True,
            'userAgent':None,

            'topLevelDomain':'com',
            'language':'en',
            'timeLimits':'0',
            'safeSearch':'off',
            'resultsPerPage':10,
            'firstResult':0,
            'lastResult':None,

            'pauseBetweenRequests':2.0,
            'country':'',
            'extraPerams':{},
            'verifySSL':True
        }


    def setQueryStr(self,str):
        self.searchConfig['inputString']=str(str)

    def setRandomUserAgent(self):
        if self.searchConfig['randomUserAgent'] == True:
            self.searchConfig['userAgent'] = str(googlesearch.get_random_user_agent().decode('utf-8'))
        else:
            ...

    def iterateGenerator(self,generator):
        returnList = []
        while i <= self.searchConfig['resultMax']:
            for url in generator:
                returnList.append(url)
        return returnList

    def run(self):
        if self.searchConfig['inputString'] != None:
            generator = googlesearch.search(str(self.searchConfig['inputString']),tld=self.searchConfig['topLevelDomain'],lang=self.searchConfig['language'],tbs=self.searchConfig['timeLimits'],safe=self.searchConfig['safeSearch']start=self.searchConfig['firstResult'],stop=self.searchConfig['lastResult'],pause=self.searchConfig['pauseBetweenRequests'],extra_params=self.searchConfig['extraPerams'],country=self.searchConfig['country'],verify_ssl=self.searchConfig['verifySSL'])
            return generator
        else:
            ...

if __name__ == '__main__':

    if len(sys.argv[1:]) == 0:
        ...
    else:
        ...
