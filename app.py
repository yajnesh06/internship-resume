from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
db = SQLAlchemy()


@app.route("/")
def hello_world():
    return render_template('index.html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/resume'
# # initialize the app with the extension
db.init_app(app)
 

class Resume_data(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
     
    
@app.route("/registration", methods=['GET','POST'])
           
def registration():
    if(request.method=='POST'):
        '''Add entry to the database'''
        
        email = request.form.get('email')
        
        entry = Resume_data(email = email)
        db.session.add(entry)
        db.session.commit()
        e=Resume_data.query.all()
        print(e)
        
    return render_template('index2.html')



    

if __name__=="__main__":
    app.run(debug=True)