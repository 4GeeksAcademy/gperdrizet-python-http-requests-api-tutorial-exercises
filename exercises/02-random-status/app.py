import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")

response_codes={
    '404': 'The URL you asked for is not found',
    '503': 'Unavailable right now',
    '200': 'Everything went perfect',
    '400': 'Something is wrong with the request params'
}

if response.status_code is response_codes.keys():
    print(response_codes[response.status_code])

else:
    print('Unknown status code')