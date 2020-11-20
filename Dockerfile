FROM ubuntu

WORKDIR /app
COPY . .

RUN apt update
RUN apt install make

RUN make init

CMD ["make", "run"]