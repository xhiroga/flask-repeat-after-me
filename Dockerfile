# docker build -t hiroga/flask-repeat-after-me .
# docker run --rm -p 5000:5000 hiroga/flask-repeat-after-me
# docker push hiroga/flask-repeat-after-me
FROM python:3.6.8-alpine3.9
WORKDIR /app
ADD app.py /app
ADD requirement.txt /app
RUN pip install -r requirement.txt
ENTRYPOINT ["python","app.py"]