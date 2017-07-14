from urllib import * 

url_request = urlopen('http://entercloud.info/index_ccc.html')
ec_ui = url_request.read()

