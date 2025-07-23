from flask import Flask
from insert import insert_bp
from view import view_bp
from delete import delete_bp
from edit_update import edit_update_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(insert_bp)
app.register_blueprint(view_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(edit_update_bp)

if __name__ == '__main__':
    app.run(debug=True)

