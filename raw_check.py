import sys
import requests

if len(sys.argv) > 1:
    last_arg = sys.argv[-1]
    print(f"The last argument is: {last_arg}")
else:
    print("No arguments were provided.")

req = requests.get("https://www.twitch.tv/"+last_arg)
if '"isLiveBroadcast":true' in req.text:
    print("LIVE")
else:
    print("NOT LIVE")
