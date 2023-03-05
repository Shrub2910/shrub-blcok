'''
Very basic example of how to use shrubapi

Just initialises the client and prints the owner's uuid
'''

from shrubapi import HypixelApiClient # importing the client from the library

client = HypixelApiClient('--API-KEY--') # initialising client

print(client.key.owner) # printing the uuid of the api key's owner