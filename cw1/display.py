from flask import Blueprint, render_template
from models import Total, Module
import datetime
import time

# Here, for administrative purposes, I've placed all the back-end code for the display page under the display blueprint
bp = Blueprint("display", __name__, url_prefix="/display")


# The page which display all assessments.
@bp.route('/display')
def display():
    total = Total.query.all()
    return render_template("display.html", total=total)


# The page which display all modules.
@bp.route('/all_module')
def all_module():
    module = Module.query.all()
    return render_template("module.html", module=module)


# The page display all assessments which under the "XJC02011" module.
@bp.route('/module_web')
def module_web():
    module_web = []
    module_w = Total.query.all()
    for i in module_w:
        if i.module_id == "XJCO2011":
            module_web.append(i)
        else:
            continue
    return render_template("module_web.html", module_web=module_web)


# The page display all assessments which under the "XJC02211" module.
@bp.route('/module_os')
def module_os():
    module_os = []
    module_o = Total.query.all()
    for i in module_o:
        if i.module_id == "XJCO2211":
            module_os.append(i)
        else:
            continue
    return render_template("module_os.html", module_os=module_os)


# The page display all assessments which under the "XJC02321" module.
@bp.route('/module_flfa')
def module_flfa():
    module_flfa = []
    module_f = Total.query.all()
    for i in module_f:
        if i.module_id == "XJCO2321":
            module_flfa.append(i)
        else:
            continue
    return render_template("module_flfa.html", module_flfa=module_flfa)


# The page display all assessments which under the "XJC02411" module.
@bp.route('/module_nc')
def module_nc():
    module_nc = []
    module_n = Total.query.all()
    for i in module_n:
        if i.module_id == "XJCO2421":
            module_nc.append(i)
        else:
            continue
    return render_template("module_nc.html", module_nc=module_nc)


# The page display all assessments which under the "XJC02711" module.
@bp.route('/module_adi')
def module_adi():
    module_adi = []
    module_a = Total.query.all()
    for i in module_a:
        if i.module_id == "XJCO2711":
            module_adi.append(i)
        else:
            continue
    return render_template("module_adi.html", module_adi=module_adi)


# The page display all assessments which has been finished.
@bp.route('/finish')
def finish():
    finish = []
    f = Total.query.all()
    for i in f:
        if i.finish == "True":
            finish.append(i)
        else:
            continue
    return render_template("finish.html", finish=finish)


# The page display all assessments which has not been finished.
@bp.route('/unfinish')
def unfinish():
    unfinish = []
    uf = Total.query.all()
    for i in uf:
        if i.finish == "False":
            unfinish.append(i)
        else:
            continue
    return render_template("unfinish.html", unfinish=unfinish)


# The page display all assessments which has closed to the ddl.
@bp.route('/ddl')
def ddl():
    ddl = []
    today = time.localtime(time.time())
    t = datetime.datetime(today[0], today[1], today[2])
    d = Total.query.all()
    for i in d:
        dd1 = time.strptime(str(i.ddl), "%Y-%m-%d")
        dd = datetime.datetime(dd1[0], dd1[1], dd1[2])
        if (dd-t).days <= 3 and (dd-t).days >= 0:
            ddl.append(i)
        else:
            continue
    return render_template("ddl.html", ddl=ddl)
#
