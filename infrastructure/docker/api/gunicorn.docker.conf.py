proc_name = "gunicorn"

bind = "0.0.0.0:9000"

loglevel = "DEBUG"
accesslog = "/data/access.log"
errorlog = "/data/error.log"

keepalive = 1
timeout = 300
workers = 5
worker_class = "gevent"
