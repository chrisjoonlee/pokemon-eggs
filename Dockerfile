FROM python:3.10.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY=";kC@]8VsHkn_RD,[.P@UR!Lc/{A%#iR4Y|;KjWj:py.XZjaoP=Q9^8yo'`=,]!"
ENV FLASK_DEBUG=True
ENV DB_USER=pokemon_eggs
ENV DB_PASSWORD=udnvLYfb59
ENV DB_URL=postgresql://pokemon_eggs:udnvLYfb59@localhost/pokemon_eggs_db

CMD ["flask", "run", "--host=0.0.0.0"]