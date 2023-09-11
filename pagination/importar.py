#!/usr/bin/python3
import csv
import urllib.request
from io import StringIO

url = 'https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230911%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230911T161522Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=52a8700cce22c751c1c58fc35238055aa6648518fe66ed25dcb33e91b3a714f1'
respuesta = urllib.request.urlopen(url)
f = StringIO(bytearray(respuesta.read()).decode())
archivo = csv.reader(f)
with open("Popular_Baby_Names.csv", 'w') as fil:
    fil.write(respuesta.read().decode())

