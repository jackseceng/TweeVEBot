# TweeVEBot:

*A twitter bot for tweeting interesting data on CVEs from multiple sources. Running in GCP as a cloud function.*

### GCP setup guide

1. Copy the contents of either the *'monthly'* or '*weekly*' directories into a new GCP cloud function.
2. Set up a pub/sub channel with google cloud scheduler with the desired trigger time and date.
3. Subscribe your new cloud function to that pub/sub channel.
4. Set GCP Secrets Manager values as follows (with appropriate permissions):

Name | Value
------------ | -------------
consumer_key | your twitter API key
consumer_secret | your twitter API key secret
access_token | generated twitter access token
access_secret | generated twitter access token secret

### Branches

*gcp_implementation:*

- [x] Gather top exploits/vulnerabilities from https://cvedetails.com and sift through data to find most recently updated 8+ CVSS score CVE

- [x] Each month, report on 1 of 4 categories: SQLi, Remote Execution, DDoS & Privilege Escalation

- [x] Run in Google Cloud Platform as a Cloud Function, triggered on the first day of each month, at 10:00 GMT by GCP Cloud Scheduler and pub/sub channel

- [x] API keys/tokens from twitter in GCP Secrets Manager

- [ ] Report on top 3 most recently modified CVE's of the week
 
- [ ] Integrate json data from https://nvd.nist.gov

## Developed by Jack
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk
