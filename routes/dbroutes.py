from config import app,db
from flask import jsonify,request,abort
from models import DbPerson

@app.route("/dbpeople")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)


@app.route("/dbpeople",methods=['POST'])
def processDepartments():
    try:      
      input=request.get_json()
       sno=input['sno']
       name=input['city']
       db.session.add(Dbperson(sno,name,city))
       db.session.commit()
       return {"status": "success"},201
    expect:
       abort({'status':"internal server error"},500)