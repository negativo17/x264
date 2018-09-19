#!/bin/sh
set -e

git clone git://git.videolan.org/x264.git -b stable x264

cd x264

API=$(grep '#define X264_BUILD' x264.h | awk '{print $3}')
COMMIT=$(git rev-list HEAD -n1)
SHORTCOMMIT=$(echo ${COMMIT:0:7})
DATE=$(git log -1 --format=%cd --date=short | tr -d \-)
rm -fr .git*

cd ..

tar -cJf x264-0.$API-$SHORTCOMMIT.tar.xz x264
rm -fr x264

echo %global commit0 $COMMIT
echo %global date $DATE
echo %global api_version $API
