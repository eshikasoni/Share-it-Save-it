#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
if form.getvalue('RES'):
   restaurant = form.getvalue('RES')
else:
   restaurant = "Not set"
if restaurant == 'r4':
	print "Content-type: text/html"
	print """
			<html>
<head>
<title>
Menu 1
</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="style2.css" type="text/css" />

<body>

<div id="facebook-Bar">

  <div id="facebook-Frame">

    <div id="logo"> <img src="/images/logo.jpg"> </div>
    
    </div>
 </div>
 
 <div class="loginbox radius">

  <h2 style="color:#141823; text-align:center;"><font face="Verdana">Whats your order today?</font></h2>

  <div class="loginboxinner radius">

    <div class="loginheader">


    </div>

   <div class="loginform">

      <form id="login" action="time.cgi" method="post">
         <p><h1>
		<input type="radio" name="MENU" value="m1" /> Dal Makhani and Naan<br />
		<input type="radio" name="MENU" value="m2" /> Kadai Paneer and Naan<br />
		<input type="radio" name="MENU" value="m3" /> Palak Paneer and Roti<br />
		<input type="radio" name="MENU" value="m4" /> Chicken Malai and Roti<br />
		<input type="radio" name="MENU" value="m5" /> Mutton Rogan and Rice<br />
		<input type="radio" name="MENU" value="m6" /> Fish Curry and Rice<br />
		<input type="radio" name="MENU" value="m7" /> Paneer Pasanda and Roti<br />
			
		<input type="submit" value="Submit your Order"/>
		</p></h1>
	</form>
	</div>
	</div>
</div>	


</body>
</html>
print """

if restaurant == 'r3':
	print "Content-type: text/html"
	print """
<html>
<head>
<title>
Menu 2
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

  <h2 style="color:#141823; text-align:center;"><font face="Verdana">Whats your order today?</font></h2>

  <div class="loginboxinner radius">

    <div class="loginheader">


    </div>

   <div class="loginform">

      <form id="login" action="time.cgi" method="post">
         <p><h1>
		<input type="radio" name="MENU" value="m1" /> Manchurian and Fried Rice<br />
		<input type="radio" name="MENU" value="m2" /> Dim Sum and Fried Rice<br />
		<input type="radio" name="MENU" value="m3" /> Veg Wonton and Hakka Noodles<br />
		<input type="radio" name="MENU" value="m4" /> Chicken Manchurian Noodles<br />
		<input type="radio" name="MENU" value="m5" /> Chicken Chopsuey<br />
		<input type="radio" name="MENU" value="m6" /> Fish and Hakka Noodles<br />
		<input type="radio" name="MENU" value="m7" /> Thai Noodles<br />
		<input type="submit" value="Submit your Order" onclick="location.href='file:///Users/eshikasoni/Desktop/u25/time.html';" />
	
		</p></h1>
	</form>
	</div>
	</div>
</div>	


</body>
</html>
"""


