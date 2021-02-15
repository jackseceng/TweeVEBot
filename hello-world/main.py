#Comments will detail the different elements of this code for those that were curious about it from the video.

#Import the libraries that we need to run this bot, these are also defined in the 'requirements.txt' file
import os #Library for getting operating system environment information
import tweepy #Twitters library for interacting with the twitter API

from google.cloud import secretmanager #Library for interacting with the GCP Secret Manager API

#Define global variables for script
project_id = os.environ["GCP_PROJECT"] #Get current GCP project name
client = secretmanager.SecretManagerServiceClient() #Establish client service for connecting to GCP Secret Manager

#Define get_secrets function
def get_secrets(secret_request): #Function takes in a secret name as the secret_request argument
    name = f"projects/{project_id}/secrets/{secret_request}/versions/latest"
    """
    Uses project_id variable established in line 9, and the secret_request argument input on line 14
    to create a query string for the name of the secret to extract from GCP Secret Manager.
    """
    response = client.access_secret_version(name=name) #Get response from client service using the name variable as input
    return response.payload.data.decode("UTF-8") #Return the secret value from clients response in utf-8 encoded format

#Define the pubsub_trigger function
def pusbsub_trigger(event, context): #Input 2 variables from GCP PubSub signal event and context
    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))
    """
    Printing anything in GCP Cloud Functions will create a log in the Logs Explorer dashboard for reference later.
    In this example, the code will create a log detailing the message that triggered it with an accompanying timestamp.
    """
    status = ("Hello World") #Set the status variable with the string value to be used in the tweet

    consumer_key = get_secrets("twitter_consumer_key")
    consumer_secret = get_secrets("twitter_consumer_secret")
    access_token = get_secrets("twitter_access_token")
    access_secret = get_secrets("twitter_access_secret")
    """
    This section repeatedly calls the get_secrets function defined on line 14 to get the 4 different secret values
    for the twitter API that were defined earlier in the tutorial. Each one has a unique variable name that can be
    passed to the twitter API in order to authenticate.
    """

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Set the OAuth for twitter API using consumer credentials
    auth.set_access_token(access_token, access_secret) #Set the twitter API access token using access credentials

    api = tweepy.API(auth) #Check that OAuth to twitter is valid, will stop execution and error if not
    api.update_status(status) #Post a tweet using the status string defined on line 30 as the contents
    print("Tweet length: " + str(len(status)))
    """
    Print out the tweet that was sent to twitter and the length of the tweet in characters for reference.
    This will appear in the Logs Explorer dashboard in GCP, allowing for verification that the Cloud Function
    sent the string that was intended to be tweeted and how long it was (in case the string went over the 280 character
    limit that twitter has).
    """
