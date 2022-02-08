# Windows Scheduling Instructions

Scheduling for Windows is easy once you understand what's required.

## A. Find the `root path` where these scripts are located on your computer
1. For me it is `C:\Users\coryr\OneDrive\Documents\GitHub\NiceHash-Mining-Scheduler`
   1. Keep this location for later

## B. Update the .bat files:
1. Find where python is located 
   1. Open cmd and type `where python`
   2. For me it was `C:\Users\coryr\AppData\Local\Programs\Python\Python39\python.exe`
   3. ![image](https://user-images.githubusercontent.com/3461713/152732529-2b469bcb-6780-4984-914d-788a579904a6.png)
   4. A shortcut to the above location is `%LocalAppData%\Programs\Python\Python39\python.exe`
2. Open `windows_start_mining.bat` and `windows_stop_mining.bat` and replace the first quoted part with your python location

## C. Windows Task Scheduler
1. Hit Windows key and type `Task scheduler`
2. On the left side, expand the `Task Scheduler Library`
3. Create a new folder called Nicehash
4. Inside this folder we're going to create 2 basic tasks ![image](https://user-images.githubusercontent.com/3461713/152732656-a7addf98-b7c8-441b-b1c7-f7e392666956.png)
5. Also, to help with troubleshooting, `Enable All Tasks History` in the Actions menu \n ![image](https://user-images.githubusercontent.com/3461713/153086146-80b5b411-0d88-4dce-be6c-52a28520de80.png)


## D. Schedule turning ON miner
1. Right click on the folder you created, click `Create Basic Task`
2. Name is `Turn on miner` *click next* \n ![image](https://user-images.githubusercontent.com/3461713/152732920-ae64448d-8644-4712-86c3-4bf63a10d60a.png)

3. Set schedule to Daily - *click next* \n ![image](https://user-images.githubusercontent.com/3461713/152732963-0d02b688-d605-4907-b9a5-9b1935cc9880.png)

4. Set the miner to turn on at your desired time (mine is 9pm) - *click next* \n ![image](https://user-images.githubusercontent.com/3461713/152733011-efbb6bf2-7b20-4da0-bb7c-840980c76181.png)

5. Select `Start a program` as the desired `Action` - *click next* \n ![image](https://user-images.githubusercontent.com/3461713/152733034-94bf6658-78c7-4e28-9b86-8ede6da48608.png)

6. Under `Start a program` browse for the script `windows_start_mining.bat`
   1. For `Start in (optional)` add the `root path` you found from `step A` *click next* \n ![image](https://user-images.githubusercontent.com/3461713/152733095-c3ae3852-80bf-4435-8eae-18fba68f1fa8.png)

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
2. Click `run` on the right side \n ![image](https://user-images.githubusercontent.com/3461713/152733164-28981d85-803c-4e94-bc08-bea6fe7e7a61.png)

