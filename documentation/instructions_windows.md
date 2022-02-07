# Windows Scheduling Instructions

Scheduling for Windows is easy once you understand what's required.

## A. Find the `root path` where these scripts are located on your computer
1. For me it is `C:\Users\coryr\OneDrive\Documents\GitHub\NiceHash-Mining-Scheduler`
   1. Keep this location for later

## B. Update the .bat files:
1. Find where python is located 
   1. Open cmd and type `where python`
   2. For me it was `C:\Users\coryr\AppData\Local\Programs\Python\Python39\python.exe`
2. Open `windows_start_mining.bat` and `windows_stop_mining.bat` and replace the first quoted part with your python location

## C. Windows Task Scheduler
1. Hit Windows key and type `Task scheduler`
2. On the left side, expand the `Task Scheduler Library`
3. Create a new folder called Nicehash
4. Inside this folder we're going to create 2 basic tasks 

## D. Schedule turning ON miner
1. Right click on the folder you created, click `Create Basic Task`
2. Name is `Turn on miner` *click next*
3. Set schedule to Daily - *click next*
4. Set the miner to turn on at your desired time (mine is 9pm) - *click next*
5. Select `Start a program` as the desired `Action` - *click next*
6. Under `Start a program` browse for the script `windows_start_mining.bat`
   1. For `Start in (optional)` add the `root path` you found from `step A` *click next*
7. *Click finish*

## E. Schedule turning OFF miner
1. Right click on the folder you created, click `Create Basic Task`
2. Name is `Turn off miner` *click next*
3. Set schedule to Daily - *click next*
4. Set the miner to turn off at your desired time (mine is 4pm) - *click next*
5. Select `Start a program` as the desired `Action` - *click next*
6. Under `Start a program` browse for the script `windows_stop_mining.bat`
   1. For `Start in (optional)` add the `root path` you found from `step A` *click next*
7. *Click finish*

***Congratulations, your miner(s) should be scheduled.***

## F. Testing your scripts
1. Select your script from the Task Scheduler
2. Click run on the right side
