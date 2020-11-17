FROM python:3.8

RUN mkdir /app
WORKDIR /app/
COPY . /app

RUN pip install --upgrade -r requirements.txt

EXPOSE 7000

CMD python run.py --env production
