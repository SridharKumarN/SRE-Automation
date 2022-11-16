#!/usr/bin/env python

"""This python script sample is used to check Telecom Applications of TIMESTEN DBs 
:Prepaid_DSN1, 
 Prepaid_DSN2, 
 TOLLFREE_DSN3 Services
Timesten DB Instance is in Sync with Master or not.
This Script doesn't requires any input while execution."""

from datetime import datetime
import os
import subprocess
import math
import re
import time
import sys
import logging


#List of SUPPORT OS Applications -Replication to be checked.
telecom_os_apps=['Prepaid_DSN1','Prepaid_DSN2','TOLLFREE_DSN3']

def main( ):
    log_format = "%(asctime)s::%(levelname)s::%(message)s"
    LOG_FILENAME = '/home/timesten/Scripts/log/tt_rep_check.log'
    logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO,filemode='w',format=log_format)
    today = datetime.now()
    etime_mail = today.strftime("%H%M")
    #print etime_mail
    logging.info('Good Day!SRE Team - Let Me start Replication check by Python Automation.')
    logging.info('------------------------------------------------------------------------------------------')
    logging.info('SUPPORT OS - Prepaid_DSN1,Prepaid_DSN2,TOLLFREE_DSN3 Replication Check Started at %s',today)
    b_sum=0
    s_sum=0
    for telecom_app in telecom_os_apps:
       #print "---------------------",telecom_app,"Rep-Check-------------"
       logging.info('-------------------------- Check for DSN:%s --------------------------------------------',telecom_app)
       B_C=t_bookmark(telecom_app)
       print B_C
       logging.info('Expected Replication hold LSN/Last written LSN is > 0.95, Observed is %s.',B_C)
       if B_C > 0.95:
          #print "DSN:",telecom_app, "BookMark value is as per expectation."
          logging.info('DSN:%s BookMark value is as per expectation.',telecom_app)
          b_sum = b_sum + 1
       else:
          time.sleep(60)
          B_C=t_bookmark(telecom_app)
          if B_C > 0.95:
             #print "DSN:",telecom_app, "BookMark value is as per expectation - After 2nd Check."
             logging.info('DSN:%s BookMark value is as per expectation after 2nd Check',telecom_app)
             b_sum = b_sum + 1
          else:
             #print "DSN:",telecom_app,"BookMark value is not ok."
             logging.error('DSN:%s BookMark value difference is more b/w hold LSN,Last LSN,Please check.',telecom_app)
       #print ""
       #logging.info('')
       check=t_sync_check(telecom_app)
       if (check == True):
          #print "DSN:",telecom_app, "Subscribers node Sync is working Properly."
          logging.info('DSN:%s Subscribers node Sync is working Properly.',telecom_app)
          s_sum = s_sum + 1
       else:
           #print "DSN:",telecom_app,"Subscriber node Sync is not working Properly."
           logging.error('DSN:%s Subscribers node Sync is not working Properly.please check.',telecom_app)
    logging.info('------------------------------------------------------------------------------')
    logging.info('Take Action if Error message printed.')
    logging.info('Have a Good Day!Stay Home, Save Lives!!')
    time.sleep(5)
    print "------------------If Parameters--------------------"
    print b_sum
    print s_sum
    print "------------------Mail-Trigger--------------------"
    if ( s_sum  != 3):
       cmd="""cat /home/timesten/Scripts/log/tt_rep_check.log | mailx -s 'TIMESTEN |REPLICATION CHECK | STATUS is Red!' Drkalam@xyz.com"""
       p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
       output, errors = p.communicate()
       print errors,output
       print "if None: i.e. No error while sending Mail"
	elif (int(etime_mail) == 0900):
       cmd="""cat /home/timesten/Scripts/log/tt_rep_check.log | mailx -s 'TIMESTEN|REPLICATION CHECK | STATUS is Green!' Drkalam@xyz.com"""
       p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
       output, errors = p.communicate()
       print errors,output
       print "if None: i.e. No error while sending Mail"
    else:
        print "ALL IS WELL. Hence No Need Mail Trigger"

def t_bookmark(telecom_os_apps):
    b_value=[]
    bookmark = subprocess.Popen(["ttrepadmin", "-bookmark", telecom_os_apps], stdout=subprocess.PIPE)
    for b_line in bookmark.stdout:
        b_splitline = b_line.split("/")
        b_value.append(b_splitline[1].rstrip('\n'))
    print b_value
    logging.info('Replication hold LSN,Last written LSN,Last LSN forced to disk values: %s',b_value)
    B_A=float(b_value[0])
    B_B=float(b_value[1])
    B_C=B_A/B_B
    return B_C

def t_sync_check(telecom_os_apps):
    s_value=[]
    sum_s_valve_line = 0
    Sync_Check = subprocess.Popen(["ttrepadmin", "-dsn", telecom_os_apps, "-receiver", "-list"], stdout=subprocess.PIPE)
    for s_line in Sync_Check.stdout:
         if re.search(r":",s_line):
            s_splitline = s_line.split(":")
            s_value.append(s_splitline[1].rstrip('\n'))
    print s_value
    logging.info('Last Msg Sent to All Subscriber values in Minutes(All Should be 0) : %s',s_value)
    for s_valve_line in s_value:
        int_s_valve_line= int (s_valve_line)
        sum_s_valve_line = sum_s_valve_line + int_s_valve_line
    if (sum_s_valve_line  == 0 ):
       return True
    else:
       return False

if __name__ == '__main__':

    main()
