FROM python:3.6.9-alpine

# Set the working directory in the container to /src/website
WORKDIR /src/website

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

# Upgrade pip
RUN python3 -m pip install --upgrade pip

COPY src/requirements.txt requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# Unblock port 7007 for the Flask app to run on
EXPOSE 7007

COPY src .

CMD [ "python", "app.py" ]