#!/bin/bash
DB=$1
FECHA=`date +"%Y%m%d_%H%M"`
DIA=`date +"%d"`

if [ $DIA -eq 1 ] || [ $DIA -eq 15 ]
then
#rm -rf /backup/*.gz
touch /backup/pp.txt
fi

ARCHIVO=$FECHA'_'$1.sql
#touch $FECHA'_'$1
mysqldump -u drinuxbackup $1>$ARCHIVO
gzip $ARCHIVO
mv $ARCHIVO.gz /backup
