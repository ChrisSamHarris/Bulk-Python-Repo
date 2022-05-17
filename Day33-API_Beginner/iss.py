#API - Set of commands, functions, protocls and objects - Used to create software or interact with an external system
#Interface between your programme and an external system | Request > Response Relationship 

import requests
import datetime as dt

ISS_response_code = requests.get(url="http://api.open-notify.org/iss-now.json") #.status_code just provides the status code as an int

print(ISS_response_code.status_code)
print(type(ISS_response_code.status_code)) 

ISS_response_code.raise_for_status() #Requests module can raise Exceptions instead of manual input 

long_data = ISS_response_code.json()['iss_position']['longitude']
lat_data = ISS_response_code.json()['iss_position']['latitude']
print(f"{long_data}, {lat_data}")




