# NiceHash Mining Scheduler
 
Use this script to schedule your NiceHash Miner(s).

Electricity costs between 4-9pm are high in my area and I want NiceHash to stop mining during those times. This script should start and stop your rigs on a schedule. 

## Installation

Acquire the necessary files by downloading the [latest release](https://github.com/SeaRoth/NiceHash-Windows-Scheduler/releases). Save and extract the files to a directory of your choosing.

## Configuration

1. Open the NiceHash [API key](https://www.nicehash.com/my/settings/keys) settings. Take note of your organization id located at the top of the page. (Ex. 01234567-0123-0123-0123-012345678900)

2. Create an API key. You can make the App Name whatever you want. I recommend changing the API permissions to `only` allow "Mining permissions" and "Manage Rigs" as this is all that is required for the script to function. Take note of the "API Key Code" (public key) and the "API Secret Key Code" (private key). Make sure you complete the process of activating the new API key.

3. Install python and and pip and requests for your operating system. These are my suggestions, do as you wish :)
### Windows:
1. Install Visual Studio Code
2. Go to plugins and install python or follow these instructions (https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/)
3. Install Pip (https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
4. Use pip to install requests (https://docs.python-requests.org/en/master/user/install/)

### MAC:
1. Install Visual Studio Code
2. Go to plugins and install python
3. Install Pip (https://www.geeksforgeeks.org/how-to-install-pip-in-macos/)
4. Use pip to install requests (https://docs.python-requests.org/en/master/user/install/)

# Initial Testing

Run the test script before setting up the Windows Task Scheduler or Cron job. Once you have added your API key, secret and organization ID in config.json and installed python and requests, you should be able to run the test script.

Using a shell of your choice (terminal, powershell, command prompt) navigate to the directory where `test.py` is located and type `python test.py` (for Windows) or `python3 test.py` (for mac).

If it worked then you should see a list of your rigs and then 'Finished' at the bottom.

# Actual Testing

1. Make sure everything is setup and the inital testing works
2. Go to https://www.nicehash.com/my/mining/rigs and determine whether your rigs are mining or stopped
3. If they are stopped, run `python3 start_schedule.py`, refresh the rigs page and they should start
4. If they are mining, run `python3 stop_schedule.py`, refresh the rigs page and they should stop

# Cron (Not finished)

### Using Windows Task Scheduler:

### Using CronTab:

If you would like to run this script on your own schedule using [crontab](https://www.hostinger.com/tutorials/cron-job), you can pass '--cron' as a command line argument. Passing this argument will suppress the automatic 4 hour loop, and the script will only execute once.

You can use [Crontab Generator](https://crontab-generator.org/) to quickly generate a custom crontab command.

**Note:** Crontab runs in your home directory by default. If you saved the script to a different directory, you will have to tell cron to change directories before running the script.

Ex:

```
* */4 * * * cd /home/[USER]/AutoWithdraw && python3 start_schedule.py --cron >/dev/null 2>&1
* */4 * * * cd /home/[USER]/AutoWithdraw && python3 stop_schedule.py --cron >/dev/null 2>&1
```

## Donations

### BTC: 3LBcrMcyGSNKJoat8dbPseqtomNBe79Yu5
### ETH: 0x7579c17a57aFF6d40472A1e21b13D197Fd0116a7
### LRC: 0x33F94f644B36AD13f232154a4C0D79c29a9656DC
### MANA: 0x0d68D933582dB964CC5E31Fe305aC59026e0Aab1
### MATIC (from Ethereum network): 0x5549d1536c2eacC50e8773c9241581465650f5eF
### XRP: rw2ciyaNshpHe7bCHo4bRWq6pqqynnWKQg TAG: 3272534061
