from flask import Blueprint, request, render_template, redirect
from database import get_connection

edit_update_bp = Blueprint('edit_update', __name__)

@edit_update_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cursor.execute("UPDATE student SET name=%s, email=%s, password=%s WHERE id=%s",
                       (name, email, password, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/view')

    cursor.execute("SELECT * FROM student WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', user=user)

