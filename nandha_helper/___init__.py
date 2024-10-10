import random
import json


with open("./nandha_helper/data/User-Agent.txt") as file:
     useragents = json.load(file)

class nandhaHelper(object):
     """ Nandha-Helper is Super !D """
     
     def __init__(self):
          self.owner = "@Nandha"
          self.support = "@NandhaSupport"
          self.channel = "@NandhaBots"


     
     @property
     def get_useragent(self) -> [str , list]:
         """
         Info:
             For get random user-agent 
         Argument: 
              limit - int
         Response: 
              list or str according to the limit argument
         """
         def _get_useragent(limit: int =0):
             if limit > 0:
                 assert limit > 0 and limit < len(useragents)
                 return random.sample(useragents, limit)
             else:
                 return random.choice(useragents)
         return _get_useragent

     
          
