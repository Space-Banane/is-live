import requests

def main(args):
    ROUTE = args.get("route")
    print(ROUTE)
    if ROUTE != "check":
        return {
            "_shsf": "v2",
            "_code": 200,
            "_res": """<html>
        <head>
        <title>Welcome to IsLive - Twitch Streamer Edition</title>
        <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-100 text-gray-800 font-sans">
        <div class="max-w-4xl mx-auto p-6">
        <h1 class="text-4xl font-bold text-center text-blue-600 mb-4">
        Welcome to IsLive - Twitch Streamer Edition
        </h1>
        <p class="text-lg text-center mb-6">
        Check if a streamer is live:
        </p>
        <div class="bg-white shadow-md rounded-lg p-4">
        <label for="streamer" class="text-lg font-medium mb-2">Streamer Name:</label>
        <input type="text" id="streamer" class="border border-gray-300 rounded-lg p-2 w-full mb-4" placeholder="Enter streamer name" required>
        <button id="checkStatus" class="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
        Check Live Status
        </button>
        </div>
        <div class="bg-gray-200 shadow-md rounded-lg p-4 mt-6">
        <h2 class="text-2xl font-bold text-center text-gray-700 mb-4">Result</h2>
        <textarea id="result" class="border border-gray-300 rounded-lg p-2 w-full h-24" readonly></textarea>
        </div>
        <div class="bg-blue-100 shadow-md rounded-lg p-4 mt-6">
        <h2 class="text-2xl font-bold text-center text-blue-700 mb-4">How to Use via HTTP</h2>
        <p class="text-lg">
        To check if a streamer is live via HTTP, send a GET request to the following endpoint:
        </p>
        <pre class="bg-gray-200 p-2 rounded-lg overflow-x-auto">
        https://shsf-api.cottonfieldworkers.shop/api/exec/6/22b5d292-ccf1-473b-8838-4db550d6a1e6/check?streamer=STREAMER_NAME
        </pre>
        <p class="text-lg mt-2">
        Replace <code>STREAMER_NAME</code> with the name of the Twitch streamer you want to check.
        </p>
        <p class="text-lg mt-2">
        Example:
        </p>
        <pre class="bg-gray-200 p-2 rounded-lg overflow-x-auto">
        https://shsf-api.cottonfieldworkers.shop/api/exec/6/22b5d292-ccf1-473b-8838-4db550d6a1e6/check?streamer=shsf
        </pre>
        <p class="text-lg mt-2">
        The response will be a JSON object indicating whether the streamer is live or not.
        </p>
        <p class="text-lg mt-2">
        Example Response:
        </p>
        <pre class="bg-gray-200 p-2 rounded-lg overflow-x-auto">
        {
            "state": true
        }
        </pre>
        </div>
        </div>
        <script>
        document.getElementById('checkStatus').addEventListener('click', async () => {
            const streamer = document.getElementById('streamer').value;
            const resultBox = document.getElementById('result');
            if (!streamer) {
            resultBox.value = "Please enter a streamer name.";
            return;
            }
            try {
            const response = await fetch(`https://shsf-api.cottonfieldworkers.shop/api/exec/6/22b5d292-ccf1-473b-8838-4db550d6a1e6/check?streamer=${encodeURIComponent(streamer)}`);
            if (!response.ok) {
                resultBox.value = "Error : " + response.statusText;
                return;
            }
            const data = await response.json();
            if ("state" in data) {
                resultBox.value = data.state ? "The streamer is live!" : "The streamer is not live.";
            } else {
                resultBox.value = "Error: Unable to fetch live status.";
            }
            } catch (error) {
            resultBox.value = "Error: " + error.message;
            }
        });
        </script>
        <footer class="mt-6 text-center">
        <p class="text-sm text-gray-600">
        Is-Live; Made with Love by <a href="https://space.reversed.dev?ref=islive_fotter" class="text-blue-500 hover:underline">Space</a>
        </p>
        </body>
        </html>
        """,
            "_headers": {
            "Content-Type": "text/html",
            }}
    streamer = ""
    if args.get("body"):
        body = args.get("body")
        if body.get("streamer"):
            streamer = body.get("streamer")
            print("has body")
    if args.get("queries"):
        queries = args.get("queries")
        streamer = queries.get("streamer")
        print("queries")
    
    if not streamer or streamer == "":
        return {"_shsf": "v2", "_code": 400, "_res": {"message": "No 'streamer' set"}}


    req = requests.get("https://www.twitch.tv/"+streamer)
    if '"isLiveBroadcast":true' in req.text:
        return {"_shsf": "v2", "_code": 200, "_res": {"state": True}}
    else:
        return {"_shsf": "v2", "_code": 200, "_res": {"state": False}}
