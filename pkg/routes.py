from flask import render_template, abort, flash, request,redirect, make_response, session
from pkg import app
from pkg import db
from pkg.models import Announced_pu_results,Announced_ward_results,Announced_lga_results,Announced_state_results,Party,States,Lga,Ward,Polling_unit


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/solution1/",methods=['GET'])
def pu_8():
    # my polling unit of choice is Sapele ward 8
    record = db.session.query(Announced_pu_results).filter(Announced_pu_results.polling_unit_uniqueid==8).all()
    return render_template('solution1.html',record=record)


@app.route('/solution2')
def sum_total():
    lgas=db.session.query(Lga).all()
    return render_template('solution2.html',lgas=lgas)
   
@app.route('/check',methods=['POST','GET'])
def check():
    if request.method == "GET":
        return render_template('solution2.html')
    else:
        lga_idd=request.form.get('lga')
        sql=f"select * from announced_pu_results join polling_unit on announced_pu_results.polling_unit_uniqueid=polling_unit.uniqueid where polling_unit.lga_id={lga_idd}"
        record=db.session.execute(sql)
        details=record.fetchall()
        return render_template('solution2.html',details=details)
    
       