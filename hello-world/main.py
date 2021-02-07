import os
import tweepy

from google.cloud import secretmanager

project_id = os.environ["GCP_PROJECT"]
client = secretmanager.SecretManagerServiceClient()


def get_secrets(secret_request):
    name = f"projects/{project_id}/secrets/{secret_request}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")


def pusbsub_trigger(event, context):
    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))
    status = ("Hello World")

    consumer_key = get_secrets("twitter_consumer_key")
    consumer_secret = get_secrets("twitter_consumer_secret")
    access_token = get_secrets("twitter_access_token")
    access_secret = get_secrets("twitter_access_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    api.update_status(status)
    print("Tweet length: " + str(len(status)))
