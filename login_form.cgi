#!/usr/bin/env python
import cgi
import pymysql
form = cgi.FieldStorage()
#now get the values
email = form.getvalue('email')
password = form.getvalue('pass')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()
cur.execute("select * from users where email = %s and password = %s",(email,password))
if cur.rowcount == 0:
	print "Content-type: text/html"		
	print """
			Please sign up to use our service
		"""
else:
	print "Content-type: text/html"
	print """
			Welcome to Share it,Save it

			Choose from the list of restaurants below 


			<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style1.css" type="text/css" />

<body>

<div id="facebook-Bar">

  <div id="facebook-Frame">

    <div id="logo"> <img src="images/logo.jpg"> </div>
    
    </div>
 </div>

 
	
	 <div class="loginbox radius">

  <h2 style=color:#141823; text-align:center;"><font face="Verdana">What restaurant are you looking for?</font></h2>

  <div class="loginboxinner radius">

    <div class="loginheader">


    </div>

   <div class="loginform">

      <form id="login" action="dishes.cgi" method="post">
         <p><h1>
        <input type="radio" name="RES" value="r1" /> BBQ Nations<br />
		<input type="radio" name="RES" value="r2" /> Chillys<br />
		<input type="radio" name="RES" value="r3" /> Mainland China<br />
		<input type="radio" name="RES" value="r4" /> Punjab Grill<br />
		<input type="radio" name="RES" value="r5" /> Onesta<br />
		<input type="radio" name="RES" value="r6" /> Truffles<br />
		<input type="radio" name="RES" value="r6" /> Sahib Sindh Sultan<br />
		<input type="radio" name="RES" value="r6" /> Napoli<br />
		<input type="radio" name="RES" value="r6" /> Bhatinda Junction<br />
		<input type="radio" name="RES" value="r6" /> Meghanas<br />
		<input type="radio" name="RES" value="r6" /> California Pizza Kitchen<br />
		<input type="radio" name="RES" value="r6" /> Greasy Spoon<br />
		<input type="submit" value="Submit Restaurant">
		</p></h1>
	</form>
	</div>
	</div>
</div>	


</body>
</html>



			"""
conn.commit()
