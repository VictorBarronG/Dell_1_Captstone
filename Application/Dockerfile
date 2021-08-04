# FROM python:alpine3.8
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE 5000
# CMD python ./app.py

FROM python:3.8
#LABEL maintainer="raul.c.pena@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]