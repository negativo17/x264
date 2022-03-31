#!/bin/sh
set -e

git clone https://code.videolan.org/videolan/x264.git x264

cd x264

API=$(grep '#define X264_BUILD' x264.h | awk '{print $3}')
COMMIT=$(git rev-list HEAD -n1)
SHORTCOMMIT=$(echo ${COMMIT:0:7})
DATE=$(git log -1 --format=%cd --date=short | tr -d \-)
rm -fr .git*

cd ..

tar -cJf x264-0.$API-$SHORTCOMMIT.tar.xz x264
rm -fr x264

sed -i \
    -e "s|%global commit0.*|%global commit0 ${COMMIT}|g" \
    -e "s|%global date.*|%global date ${DATE}|g" \
    -e "s|%global api_version.*|%global api_version ${API}|g" \
    x264.spec

rpmdev-bumpspec -c "Update to latest snapshot." x264.spec
