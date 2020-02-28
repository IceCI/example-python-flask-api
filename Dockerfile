FROM python:3.7

EXPOSE 8080
WORKDIR /code/
ENV PYTHONPATH /code/

ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn gevent

ADD quotes.py /code/quotes.py

CMD ["gunicorn", "--worker-class", "gevent", "--access-logfile", "-", "--capture-output", "--enable-stdio-inheritance", "-b", "0.0.0.0:8080", "quotes:app"]
