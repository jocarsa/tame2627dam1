#!/usr/bin/env python3
import datetime
archivo = open('/home/josevicente/cron/current_datetime.txt', 'w')
current_datetime = datetime.datetime.now()
archivo.write(current_datetime.strftime('%Y-%m-%d %H:%M:%S'))
archivo.close()