FROM python:3.6.9-alpine

WORKDIR /src/website

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN python3 -m pip install --upgrade pip

COPY src/requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 7007

COPY src .

CMD [ "python3", "app.py" ]