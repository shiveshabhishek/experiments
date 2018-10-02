This code is made to ping every hour on slack. I've written this code with the syntax of `Python3`

## Pre-requisites
- Slack dependencies:
First, create an application in slack, then get the WebHook URL from slack.
- Python Dependencies:
httplib2 
```
pip3 install httplib2
```

N.B. : You need to run this in background so as to receive the notificiations every hour. For doing the same in ubuntu, use the commands below:

```
chmod +x slack_time_notify.py
nohup /path/to/slack_time_notify.py &
```
Do not forget to use `&` to put it in background.

To see this process , run the below command:
`ps ax | grep slack_time_notify.py`
