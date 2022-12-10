
import numpy as np 
from sentinelsat import SentinelAPI
import traceback

user = 'hugsy'
password = '9cCxYTDh'
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')


with open('uuid.txt') as f:
    lines = f.readlines()

compteur  = 0

for i in range(1,len(lines)):
    try :
        print(lines[i][0:-1])
        request = lines[i][0:-1]
        api.download(str(request))
    except :
        traceback.print_exc()
        compteur = compteur +  1
        print('compteur = ',compteur)
        continue
print('Finish')

