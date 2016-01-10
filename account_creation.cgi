#!/usr/bin/env python
import cgi
import pymysql  
form = cgi.FieldStorage() 
contact = form.getvalue('contact no')
first_name= form.getvalue('firstname')
last_name= form.getvalue('lastname')
email = form.getvalue('email')
remail = form.getvalue('remail')
password = form.getvalue('password')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()
'''
if contact == "" or first_name == "" or last_name == "" or email == "" or remail=="" or password == "":
	print "Content-type: text/html"
	print "<h2> Error </h2>"
if contact == "" and first_name == "" and last_name == "" and email == "" and remail=="" and password == "":
	print "Content-type: text/html"
	print "<h2> Error </h2>"
'''
if email == remail:
	print "Content-type: text/html"
	print """ 

	<h2>Welcome to Share it,Save it</h2>


	Your account has been successfully created



	Please login with your username and password 
	"""
	cur.execute("""insert into users(firstname,lastname,email,remail,password,contact)
				values(%s,%s,%s,%s,%s,%s)""",(first_name,last_name,email,remail,password,contact))
	print """
	<body class="login">

<!-- header starts here -->

<div id="facebook-Bar">

  <div id="facebook-Frame">

    <div id="logo"> <img src="/images/logo.jpg"> </div>

    <div id="header-main-right">

    <div id="header-main-right-nav">

        <form method="post" action="login_form.cgi" id="login_form" name="login_form">

          <table border="0" style="border:none">

            <tr>

              <td ><input type="text" tabindex="1"  id="email" placeholder="Email or Phone" name="email" class="inputtext radius1" value=""></td>

              <td ><input type="password" tabindex="2" id="pass" placeholder="Password" name="pass" class="inputtext radius1" ></td>

              <td ><input type="submit" class="fbbutton" name="login" value="Login" /></td>

            </tr>

            <tr>

              <td><label>

                  <input id="persist_box" type="checkbox" name="persistent" value="1" checked="1"/>

                  <span style="color:#ccc;">Keep me logged in</span></label></td>

              <td><label><a href="" style="color:#ccc; text-decoration:none">forgot your password?</a></label></td>

            </tr>

          </table>

        </form>

      </div>

    </div>

  </div>

</div>
"""

else:
	print "Content-type: text/html"
	print """

	You have entered two different mail id's
	"""
conn.commit()

