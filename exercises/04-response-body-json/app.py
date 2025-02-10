import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

time_dict=response.json()

print(f'Current time: {time_dict["hours"]} hrs {time_dict["minutes"]} min and {time_dict["seconds"]} sec')