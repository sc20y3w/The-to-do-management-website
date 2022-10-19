from flask import Blueprint, render_template, request, url_for, redirect
from models import Total
from exts import db
from .forms import AddForm
from sqlalchemy import or_

bp = Blueprint("operation", __name__, url_prefix="/operation")


# Display the operation page.
@bp.route('/ope')
def operation():
    return render_template("operation.html")


# Display the add page.
@bp.route('/add')
def add():
    return render_template("add.html")


# Add the assessment
@bp.route('/add_assessment', methods=['GET', 'POST'])
def add_assessment():
    # Check whether its method is "get" or "post"
    if request.method == 'POST':
        form = AddForm(request.form)
        # Check whether it pass the validator
        if form.validate():
            title = form.title.data
            description = form.description.data
            ddl = form.ddl.data
            finish = form.finish.data
            module_id = form.module_id.data
            assessment = Total(title=title, description=description, ddl=ddl, finish=finish, module_id=module_id)
            db.session.add(assessment)
            db.session.commit()
            return redirect(url_for("display.display"))
        else:
            return redirect(url_for("operation.add_assessment"))
    else:
        return render_template("add.html")


# Display the mark page.
@bp.route('/mark')
def mark():
    total = Total.query.all()
    return render_template("mark.html", total=total)


# Display the delete page.
@bp.route('/delete')
def delete():
    total = Total.query.all()
    return render_template("delete.html", total=total)


# Execute the operation of deleting.
@bp.route('/delete_assessment/<int:id>')
def delete_assessment(id):
    total = Total.query.filter_by(id=id)[0]
    db.session.delete(total)
    db.session.commit()
    return redirect(url_for('operation.delete'))


# Execute the operation of marking.
@bp.route('/search_mark/<int:id>')
def search_mark(id):
    total = Total.query.filter_by(id=id)[0]
    if total.finish == "True":
        total.finish = "False"
    else:
        total.finish = "True"
    db.session.commit()
    return redirect(url_for('operation.mark'))


# Execute the operation of searching.(which in the top left corner of the page)
@bp.route('/search')
def search():
    search = request.args.get("search")
    total = Total.query.filter(or_(Total.title.contains(search),
                                   Total.description.contains(search),
                                   Total.ddl.contains(search),
                                   Total.finish.contains(search),
                                   Total.module_id.contains(search)))
    return render_template('display.html', total=total)
