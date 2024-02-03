import requests

from config import API_KEY

def proxys():
	response = requests.get(f"https://proxy6.net/api/{API_KEY}/getproxy")
	data = response.json()
	result = []
	for item in data['list'].values():
		result.append({
			'server' : f'{item["ip"]}:{item["port"]}',
			'username' : item['user'],
			'password' : item['pass']
		})
	return result