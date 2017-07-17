from __future__ import print_function

import json 
from subprocess import run
#from config.config_loader import ConfigLoader 


print('Loading Function...')



  def lambda_handler(event, context):
  #config = ConfigLoader().config()

    print("value1 = " + event.get('key1'))
    print("value2 = " + event.get('key2'))

return  run("./build_action.sh").stdout


#private event for simulating locating.

if __name__ == "__main__": 

  class Event: 
    def get(self, key): 
            e = { 

            		'key1' : 'value1',
            		'key2' : 'value2',
            	}
return e[key]

   context = 'context'
   event = Event()

  print(lambda_handler(event, context))
