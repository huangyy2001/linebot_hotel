from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://admin:123456@127.0.0.1:5432/hotel'
db = SQLAlchemy(app)

@app.route('/')
def index():
    sql = """
    CREATE TABLE formuser(
    id serial Not NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
    
    CREATE TABLE hoteluser(
    id serial Not NULL,
    uid character varying(50) NOT NULL,
    PRIMARY KEY (id));
    
    CREATE TABLE booking(
    id serial Not NULL,
    bid character varying(50) NOT NULL,
    roomtype character varying(50) NOT NULL,
    roomamount character varying(5) NOT NULL,
    datein character varying(20) NOT NULL,
    dateout character varying(20) NOT NULL,
    PRIMARY KEY (id));
    """
    db.engine.execute(sql)
    return "資料表建立成功 !"

if __name__ =='__main__':
    app.run(debug=True,use_reloader=False)

