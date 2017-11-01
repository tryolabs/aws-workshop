FROM node:8

RUN mkdir /app

WORKDIR /app

RUN npm install -g serve

COPY frontend /app

RUN npm install

ENV REACT_APP_USE_OWN_API=true
RUN npm run build

EXPOSE 5000
CMD [ \
  "serve", \
  "-s", \
  "build" \
]
