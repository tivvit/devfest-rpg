__author__ = 'tivvit'

import pycurl, json

url = 'https://practical-well-728.appspot.com/_ah/api/devfest_cdh_api/v1/user'

with file("data.csv", "r") as f:
    for line in f:
        data = line.split(",")
        print data[0], data[3]

        data = json.dumps({"name": data[3].strip(), "email": data[0]})

        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type:application/json"', 'Accept: application/json'])
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, data)
        c.perform()