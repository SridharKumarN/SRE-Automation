# SRE-Automation
Day-to-Day usage of SRE Automations 


I. Timesten DB/Instance Replication Monitoring
    As you have many ways to monitori TIMESTEN DB, Here is another Way to Monitoring Timesten Database /Instance as well Data Synchronization using Python Script. 
    As a Pre-Requsite, This Does requires Mailx to trigger Email Alert. 

    this is created for Telecom Application, It can be adopted for any Industry where Timesten Replication Monitoring is requried for daily basis by placing a cronjob. 

II. Delete Many Folders Old Files based on Disk Space/Disk Utilization not based on Number of Days. i.e Dynamic Dates 

   we usually do housekeeping based on number of days older files or random delete based on Diskspace alert.
   Here is another requriement of Staging server, where we need to keep old files as much as possible. Only Housekeeping required when it requires 90% and delete oldest    files. Kind of Different approch has been implemented using Python. 
   Condition:
    1. Check /data particular Partition directory is 90%
    2. if yes, check the unixtime of last file (oldest log file)
    3. Remove all the files from oldest files to 24hrs. (i.e delete one day file)
    4. Loop the same process untill 90% below observed.
    5. Cron the job daily once or twice based on log flow.
