# AudioToText
**This application was built with flask for python framework. It basically transcribes an audio file to its Text equivalent using [IBM watson speech](https://www.ibm.com/watson/services/speech-to-text) to text service.** 

### Tools Used
- Bootstrap twitter framework was used for front end.
- The backend is done with Python using the [Flask Framework](http://flask.pocoo.org)

##  Prerequisites
- Make sure you have an account on [IBM cloud portal](https://console.bluemix.net/registration/)
- Make sure to have git set up on your local machine as described [here](https://www.atlassian.com/git/tutorials/setting-up-a-repository).
- Once logged In, Click on **Create** link on the mainpage to create a speech-to-text resource. After which you can click on the **show credential** link to reveal the credentials necessary to use with this service.
- Make sure to copy **api_key** and **url** values into your config file or anywhere in your code.

## How I configured
- Copy the Values for **api_key** and **url** into `/instance/config` file of the flask project as shown below.
```
WATSON_API_KEY = 'your_api_key_value'
WATSON_API_URL = 'your_url_value'
```
- For this project do well to include the following code in the `/instance/config` file. 
```
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
```
- This line of code will serve as the url to be used to temporarily hold the uploaded audio file

### Running the app Locally
- clone the github repo for this project by running the following commands in a terminal.
```
git clone https://github.com/nappy29/AudioToText.git
```

``` cd AudioToText```

- It will be safer to run the app in development mode locally. So the following commands will be ok to have it running.

```
export FLASK_APP=audiotranscriptionapp
export  FLASK_ENV=development

```

These commands are best suited for mac and Unix distro systems. If you running on a windows environment do well to 

substitute `export` with `set` in the above commands

**Enjoy :)**