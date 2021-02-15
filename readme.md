# Code for TweeVEBot, cyber news twitter bot:

*This is Python code for [TweeVEBot](https://twitter.com/tweevebot), a twitter bot that tweets info about the latest CVEs.*

### GCP setup guide:

1. Add twitter credentials to GCP Secret Manager in this format:

Name | Twitter credential
------------ | -------------
consumer_key | API key
consumer_secret | API secret key
access_token | generated Access token
access_secret | generated Access token secret

2. Set up a Pub/Sub channel with GCP Cloud Scheduler set to publish the desired trigger time and date.
3. Copy the contents the '*hello-world*' directory into a new GCP Cloud Function.
4. Subscribe the new cloud function to that pub/sub channel.
5. Await trigger from Pub/Sub, or press 'Run now' in GCP Cloud Scheduler to test.

### Branch features:

*gcp_implementation branch:*

- [x] Gather top exploits/vulnerabilities from https://cvedetails.com and sift through data to find most recently updated 8+ CVSS score CVE.

- [x] Each month, report on 1 of 4 categories: SQLi, Remote Execution, DDoS & Privilege Escalation.

- [x] Run in Google Cloud Platform as a Cloud Function, triggered on the first day of each month, at 10:00 GMT by GCP Cloud Scheduler and pub/sub channel.

- [x] Integrates with GCP Secret Manager to securely contain TweeVEBot twitter credentials.

- [ ] Report on top 3 most recently modified CVE's of the week.
 
- [ ] Integrate json data from https://nvd.nist.gov.

*hello_world branch:*

- [x] Part of a [![tutorial video](https://img.youtube.com/vi/VID/0.jpg)](https://www.youtube.com/watch?v=qAKjd-PlZsI) on GCP twitter bots.

- [x] Set to tweet 'Hello World' into the twitter account set up in the tutorial video.

- [x] Integrates with GCP Secret Manager to securely contain twitter credentials.

- [x] Fully annotated code to document that exact logic of the main.py script.

- [x] Designed to work as a GCP Cloud Function only.

- [x] Tested with Python 3.7.

## Developed by Jack:
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk

