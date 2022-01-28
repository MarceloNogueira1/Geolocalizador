import requests 

def start_api(cep):
    global adress_data
    r = requests.get(f'https://ipgeolocation.abstractapi.com/v1/?api_key=a5832ca9a0264f00b77ab38ef833085a&ip_address={cep}')
    adress_data = r.json()

def resultados():
    print('IP:',adress_data["ip_address"])
    print('CIDADE:', adress_data["city"])
    print('ESTADO:', adress_data["region"])
    print('CEP:', adress_data["postal_code"])
    print('PAÍS/CODE:', adress_data["country"])
    print('CÓDIGO DO PAÍS:', adress_data["country_code"])
    print('MOEDA:', adress_data["currency"]['currency_code'])
    print('CONTINENTE:', adress_data["continent"])
    print('LONGITUDE:', adress_data["longitude"])
    print('LATITUDE:', adress_data["latitude"])
    print('VPN:', adress_data["security"])
    print('HORA:', adress_data["timezone"]["current_time"])
    print('PROVEDOR:', adress_data["connection"]["autonomous_system_organization"])
    print('TIPO DE CONEXÃO:', adress_data["connection"]["connection_type"])

ip = input('DIGITE O IP A SER CONSULTADO: ')

start_api(cep=ip)
resultados()
