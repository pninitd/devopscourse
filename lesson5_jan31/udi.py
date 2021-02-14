import json

import pymysql
from flask import Flask
app = Flask(__name__)
conn = pymysql.connect(host='remotemysql.com', port=3306, user='jC9okm9Ppe', passwd='LBIGnhlfpI', db='jC9okm9Ppe')
cursor = conn.cursor()


@app.route('/dogs')
def dogs():
    cursor.execute("SELECT * FROM jC9okm9Ppe.dogs;")
    data = cursor.fetchall()
    results = json.dumps(data, indent=2)
    # return '<H1 id=1>' + results + '</H1>', 200
    return"< ul > { %for row in cursor %}" \
    "< li > {{row}} < / li >" \
    "{ % endfor %}", 200

# <tr>
#     {% for row in cursor %}
#        <td>{{row[0]}}</td>
#        <td>{{row[1]}}</td>
#        <td>{{row[2]}}</td>
#     {% endfor %}
# </tr>

#from Maher:
# cursor.execute("SELECT * FROM {}".format(db_table))
# returnval = "<h2>All Dogs in our DB</h2>"
# for row in cursor:
#     returnval += "<p><b>Dog Name:</b> {},   <b>Age:</b> {},   <b>Breed:</b> {}</p>".format(row[0], row[1], row[2])
# return returnval, 200

app.run(host='127.0.0.1', debug=True, port=5000)


# from flask import render_template
# yeah it's basically return render_template("my_template.html")
# you can pass more arguments which are referenced inside the template like
# return render_template("my_template.html", title="Sign In", form=my_form)
# so if u have an object called form in the template, the renderer knows how to process it and create webforms