# docker build -t hiroga/flask-repeat-after-me .
# docker run --rm -p 5000:5000 hiroga/flask-repeat-after-me
# docker push hiroga/flask-repeat-after-me
FROM python:3.6.8-alpine3.9
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
ADD app.py /app
ENTRYPOINT ["python","app.py"]
