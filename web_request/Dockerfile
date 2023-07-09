FROM python:3.10

WORKDIR /web_request

COPY requirements.txt /web_request/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /web_request/requirements.txt

COPY . /web_request

CMD bash -c "while true; do sleep 1; done"