FROM python:3.7.0

COPY requirements.txt requirements.txt
RUN mkdir -p /home/q/marmot/src /home/q/marmot/log \
&& pip install --upgrade pip \
&& pip install -r requirements.txt -i http://pypi.douban.com/simple/  --trusted-host pypi.douban.com

WORKDIR /home/q/marmot/src