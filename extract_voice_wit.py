from wit import Wit
client = Wit('RNQ4DOVZ2XHKRUJMHAAQVSRTHYBSHDLL')

resp = None
with open(r'C:\Users\tanma\Downloads\RE381247e51131df3996c702b2cb18d36f_1.wav', 'rb') as f:
  resp = client.speech(f, {'Content-Type': 'audio/wav'})
print(str(resp))

resp_1= None
with open(r'C:\Users\tanma\Downloads\RE518b4a5cdcc070e536000925d0301647_2.wav', 'rb') as f:
  resp_1 = client.speech(f, {'Content-Type': 'audio/wav'})
print(str(resp_1))

resp_2= None
with open(r'C:\Users\tanma\Downloads\RE13f557aa47d6885449d87cf60352b6b8_3.wav', 'rb') as f:
  resp_2 = client.speech(f, {'Content-Type': 'audio/wav'})
print(str(resp_2))

resp_3= None
with open(r'C:\Users\tanma\Downloads\RE97288d8afadf2077ed55dba8e777bf78_4.wav', 'rb') as f:
  resp_3 = client.speech(f, {'Content-Type': 'audio/wav'})
print(str(resp_3))