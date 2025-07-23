from flask import Blueprint, redirect
from database import get_connection

delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/view')
