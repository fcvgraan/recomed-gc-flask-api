# recomed-gc-flask-api
flask api that runs in google cloud functions for recomed recruitment assignment

* Done: simple logic to get request parameters
* Done: figure out public holidays dynamically with https://pypi.org/project/holidays/
* Done: calculate business time with https://pypi.org/project/businesstimedelta/
* Done: figured out ISO-8601 date comparison and processing with python dateutil. 

* TODO: automated testing
* TODO: automated deployment
* TODO: Authentication (will be nice to have)
* TODO: Persistent storage (will be nice to have


* test url for Friday 18 September 2020 to Friday 25 September 2020 with Thursday 24 September as public holiday, answer must be 45 hours or 162000 seconds 

https://europe-west2-recomed-294109.cloudfunctions.net/calculate-business-seconds?start_time=2020-09-18T08:00:00.000Z&end_time=2020-09-25T17:00:00.000Z