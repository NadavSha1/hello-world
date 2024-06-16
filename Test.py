import requestsB
password = "AIzaSyCzmABOfcTbibaP_VmZPsFn0q3Ro2sXlHW"

response = requests.get('http://google.com', {'password': password})

print(response.json())
dd
