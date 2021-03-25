# using python request api (application programming interface)
import requests

def status_code_check(website):
    response = requests.get(website) # check in own time

    if response:
        print("The website, {}, is up and running. Status code: {}".format(website, response.status_code)) # 200 means success - website is live and running
        return response
    else:
        print("Oops, {} isn't running! Status code: {}".format(website, response.status_code))
        return False

# connect to www.bbc.co.uk and scrape the live data to display it
#response = requests.get("https://www.bbc.co.uk/")

# "https:/www1.flightrising.com"

web_start = "https://"

websites = ["www.bbc.co.uk", "www.youtube.com", "www1.flightrising.com", "www.marvel.com/404"]

response = status_code_check(web_start + websites[3])

if response:
    print(response.headers['Date'])
else:
    print("The website wasn't running...")