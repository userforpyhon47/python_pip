FROM python:3.10

WORKDIR /web-server

COPY . /web-server

RUN pip3 install --no-cache-dir --upgrade -r /web-server/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "charts:app", "--host", "0.0.0.0", "--port", "8080"]