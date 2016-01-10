#!/usr/bin/env python
print "Content-Type: text/html"

print """

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<title>Share It Save It</title>

<link rel="stylesheet" href="style1.css" type="text/css" />

</head>
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

              <td ><input type="password" tabindex="2" id="pass"  name="pass" class="inputtext radius1" ></td>

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

<!-- header ends here -->

<div class="loginbox radius">

  <h2 style="color:#141823; text-align:center;"><font face="Verdana">SHARE IT SAVE IT</font></h2>

  <div class="loginboxinner radius">

    <div class="loginheader">

      <h4 class="title">Connect with people around you to share your bill.</h4>

    </div>

    <!--loginheader-->

    <div class="loginform">

      <form id="login" action="account_creation.cgi" method="post">

        <p>

          <input required ="true" type="text" id="firstname" name="firstname"  placeholder="First Name" required value="" class="radius mini"  />

          <input type="text" id="lastname" name="lastname" placeholder="Last Name" value="" class="radius mini" />

        </p>
         <p>

          <input type="tel" id="contact no" name="contact no" placeholder="Your Number" value="" class="radius" />

        </p>

        <p>

          <input type="text" id="email" name="email" placeholder="Your Email" value="" class="radius" />

        </p>

        <p>

          <input type="text" id="remail" name="remail" placeholder="Re-enter Email" class="radius" />

        </p>

        <p>

          <input type="password" id="password" name="password" placeholder="New Password" class="radius" />

        </p>

        <p>

          <button class="radius title" name="signup">Sign Up </button>

        </p>

    </form>

    </div>

    <!--loginform-->
  </div>

  <!--loginboxinner-->

</div>

<!--loginbox-->
</body>
</html>
"""
