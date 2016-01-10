#!/usr/bin/env python
import cgi
import Cookie
import os
import pymysql
import urllib
form = cgi.FieldStorage()
if form.getvalue('MEAL'):
  timings = form.getvalue('MEAL')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()
rows = cur.execute("""select * from dish""")
for row in cur.fetchall():
	dish_name = row
name_row = cur.execute("""select firstname from users""")
#to retreive the customer name
for row in cur.fetchall():
	 cust_name = row 
#to retreive the customer contact no
contact_row=cur.execute("""select contact from users""")
for row in cur.fetchall():
	contact_from= row
result = cur.execute("""select name from final_list where dish = %s and timings = %s""",(dish_name,timings))
if cur.rowcount>0:
	for row in cur.fetchall():
		name = row
result = cur.execute("""select contact no from final_list where dish = %s and timings = %s""",(dish_name,timings))
if cur.rowcount>0:
	for row in cur.fetchall():
		contact_to =row
	from pprint import pprint
	import requests
	from settings import sid, token
	def send_message(sid, token, sms_from, sms_to, sms_body):
		return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid = sid),
		   auth=(sid, token),
		   data={
				'From': sms_from,
				'To': sms_to,
				'Body': sms_body
		   })
	if __name__ == '__main__':
	# 'From' doesn't matter; For transactional, this will be replaced with your SenderId;
	# For promotional, this will be ignored by the SMS gateway
	# Incase you are wondering who Dr. Rajasekhar is http://en.wikipedia.org/wiki/Dr._Rajasekhar_(actor)
		r = send_message(sid, token,
		sms_from= contact_from,  # sms_from='8808891988',
		sms_to= contact_to, # sms_to='9052161119',
		sms_body='Hi,you will be visiting the restaurant today with %s' % cust_name)
		print r.status_code
		pprint(r.json())
		#for the second thingy
		r = send_message(sid, token,
		sms_from= contact_to,  # sms_from='8808891988',
		sms_to= contact_from, # sms_to='9052161119',
		sms_body='Hi,you will be visiting the restaurant today with %s' % name)
		print r.status_code
		pprint(r.json())
final_rows = cur.execute("""insert into final_list(name,contact,dish,timings)
				values(%s,%s,%s,%s)""",(cust_name,contact_from,dish_name,timings))
cur.execute("delete from dish")
print "Content-type :text/html"
print """
<html>
<head>
<title>
Last
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style2.css" type="text/css" />

<body>

<div id="facebook-Bar">

  <div id="facebook-Frame">

	<div id="logo"> <img src="/images/logo.jpg"> </div>
	
	</div>
 </div>
 <p><br /><br /><br />
 <h2 style="font-family:Verdana; text-align:center; color:black;">
		You will get a Text Message in some time.
		</h2>
 <p><br /><br /><br />
 
 <h2 style="font-family:Verdana; text-align:center; color:black;">
		Thanks for using SAVE IT SHARE IT
		</h2>
 <p>


 </body>
 </html>
 """

		