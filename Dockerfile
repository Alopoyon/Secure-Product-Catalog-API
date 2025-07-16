FROM python:3. as base

WORKDIR /catalog

COPY ./requirements.txt /catalog/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /catalog/requirements.txt

COPY ./app /catalog/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]