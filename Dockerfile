FROM python:2.7-alpine
RUN pip install pyowm
COPY getweather.py /
ENTRYPOINT ["./getweather.py"]
