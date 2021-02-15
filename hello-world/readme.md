# Twitter bot designed for GCP:

*This is Python code from my video tutorial on making twitter bot in GCP. View the original video here:*
[![Alt text](https://img.youtube.com/vi/VID/0.jpg)](https://www.youtube.com/watch?v=qAKjd-PlZsI)

### GCP setup guide

1. Copy the contents of either the '*hello-world*' directories into a new GCP cloud function.
2. Set up a pub/sub channel with google cloud scheduler with the desired trigger time and date.
3. Subscribe your new cloud function to that pub/sub channel.
5. Add your twitter credentials to GCP Secrets Manager

### Branches

*gcp_implementation:*

- [x] Gather top exploits/vulnerabilities from https://cvedetails.com and sift through data to find most recently updated 8+ CVSS score CVE

- [x] Each month, report on 1 of 4 categories: SQLi, Remote Execution, DDoS & Privilege Escalation

- [x] Run in Google Cloud Platform as a Cloud Function, triggered on the first day of each month, at 10:00 GMT by GCP Cloud Scheduler and pub/sub channel

- [x] Environment variables in GCP are set to API keys/tokens from https://dev.twitter.com

- [ ] Report on top 3 most recently modified CVE's of the week
 
- [ ] Integrate json data from https://nvd.nist.gov

*master*

To be merged with gcp_implementation branch in next commit.

## Developed by Jack
![Alt Text](https://raw.githubusercontent.com/jacksec/jacksec.github.io/master/assets/img/logo.png)

https://jacksec.uk
