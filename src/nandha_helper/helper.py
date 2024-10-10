import random
import re
import io
import uuid
import string
import json

with open("./data/User-Agent.txt") as file:
    useragents = json.load(file)
    
class nandhaHelper(object):
     """ Nandha-Helper is Super !D """
     
     def __init__(self):
          self.owner = "@Nandha"
          self.support = "@NandhaSupport"
          self.channel = "@NandhaBots"



     def search_text(pattern: str, text: str, ignore_case: bool = False):
           return bool(re.search(pattern, text, re.IGNORECASE)) if ignore_case else bool(re.search(pattern, text))

     def match_text(pattern: str, text: str, ignore_case: bool = False):
           return bool(re.match(pattern, text, re.IGNORECASE)) if ignore_case else bool(re.match(pattern, text))

     def get_as_document(text_string: str, file_name: str = None, ext: str = "txt"):
           filename = f"{file_name if file_name else uuid.uuid4()}.{ext}"
           file = io.BytesIO(str.encode(text_string))
           file.name = filename
           return file

     def get_token(length: int = 10) -> str:
         letters = string.ascii_uppercase + string.ascii_lowercase
         token = "".join(random.choice(letters) for _ in range(length)) 
         return token
          
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
         def _get_useragent(limit: int = 0):
             if limit > 0:
                 assert limit > 0 and limit < len(useragents)
                 return random.sample(useragents, limit)
             else:
                 return random.choice(useragents)
         return _get_useragen
