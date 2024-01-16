FROM python:3.9

MAINTAINER anmol "anmol.singh@nativetouch.com"

COPY . /app

WORKDIR /app
RUN pip install --upgrade pip

RUN pip install setuptools

RUN pip install -r ./requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "src/application.py" ]