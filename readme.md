# Code for example GCP Twitter bot:

*This is Python code from my video tutorial on making twitter bot in GCP. View the original video [![here.](https://img.youtube.com/vi/VID/0.jpg)](https://www.youtube.com/watch?v=qAKjd-PlZsI)

### GCP setup guide

1. Copy the contents of either the '*hello-world*' directory into a new GCP cloud function.
2. Set up a pub/sub channel with google cloud scheduler with the desired trigger time and date.
3. Subscribe your new cloud function to that pub/sub channel.
5. Add your twitter credentials to GCP Secrets Manager in this format:

Name | Value
------------ | -------------
consumer_key | your twitter API key
consumer_secret | your twitter API key secret
access_token | generated twitter access token
access_secret | generated twitter access token secret

### Branch features

*hello_world:*

- [x] Set to tweet 'Hello World' into the twitter account set up in the tutorial video

- [x] Integrates with GCP Secret Manager to securely contain twitter credentials

- [x] Fully annotated code to document that exact logic of the main.py script

- [x] Designed to work as a GCP Cloud Function only

- [x] Tested with Python 3.7

*gcp_implementation:*

- [x] Gather top exploits/vulnerabilities from https://cvedetails.com and sift through data to find most recently updated 8+ CVSS score CVE

- [x] Each month, report on 1 of 4 categories: SQLi, Remote Execution, DDoS & Privilege Escalation

- [x] Run in Google Cloud Platform as a Cloud Function, triggered on the first day of each month, at 10:00 GMT by GCP Cloud Scheduler and pub/sub channel

- [x] Integrates with GCP Secret Manager to securely contain TweeVEBot twitter credentials

- [ ] Report on top 3 most recently modified CVE's of the week
 
- [ ] Integrate json data from https://nvd.nist.gov


## Developed by Jack
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk

