FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install uwsgi
RUN mkdir -p /usr/config/
COPY docker-config/uwsgi.ini /usr/config/
COPY docker-config/supervisor-app.conf /etc/supervisor/conf.d/

VOLUME /usr/src/app
EXPOSE 9001

CMD ["supervisord", "-n"]