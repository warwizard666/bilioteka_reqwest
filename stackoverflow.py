import requests
import datetime
url = "https://api.stackexchange.com/questions"
date1 = int(datetime.datetime.now().timestamp())
date2 = int((datetime.datetime.now() - datetime.timedelta(days=2)).timestamp())
params = {"site": "stackoverflow",
          "tagged": "python",
          "fromdate": date2,
          "todate": date1}
response = requests.get(url, params=params)
data = response.json()["items"]
for qwestions in data:
    print(qwestions["title"])


