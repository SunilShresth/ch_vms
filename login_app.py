from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.utils import secure_filename
import sorting

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

def insertBLOB(photo, signature, first_name, last_name, email, phone, org, purpose, visited_department, ch_personnel):
    print("Inserting BLOB into python_employee table")
    try:
        # connection = mysql.connector.connect(host='localhost', database='VMS', user='vms_user', password='Hell0w0rld')
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO visitorinfo
                          (photo, signature, firstname, lastname, emailid, phone, organization, purpose, sent_department, ch_personnel, checkin, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        # bin_photo = convertToBinaryData(photo)
        checkin = datetime.now()
        status = True

        # Convert data into tuple format
        insert_blob_tuple = (photo, signature, first_name, last_name, email, phone, org, purpose, visited_department, ch_personnel, checkin, status)
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
    try:
        connection = mysql.connector.connect(**db_conf_dict)
        cursor = connection.cursor()
        select_record_query = "select organization from visitorinfo"
        cursor.execute(select_record_query)
        record_list = cursor.fetchall()
        company_list = []
        for record in record_list:
            if record[0] not in company_list:
                company_list.append(record[0])
        print(company_list)

    except mysql.connector.Error as error:
        print("Failed to select from visitorinfo table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return render_template('registration_form.html', suggestions=company_list)


# Uploading directory path set up
# photo_upload_path = os.path.abspath("../vms_webapp/static/photo/")
# signature_upload_path = os.path.abspath("../vms_webapp/static/signature/")

# saving visitor detail form data to database and uploading photo and signature to static folder
@app.route('/visitordetail', methods=['POST', 'GET'])
def visitor_detail():
    photo_img = request.files['photo']
    signature_img = request.files['signature']
    # photo = img_file.read()
    # photo_path = os.path.join('static/photo', secure_filename(img_file.filename))
    photo_path = "static/photo/" + secure_filename(photo_img.filename)
    signature_path = "static/signature/" + secure_filename(signature_img.filename)
    photo_img.save(photo_path)
    signature_img.save(signature_path)
    
    # to make suite the path in production server

    # photo_upload_path = "/var/www/vms_webapp/static/photo/" + secure_filename(photo_img.filename)
    # signature_upload_path = "/var/www/vms_webapp/static/signature/" + secure_filename(signature_img.filename)
    # photo_path = "static/photo/" + secure_filename(photo_img.filename)
    # signature_path = "static/signature/" + secure_filename(signature_img.filename)
    # photo_img.save(photo_upload_path)
    # signature_img.save(signature_upload_path)

    # print(photo_path)
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    # print(first_name)
    email = request.form['email']
    purpose = request.form['purpose']
    phone = request.form['phone']
    org = request.form['company']
    department = request.form['visited_depart']
    ch_personnel = request.form['ch_personnel']
    insertBLOB(photo_path, signature_path, first_name, last_name, email, phone, org, purpose, department, ch_personnel)
    return redirect('/pendingoutlist')


@app.route('/recordlist', methods=['GET','POST'])
def record_list():
    record_list =  sorting.get_record_list()
    if request.method == "POST":
        parameter = request.form['sort_parameter']
        parameter_index = sorting.get_sort_parameter_index(parameter)
        sorted_list = sorting.get_sorted_record(record_list, parameter_index)
        return render_template('record_list.html', data=sorted_list, selected_option=parameter)

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
        select_individual_detail = "select id, photo, firstname, lastname, emailid, phone, organization, sent_department, purpose, checkin, signature from visitorinfo where id="+visitor_id
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
        select_individual_detail = "select id, photo, firstname, lastname, emailid, phone, organization, sent_department, purpose, checkin, signature from visitorinfo where id="+visitor_id
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
        select_individual_detail = "select photo, firstname, lastname, emailid, phone, organization, sent_department, purpose, ch_personnel from visitorinfo where id="+visitor_id
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

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_results = []
    if request.method == "POST":
        try:
            search_string = request.form['search']
            connection = mysql.connector.connect(**db_conf_dict)
            cursor = connection.cursor()
            search_query = '''select id, firstname, lastname, emailid, organization, sent_department, purpose,ch_personnel, checkin, checkout from visitorinfo where firstname = "%s"''' %search_string
            cursor.execute(search_query)
            search_results = cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to select from visitorinfo table {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    return render_template('search.html', data = search_results)

@app.route('/updatecheckin', methods=['POST', 'GET'])
def update_visitor_checkin():
    photo_path = request.form['photo']
    print(photo_path)
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    print(first_name)
    email = request.form['email']
    purpose = request.form['purpose']
    phone = request.form['phone']
    org = request.form['company']
    department = request.form['visited_depart']
    ch_personnel = request.form['ch_personnel']
    insertBLOB(photo_path, first_name, last_name, email, phone, org, purpose, department, ch_personnel)
    return redirect('/pendingoutlist')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)