#!/usr/bin/env sh

set -e

IMAGE_VERSION=1.0
IMAGE_NAME=marmot

echo '注意：本次构建的镜像为'${IMAGE_NAME}:${IMAGE_VERSION}
sudo docker build -t $IMAGE_NAME:${IMAGE_VERSION} .
