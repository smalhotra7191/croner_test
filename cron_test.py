bot_token = '8098425878:AAHtqEidzKKzpi5pzAi8FAZE1B82AOUJsgI'
import requests
chat_id = '1725303057'
message = 'The san ti are coming'

send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
payload = {'chat_id': chat_id, 'text': message}

response = requests.post(send_url, data=payload)
print('Status:', response.status_code)
print('Response:', response.json())