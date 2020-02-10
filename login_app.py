from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug import secure_filename

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import mysql.connector
from mysql.connector import Error

db_conf_dict = {'host':'localhost', 'database':'VMS', 'user':'vms_user', 'password':'Hell0w0rld!', 'auth_plugin':'mysql_native_password'}

# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData

def insertBLOB(photo, first_name, last_name, email, phone, org, purpose, visited_department):
    print("Inserting BLOB into python_employee table")
    try:
        # connection = mysql.connector.connect(host='localhost', database='VMS', user='vms_user', password='Hell0w0rld')
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO visitorinfo
                          (photo, firstname, lastname, emailid, phone, organization, purpose, sent_department, checkin, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        # bin_photo = convertToBinaryData(photo)
        checkin = datetime.now()
        status = True

        # Convert data into tuple format
        insert_blob_tuple = (photo, first_name, last_name, email, phone, org, purpose, visited_department, checkin, status)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     if request.form['password'] == 'password' and request.form['username'] == 'admin':
#         session['logged_in'] = True
#     else:
#         flash('wrong password!')
#         return home()


@app.route('/visitorhome', methods=['POST', 'GET'])
def visitor_home():
    return render_template('index.html')


# Visitor detail form to fillup when new visitor comes in
@app.route('/visitorform', methods=['POST', 'GET'])
def visitor_form():
    return render_template('registration_form.html')


# Uploading directory path set up
# photo_upload_path = os.path.abspath("../vms_webapp/static/photo/")
# signature_upload_path = os.path.abspath("../vms_webapp/static/signature/")

# saving visitor detail form data to database and uploading photo and signature to static folder
@app.route('/visitordetail', methods=['POST', 'GET'])
def visitor_detail():
    img_file = request.files['photo']
    # photo = img_file.read()
    photo_path = os.path.join('static/photo', secure_filename(img_file.filename))
    img_file.save(photo_path)
    print(photo_path)
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    print(first_name)
    email = request.form['email']
    purpose = request.form['purpose']
    phone = request.form['phone']
    org = request.form['company']
    department = request.form['visited_depart']
    insertBLOB(photo_path, first_name, last_name, email, phone, org, purpose, department)
    return redirect('/pendingoutlist')


@app.route('/recordlist', methods=['GET'])
def record_list():
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_record_query = "select id, firstname, lastname, emailid, organization, sent_department, purpose, checkin, checkout from visitorinfo"
        cursor.execute(select_record_query)
        record_list = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('record_list.html', data=record_list)

@app.route('/pendingoutlist', methods=['GET'])
def pending_list():
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_pending_query = "select id, firstname, lastname, emailid, organization, sent_department, checkin from visitorinfo where status=1"
        cursor.execute(select_pending_query)
        pending_records = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('pending_list.html', data=pending_records)

@app.route('/checkout/<string:visitor_id>', methods=['GET','POST'])
def checkout(visitor_id):
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        # , checkout="+str(datetime.now())+
        checkout = datetime.now()
        update_pending_tuple = (checkout, visitor_id)
        update_pending_query = "update visitorinfo set status=0, checkout=%s where id=%s"
        cursor.execute(update_pending_query, update_pending_tuple)

    except mysql.connector.Error as error:
        print("Failed to update pending visitor {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return redirect("/pendingoutlist")


@app.route('/individualdetail/<string:visitor_id>', methods=['GET', 'POST'])
def individual_detail(visitor_id):
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_individual_detail = "select id, photo, firstname, lastname, emailid, phone, organization, sent_department, purpose, checkin from visitorinfo where id="+visitor_id
        cursor.execute(select_individual_detail)
        individual_detail_data = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('individual_detail.html', data=individual_detail_data[0])


@app.route('/visitorlogdetail/<string:visitor_id>', methods=['GET', 'POST'])
def visitor_log_detail(visitor_id):
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_individual_detail = "select id, photo, firstname, lastname, emailid, phone, organization, sent_department, purpose, checkin from visitorinfo where id="+visitor_id
        cursor.execute(select_individual_detail)
        individual_detail_data = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('visitor_detail.html', data=individual_detail_data[0])

@app.route('/updatevisit/<string:visitor_id>', methods=['GET', 'POST'])
def update_registration(visitor_id):
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_individual_detail = "select photo, firstname, lastname, emailid, phone, organization, sent_department, purpose from visitorinfo where id="+visitor_id
        cursor.execute(select_individual_detail)
        individual_detail_data = cursor.fetchall()

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return render_template('update_registration.html', data=individual_detail_data[0])

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)