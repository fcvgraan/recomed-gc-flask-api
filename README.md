# recomed-gc-flask-api
flask api that runs in google cloud functions for recomed recruitment assignment

Name: Francois Van Graan
Endpoint: https://europe-west2-recomed-294109.cloudfunctions.net/calculate-business-seconds?start_time=2020-09-18T08:00:00.000Z&end_time=2020-09-25T17:00:00.000Z

* The provided endpoint constains query string parameters for Friday 18 September 2020 to Friday 25 September 2020. This is period that contains 5 work days, a weekend and one public holiday, Thursday 24 September. The response is supposed to be 45 hours or 162000 seconds. There are many different other test cases in the test folder

* The code is hosted in my personal google cloud instance but you can set up your own instance by following the deployment instructions and using the deploy.sh script.

* The test folder contains an exported Postman collection with several test cases. They are configured to point to the endpoint provided above but you can obviously update them with your own. I've provided instructions on how to run the tests in test instructions.txt



