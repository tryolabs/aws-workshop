proc_name = "gunicorn"

bind = "0.0.0.0:9000"

daemon = True
pidfile = "/var/run/gunicorn.pid"

loglevel = "DEBUG"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"

keepalive = 1
timeout = 300
workers = 5
worker_class = "gevent"
