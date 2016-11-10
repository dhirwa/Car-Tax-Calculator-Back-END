from app import *
from app.model.model import *
from app.model.schema import *
from sqlalchemy import func
from flask import jsonify
from app.controllers.car_contr import *

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404: Page not found, Please check ur route well.'


@app.route('/getcars')
def get_prov():
    provs=Cars.query.all()
    result=crs_schema.dump(provs)
    return jsonify({'Cars':result.data})

@app.route('/getcars/brand/<br>')
def get_cb(br):
    provs=Cars.query.filter_by(cr_brand=br).all()
    if provs :
        result=crs_schema.dump(provs)
        return jsonify({'Message':'1','Cars':result.data})
    else:
        return jsonify({'Message':'0'})

@app.route('/getcars/year/<int:yr>')
def get_cy(yr):
    provs=Cars.query.filter_by(cr_year=yr).all()
    if provs :
        result=crs_schema.dump(provs)
        return jsonify({'Message':'1','Cars':result.data})
    else:
        return jsonify({'Message':'0'})

@app.route('/getcars/brand/mark/year/<br>/<mrk>/<int:yr>')
def cby(br,mrk,yr):
    c=Cars.query.filter_by(cr_brand=br).filter_by(cr_mark=mrk).filter_by(cr_year=yr).all()
    if c:
        result=crs_schema.dump(c)
        return jsonify({'Message':'1','Cars':result.data})
    else:
        return jsonify({'Message':'0'})

@app.route('/getcars/getamount/<br>/<mrk>/<int:yr>/<tr>/<wt>')
def cam(br,mrk,yr,tr,wt):
    c=Cars.query.filter_by(cr_brand=br).filter_by(cr_mark=mrk).filter_by(cr_year=yr).first()
    if c:
        json_data = cr_schema.dump(c).data
        part= get_car(json_data,tr,wt);
        return jsonify(part)
    else:
        return jsonify({'Message':'0'})
