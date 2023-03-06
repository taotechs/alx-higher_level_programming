#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    email_payload = argv[2]
    response = requests.post(url, data={'email': email_payload})

    print(response.text)
