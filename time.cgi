#!/usr/bin/env python
import cgi
import Cookie
import pymysql
form = cgi.FieldStorage()
if form.getvalue('MENU'):
   dish = form.getvalue('MENU')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()
cur.execute("""INSERT into dish (dish_name)
                  values (%s)""",
                  (dish))
print "Content-type :text/html"
print ""
print ""
print """
<html>
<head>
<title>
Time
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style2.css" type="text/css" />

<body>

<div id="facebook-Bar">

  <div id="facebook-Frame">

    <div id="logo"> <img src="food.jpg"> </div>
    
    </div>
 </div>
 <div class="loginbox radius">

  <h2 style="color:#141823; text-align:center;"><font face="Verdana">What meal are you looking for?</font></h2>

  <div class="loginboxinner radius">

    <div class="loginheader">


    </div>

   <div class="loginform">

      <form id="login" action="last.cgi" method="post">
         <p><h1>
		<input type="radio" name="MEAL" value="Lunch" /> Lunch<br />
		<input type="radio" name="MEAL" value="Dinner" /> Dinner<br />
		<input type="submit" value="Submit Timing" />

		</p></h1>
	</form>
	</div>
	</div>
	</body>
	</html>
	 """

conn.commit()

