"""This code is written by AKmahim"""

import re
import requests
import sys
from twilio.rest import Client


def find_case(url):
    #this take a the url and collect the data about world coronavirus case return 3 data-world_case,death_case,recovered_case
    resp = requests.get(url)
    if resp.ok is False:
        sys.exit("Could not connect with website")
    else:
        content = resp.text
        WC = re.findall(total_pat,content)
        DC = re.findall(death_pat,content)
        RC = re.findall(recover_pat,content)
        
        return WC[0],DC[0],RC[0]







if __name__ == "__main__":
    total_pat = re.compile(r'<div class="maincounter-number">\s+<span style="color:#aaa">(.*?) </span>\s+</div>')
    death_pat = re.compile(r'<div class="maincounter-number">\s+<span>(.*?)</span>\s+</div>')
    recover_pat =re.compile(r'<div class="maincounter-number" style="color:#8ACA2B ">\s+<span>(.*?)</span>\s+</div>')
    world_url = "https://www.worldometers.info/coronavirus/#countries"
    bd_url = "https://www.worldometers.info/coronavirus/country/bangladesh/"
    tc1,dc1,rc1 = find_case(world_url)
    tc2,dc2,rc2 = find_case(bd_url)

    res1 = "World Case---\nCoronavirus Cases: {}\nDeaths: {}\nRecovered: {}\n".format(tc1,dc1,rc1)
    res2 = "Bangladesh Case--\nCoronavirus Cases: {}\nDeaths: {}\nRecovered: {}\n".format(tc2,dc2,rc2)
    #print(res1) #world case
    #print(res2) #bangladesh case
    whatapp_mess = res1 + res2
    ac_sid = "ACfb554f4b5d8f847c156f03a78da2751c"
    auth_token ="852d3df24fa063ee6c3f15b93211c912"
    client = Client(ac_sid,auth_token)
    message = client.messages.create(body=whatapp_mess,from_='whatsapp:+14155238886',to='whatsapp:+8801635227460')
    print("Data send")
