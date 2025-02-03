import click # type: ignore
import requests
import json

def get_data(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    pushEvent = []
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        for event in data:
            if event["type"] == 'PushEvent':
                pushEvent.append(event)
        return pushEvent
    else:
        return None
    
def last_message(username):
    try:
        data = get_data(username)
        for event in data:
            if event["type"] == "PushEvent":
                return print("Committed", event["payload"]["commits"][0]["message"], "to", event["repo"]["name"].split('/')[1])
    except:
        return print("Failed fetching data.")

@click.group()
def main():
    pass

@main.command()
@click.argument('username', nargs=1)
def latest_commit(username):
    last_message(username)

if __name__ == "__main__":
    main()