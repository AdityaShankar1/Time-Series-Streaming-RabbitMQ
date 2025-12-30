from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded login credentials
USERNAME = "admin"
PASSWORD = "opensesame"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            return redirect(url_for("report"))
        else:
            return "<h3 style='color:red; text-align:center;'>❌ Invalid credentials. Try again.</h3>"
    return '''
    <body style="background-image: url('/static/andrey-metelev-powergrid-unsplash.jpg');
                 background-size: cover;
                 background-repeat: no-repeat;
                 background-attachment: fixed;
                 font-family: Arial;">
    <center>
        <h2 style="color:white; background-color:rgba(0,0,0,0.5); padding:10px; border-radius:8px;">
            🔒 Energy Dashboard Login
        </h2>
        <form method="post">
            <table border="1" bgcolor="#ffffff" cellpadding="12" cellspacing="0"
                   style="border-radius:10px; opacity:0.9;">
                <tr>
                    <td align="right"><b>Username:</b></td>
                    <td><input type="text" name="username" style="width:200px; padding:5px;"></td>
                </tr>
                <tr>
                    <td align="right"><b>Password:</b></td>
                    <td><input type="password" name="password" style="width:200px; padding:5px;"></td>
                </tr>
                <tr>
                    <td colspan="2" align="center">
                        <input type="submit" value="Login"
                               style="background-color:navy; color:white; padding:8px 16px;
                                      border:none; border-radius:5px;">
                    </td>
                </tr>
            </table>
        </form>
        <p style="color:white; background-color:rgba(0,0,0,0.5); padding:5px; border-radius:5px;">
            Enter <b>admin</b> / <b>opensesame</b> to access the report
        </p>
    </center>
    </body>
    '''

@app.route("/report")
def report():
    return render_template("report.html")

if __name__ == "__main__":
    app.run(debug=True)