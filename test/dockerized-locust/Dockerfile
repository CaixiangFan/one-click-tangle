FROM python:3.8

COPY . /build
RUN cd /build && pip install . && pip install PyOTA && rm -rf /build

EXPOSE 8089 5557

RUN useradd --create-home locust
USER locust
WORKDIR /home/locust
COPY *.py .
ENTRYPOINT ["locust"]

# turn off python output buffering
ENV PYTHONUNBUFFERED=1