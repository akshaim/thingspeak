import urllib
response = urllib.urlopen('http://api.thingspeak.com/channels/your_channel_no/field/1/last.txt')
data = response.read()
print data
