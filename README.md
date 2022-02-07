# NiceHash Mining Scheduler
 
Use this script to schedule all of your NiceHash Miner(s) to turn on and off at certain times of the day.

Electricity costs between 4-9pm are high in my area and I want NiceHash to stop mining during those times. This script should start and stop your rigs on a schedule. 

`Setting up this scheduling process could take up to 1 hour depending on your skill level`

## Installation

Acquire the necessary files by downloading the [latest release](https://github.com/SeaRoth/NiceHash-Windows-Scheduler/releases). Save and extract the files to a directory of your choosing or download using your preferred method.

## API Configuration

1. Open the NiceHash [API key](https://www.nicehash.com/my/settings/keys) settings. Take note of your organization id located at the top of the page. (Ex. 01234567-0123-0123-0123-012345678900)

2. Create an API key. You can make the App Name whatever you want. I recommend changing the API permissions to `only` allow "Mining permissions" and "Manage Rigs" as this is all that is required for the script to function. Take note of the "API Key Code" (public key) and the "API Secret Key Code" (private key). Make sure you complete the process of activating the new API key.

3. Put the `public api key`, `private api key` and `organization id` into their respective locations inside config.json
   
## Python, Pip and Requests Configuration
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

Run the `test_api.py` script before setting up the Windows Task Scheduler or Cron job. 

Using a shell of your choice ([terminal](https://www.businessinsider.com/how-to-open-terminal-on-mac#:~:text=The%20Mac%20Terminal%20is%20a,Mac's%20Finder%20or%20through%20Spotlight.), [cmd](https://www.lifewire.com/command-prompt-2625840)) navigate to the directory where `test_api.py` is located and type `python test.py` (for Windows) or `python3 test.py` (for mac).

If it worked then you should see a list of your rigs and then 'Finished' at the bottom.

If it didn't work then read the error messages and troubleshoot.

# Actual Testing

1. *Make sure the inital testing works*
2. Go to https://www.nicehash.com/my/mining/rigs and determine whether your rigs are mining or stopped
3. Open a terminal/cmd prompt to the `root folder` of this project
4. If they are stopped, run `python start_mining.py` (Windows) `python3 start_mining.py` (MAC), refresh the rigs page and they should start
5. If they are mining, run `python3 start_mining.py` (Windows) `python3 stop_mining.py` (MAC), refresh the rigs page and they should stop

# Setting up a custom schedule (choose 1)

1. Using `Windows` [Task Scheduler](documentation/instructions_windows.md)

1. Using `CronTab` (`not tested yet`):

If you would like to run this script on your own schedule using [crontab](https://www.hostinger.com/tutorials/cron-job), you can pass '--cron' as a command line argument. Passing this argument will suppress the automatic 4 hour loop, and the script will only execute once.

You can use [Crontab Generator](https://crontab-generator.org/) to quickly generate a custom crontab command.

**Note:** Crontab runs in your home directory by default. If you saved the script to a different directory, you will have to tell cron to change directories before running the script.

Ex:

```
* */4 * * * cd /home/[USER]/NiceHash-Windows-Scheduler && python3 start_schedule.py --cron >/dev/null 2>&1
* */4 * * * cd /home/[USER]/NiceHash-Windows-Scheduler && python3 stop_schedule.py --cron >/dev/null 2>&1
```

## Donations

#### `BTC:` 3LBcrMcyGSNKJoat8dbPseqtomNBe79Yu5
#### `ETH:` 0x7579c17a57aFF6d40472A1e21b13D197Fd0116a7
#### `LRC:` 0x33F94f644B36AD13f232154a4C0D79c29a9656DC
#### `MANA:` 0x0d68D933582dB964CC5E31Fe305aC59026e0Aab1
#### `MATIC:` (from Ethereum network): 0x5549d1536c2eacC50e8773c9241581465650f5eF
#### `XRP:` rw2ciyaNshpHe7bCHo4bRWq6pqqynnWKQg TAG: 3272534061
