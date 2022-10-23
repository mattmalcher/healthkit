FROM python:3.9.2-slim-buster

RUN apt update
RUN apt install -y python3-dev gcc spatialite-bin libsqlite3-mod-spatialite wget unzip

RUN pip install datasette datasette-leaflet-geojson datasette-block-robots

ENV SQLITE_EXTENSIONS /usr/lib/x86_64-linux-gnu/mod_spatialite.so

EXPOSE 8001

CMD ["datasette", "serve", "timezones.db", "--host", "0.0.0.0", "--cors", "--port", "8001", "--inspect-file", "inspect-data.json", "-m", "metadata.json", "--template-dir", "templates"]
