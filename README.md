# connection-latency-tests

Usage and example output:

```
$ python -m venv venv
$ pip install -r requirements.txt
$ ./cxn tcp tls http keepalive
TCP handshake requests:
  50th percentile: 0.06515071400000005
  90th percentile: 0.07143438169999992
  95th percentile: 0.07347477034999997
  99th percentile: 0.07510708127
  100th percentile: 0.075515159
TLS handshake requests:
  50th percentile: 0.20956318949999986
  90th percentile: 0.2161831738999999
  95th percentile: 0.2170044909499999
  99th percentile: 0.21766154458999995
  100th percentile: 0.21782580799999995
HTTTP requests:
  50th percentile: 0.2842054665
  90th percentile: 0.30312922519999974
  95th percentile: 0.30902286709999993
  99th percentile: 0.3137377806200001
  100th percentile: 0.3149165090000001
HTTP requests with keep-alive:
  50th percentile: 0.07146362849999965
  90th percentile: 0.10463262520000004
  95th percentile: 0.18401473210000002
  99th percentile: 0.24752041762000032
  100th percentile: 0.2633968390000003
```
