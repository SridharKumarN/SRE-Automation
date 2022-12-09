#!/bin/bash
#set -x
#This Script is part of XML File format and transfer to different loaction.
#################################################################
#       Declare Variables
#################################################################

ORGIN_LOCATION=/logs/testdir/ORGIN_XML
DESTINATION_DIRECTORY=/logs/testdir/DEST_XML

LOCKFILE=/tmp/xml_transfer.lock

# check if lock file exists
if [ -f $LOCKFILE ]; then
  echo "xml_transfer.sh is already running"
  find /tmp -type f -name "xml_transfer.lock" -mmin +60 | xargs rm -f
else
# create a lock file
touch $LOCKFILE
# Navigate to the folder containing the CDR Files transferred by NOAS CSG STG(Rhino)
cd $ORGIN_LOCATION
for folder in *; do
if [ -d "$folder" ]; then
mkdir -p $DESTINATION_DIRECTORY/$folder
        # Retrieve the filelist of the XMLs generated and gunzip.
        cd ${ORGIN_LOCATION}/$folder
        ls -lthr XML_*.gz |awk '{print $9}'|head -100 > /tmp/gzfilelist
        for gzfile in `cat /tmp/gzfilelist`
        do
        chmod 775 $gzfile
        sleep 1
        gunzip $gzfile
        done
        rm /tmp/gzfilelist
        #remove lock file

        # Retrieve the filelist of the XMLs unzipped .
        ls -lthr XML_*|grep -v ".gz" | awk '{print $9}'|head -100 > /tmp/filelist
        for file in `cat /tmp/filelist`
        do
        xmllint --format $file > $DESTINATION_DIRECTORY/$folder/$file.xml
        sleep 1
        done
        rm /tmp/filelist
        #remove lock file
cd $ORGIN_LOCATION
fi
done
rm $LOCKFILE
# End of script
fi
