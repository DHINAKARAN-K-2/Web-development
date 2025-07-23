import os
from flask import Blueprint, request, redirect, render_template
from database import get_connection
from werkzeug.utils import secure_filename
import mysql.connector

insert_bp = Blueprint('insert', __name__)
UPLOAD_FOLDER = 'static/uploads'

@insert_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        image = request.files['image']
        filename = None
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(UPLOAD_FOLDER, filename))
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student (name, email, password,image) VALUES (%s, %s, %s,%s)", 
                       (name, email, password,filename))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/view')
    return render_template('register.html')
