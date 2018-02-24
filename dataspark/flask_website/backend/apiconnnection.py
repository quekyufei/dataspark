import requests
import base64


class APIConnection:
    # ConsumerKey
    consumerKey = "4xGO7wDdCta9g5nlX_NXUfbdWE8a"
    consumerSecret = "jYtKEdtV9JlXw4lCimvwkrbtt1ca"

    # Set up connection
    keySecret = (consumerKey + ":" + consumerSecret).encode('utf-8')
    consumerKeySecretB64 = base64.b64encode(keySecret).decode('utf-8')
    tokenResponse = requests.post("https://apistore.datasparkanalytics.com/token",
                                  data={'grant_type': 'client_credentials'},
                                  headers={'Authorization': 'Basic ' + consumerKeySecretB64})

    # Access token and set content type
    token = tokenResponse.json()['access_token']
    contentType = "application/json"

