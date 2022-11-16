#!/usr/bin/python
import subprocess
import os, time, sys
########Variable Definition###########
path1 = "/data/abc-logpath/abc-logpath-subdir1"
now = time.time()
threshold = 5

##########Multiple Definiton Loop Call########
def check_once():
  df = subprocess.Popen(["df","-h","/data"], stdout=subprocess.PIPE)
  for line in df.stdout:
     print line
     splitline = line.decode().split()
     print splitline[5]
     if splitline[5] == "/data":
        if int(splitline[4][:-1]) > threshold:
           find_oldfile_date()

##########To Delete oldest File, Pick one particular subdirectory to choose OLDEST date ########          
def find_oldfile_date():
   os.chdir(path1)
   files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
   oldest = files[0]
   #newest = files[-1]
   print "Oldest:", oldest
   #print "Newest:", newest
   stat = os.stat(os.path.join(path1,oldest)).st_mtime
   #stat1 = os.stat(os.path.join(path1,newest)).st_mtime
   print (stat)
   #print (stat1)
   Perform_housekeep(stat)
   
##########Once Identified Oldest Date, Delete that Date files in all Subdirectories ########  
    
def Perform_housekeep(stat):
   print "I am doing Perform_housekeep"
   for path, subdirs, files in os.walk("/data/abc-logpath1/"):
       for name in files:
           if os.stat(os.path.join(path,name)).st_mtime < stat + 1 * 86400:
              print(os.path.join(path, name))
              os.remove(os.path.join(path, name))
   for path, subdirs, files in os.walk("/data/abc-logpath2/"):
       for name in files:
           if os.stat(os.path.join(path,name)).st_mtime < stat + 1 * 86400:
              print(os.path.join(path, name))
              os.remove(os.path.join(path, name))

   for path, subdirs, files in os.walk("/data/abc-logpath3/"):
       for name in files:
           if os.stat(os.path.join(path,name)).st_mtime < stat + 1 * 86400:
              print(os.path.join(path, name))
              os.remove(os.path.join(path, name))

   for path, subdirs, files in os.walk("/data/abc-logpath4/"):
       for name in files:
           if os.stat(os.path.join(path,name)).st_mtime < stat + 1 * 86400:
              print(os.path.join(path, name))
              os.remove(os.path.join(path, name))

   for path, subdirs, files in os.walk("/data/abc-logpath5/"):
       for name in files:
           if os.stat(os.path.join(path,name)).st_mtime < stat + 1 * 86400:
              print(os.path.join(path, name))
              os.remove(os.path.join(path, name))
              
#####Recheck Space reduced or not else form loop again#############
   check_once()
   
#########Main Function Call#########
check_once()
