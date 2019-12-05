## Implementation of a simple github events fetcher


In this repository you can find a file named ```github.py``` that implements the ```get_events(user, repo)``` function. This function is used in the ```main.py``` file to fetch a list of events coming from a github repository using the github API. If you run the program, executing the main file with: ```python main.py``` it will  give you the list of events for the 'swdevel-lab-hfarm' user and the 'example' repository. 

```
$ python3 main.py 
Repository "example" from user "swdevel-lab-hfarm" has 18 events.
```


## Credits:

Github API are free to use without an API key up to [5000 requests per hour](https://developer.github.com/v3/#rate-limiting).
