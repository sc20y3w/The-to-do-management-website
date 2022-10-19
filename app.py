from flask import Flask, render_template
from models import Total, Module

# It was written because without it, the application would jump again and again
# between form and models.py and app.py.
from exts import db

import config
from cw1.operation import bp as operation_bp
from cw1.display import bp as display_bp
from flask_migrate import Migrate


# Some blueprint.
app = Flask(__name__)
app.register_blueprint(operation_bp)
app.register_blueprint(display_bp)
app.config.from_object(config)
# Secret key
app.config['SECRET_KEY'] = "123456"
# Bind the app to bd
db.init_app(app)


migrate = Migrate(app, db)


@app.route("/total")
def total_view():
    # Add data
    total = Total(title="assessment", description="DO IT NOW", ddl="2022-11-06", finish="False", module_id="XJCO2011")
    db.session.add(total)
    # submit operation
    db.session.commit()
    return "Add successful"


# Test whether you can successfully connect and add information to the database table.
@app.route("/total_test_otm")
def otm():
    assessment1 = Total(title="assessment1", description="DO IT NOW", ddl="2022-11-06", finish="False")
    assessment2 = Total(title="assessment2", description="222", ddl="2022-11-07", finish="False")
    assessment3 = Total(title="assessment3", description="333", ddl="2022-11-08", finish="True")
    assessment4 = Total(title="assessment4", description="777", ddl="2022-11-12", finish="True")
    assessment5 = Total(title="assessment5", description="888", ddl="2022-11-13", finish="False")
    assessment6 = Total(title="assessment6", description="999", ddl="2022-11-14", finish="True")
    module1 = Module(id="XJCO2011", module_name="Web")
    module2 = Module(id="XJCO2211", module_name="Web")
    module3 = Module(id="XJCO2321", module_name="Web")
    module4 = Module(id="XJCO2421", module_name="Web")
    module5 = Module(id="XJCO2711", module_name="Web")
    assessment1.module = module1
    assessment2.module = module2
    assessment3.module = module3
    assessment4.module = module4
    assessment5.module = module5
    assessment6.module = module1
    db.session.add(assessment1)
    db.session.add(assessment2)
    db.session.add(assessment3)
    db.session.add(assessment4)
    db.session.add(assessment5)
    db.session.add(assessment6)
    db.session.commit()
    return "Add successful"


# Displaying the help page.(The following is the code to show the page, here will not go to comment one by one.)
@app.route('/dis')
def dis():
    return render_template("help.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/reference")
def reference():
    return render_template("reference.html")


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


# Run! Run! Run!
if __name__ == '__main__':
    app.run()
