from markupsafe import escape
from flask import Flask, abort, render_template, request, jsonify 
import logging as logger
import controller

logger.basicConfig(level="DEBUG")


app = Flask(__name__)

@app.route('/')
def indexx():
    return "Index Page!"

@app.route('/test')
def hello():
    return "Index Page Test!"

@app.route('/capitalize/<words>/')
def capitalize(words):
    return '<h1>{}</h1>'.format(escape(words.capitalize()))

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam1']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)

@app.route('/add_entry')
def add_entry():
    return render_template('add_entry.html')

@app.route('/add_entry', methods=["POST"])
def add_entry_post():
    id = request.form.get('employee_id')
    name = request.form.get('employee_name')
    city = request.form.get('emp_city')
    age = request.form.get('emp_age')
    response = controller.add_employee(id, name, city, age)   
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Add Employee successful',
            'response': response
        }
    return { 
        'msg': 'error occurred',
        'response': response
    }

@app.route('/list_tables')
def list_tables():
    response = controller.list_tables()   
    
    return {
        'msg': 'Add Employee successful',
        'response': response
    }

@app.route('/get_emp')
def get_emp():
    return render_template('get_entry.html')
    

@app.route('/get_emp', methods=["POST"])
def get_emp_post():
    try:
        id = request.form.get('employee_id')
        response = controller.get_employee(id) 
        if response:
           return render_template('employee_table.html',
                           response=response)
        else:
            return {
                'msg': 'No Record Found'
            }
    except Exception:
        return jsonify("Exception Found") 
    # return {
    #     'msg': 'Search Employee successful',
    #     'response': response
    # }

# @app.route('/get_emp', methods=["POST"])
# def get_emp_post():
#     id = request.form.get('employee_id')
#     response = controller.get_employee(id)   
    
#     return {
#         'msg': 'Search Employee successful',
#         'response': response
#     }

if __name__ == "__main__":
    logger.debug("Starting application")
    app.run(host="0.0.0.0", port=5100, debug=True,use_reloader=True)