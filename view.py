from flask import Blueprint, render_template
from database import get_connection

view_bp = Blueprint('view', __name__)

@view_bp.route('/view')
def view_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view.html', users=students)

