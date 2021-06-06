import requests

response = requests.get('https://www.terra.com.br')

print(f'Status code {response.status_code}')
print(f'Headers \n {response.headers}')
print(f'Content \n {response.content}')