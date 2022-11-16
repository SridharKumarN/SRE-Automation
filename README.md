# SRE-Automation
Day-to-Day usage of SRE Automations 


1. Timesten DB/Instance Monitoring
    As you have many ways to monitori TIMESTEN DB, Here is another Way to Monitoring Timesten Database /Instance as well Data Synchronization using Python Script. 
    As a Pre-Requsite, This Does requires Mailx to trigger Email Alert. 

    this is created for Telecom Application, It can be adopted for any Industry where Timesten Monitoring is requried for daily basis by placing a cronjob. 

2. Delete Many Folder Old Files based on Disk Space/Disk Utilization not based on Number of Days. 

   we usually do housekeeping based on number of days older files or random delete based on Diskspace alert.
   Here is another requriement of Staging server, where we need to keep old files as much as possible. Only Housekeeping required when it requires 90% and delete oldest    files. Kind of Different approch has been implemented using Python. 
