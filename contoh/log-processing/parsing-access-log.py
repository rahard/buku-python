import apache_log_parser
line_parser = apache_log_parser.make_parser("%a %l %u %t \"%r\" %>s %b") 

from pprint import pprint

# baris = '103.90.64.250 - - [14/Apr/2018:06:25:08 +0700] "GET /weatherstation/updateweatherstation.php?ID=IBANDUNG8&tempf=69.80&humidity=59.00&softwaretype=BRIotv1&action=updateraw&realtime=1&rtfreq=5 HTTP/1.1" 502 172 "-" "-"'

count=1

import fileinput
for baris in fileinput.input():
   if "ID" in baris:
      hasil = line_parser(baris)
      #pprint(hasil)
   
      waktu = hasil['time_received_datetimeobj']
   
      webdata = hasil['request_url_query_simple_dict']
      #pprint(webdata)
   
      # kumpulkan hasil
      id = webdata['ID']
      tempf = webdata['tempf']
      humidity = webdata['humidity']
      print(count, waktu, id, tempf, humidity)
      # print(count, end=', ')
      # print(waktu, end=', ')
      # print(id, end = ', ') 
      # print(tempf, end = ', ')
      # print(humidity)
      count = count+1
