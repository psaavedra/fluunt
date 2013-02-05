#! /bin/bash

RECORDER=/usr/local/bin/recorder-http-libav

URL="http://host:8000/media.ts"
KEY="npvr"
WORKDIR="/tmp/"
CHUNKDURATION=10
SOCKETTIMEOUT=10


if [ $# -eq 0 ]
then
	echo "
Usage: $0 $URL $KEY $WORKDIR $CHUNKDURATION $SOCKETTIMEOUT
	"
	exit -1
fi

URL=$1
KEY=$2
WORKDIR=$3
CHUNKDURATION=$4
SOCKETTIMEOUT=$5

mkdir -p $WORKDIR/ts/$KEY/

while [ 1 ]
do
    wget -t 1 -T $SOCKETTIMEOUT -q -O - $URL | $RECORDER  -w $WORKDIR -K $KEY -C $CHUNKDURATION -i -
    sleep 1.5
done
