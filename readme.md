# TweeVEBot:

A twitter bot tweeting interesting cyber security realted updates, including vulnerabilties from various sources in concise intersting ways.

Form two (Current):
> Gather top exploits/vulnerabilities from multiple sources, and compile a top 3 of the most common types of new attack vectors monthly.

> Decided on these 4 categories: SQLi, Remote Execution, DDoS & Privilege Escalation

> Working on monthly updates on different types of CVEs

> Types include: SQLi, DDoS, Remote Code Execution and Privilege Escalation

> Perhaps a feature that will respond to tweets mentioning the bots account

Crontab config (for 15:00 on first dat of each month)

0 15 1 1 * python3 main.py -m 0

0 15 1 2 * python3 main.py -m 1

0 15 1 3 * python3 main.py -m 2

0 15 1 4 * python3 main.py -m 3

0 15 1 5 * python3 main.py -m 0

0 15 1 6 * python3 main.py -m 1

0 15 1 7 * python3 main.py -m 2

0 15 1 8 * python3 main.py -m 3

0 15 1 9 * python3 main.py -m 0

0 15 1 10 * python3 main.py -m 1

0 15 1 11 * python3 main.py -m 2

0 15 1 12 * python3 main.py -m 3

Form one (Depricated):
> Tweets top 3 CVEs from https://cvedetails.com which have a CVSS score of at least 8+. Tweet includes recorded exploit count, affected products and generated tinyurl for more info

- Developed by Jack: https://jacksec.uk
