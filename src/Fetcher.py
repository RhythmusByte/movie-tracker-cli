import requests
from rich import print

class Fetcher:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
    
    def fetch(self, retries=3):
        try:
            r = requests.get(self.base_url, headers=self.headers)

            if r.status_code == 200:
                return r.json()
            else:
                r.raise_for_status()

        except requests.ConnectTimeout as err:
            print("[red]The request timed out while trying to connect to the remote server.[/red]")
            if retries > 0:
                return self.fetch(retries=retries - 1)
            else:
                raise SystemExit(err)

        except requests.ReadTimeout as err:
            print("[red]The server did not send any data in the allotted amount of time.[/red]")
            raise SystemExit(err)

        except requests.ConnectionError as err:
            print("[red]A Connection error occurred.[/red]")
            raise SystemExit(err)

        except requests.HTTPError as err:
            print("[red]An HTTP error occurred.[/red]")
            raise SystemExit(err)

        except requests.TooManyRedirects as err:
            print("[red]Too many redirects.[/red]")
            raise SystemExit(err)

        except requests.JSONDecodeError as err:
            print("[red]Couldn’t decode the text into json.[/red]")
            raise SystemExit(err)
            
        except requests.RequestException as err:
            print("[red]There was an ambiguous exception that occurred while handling your request.[/red]")
            raise SystemExit(err)