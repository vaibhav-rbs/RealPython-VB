from views import db
from models import Task
from datetime import date

db.create_all()


#db.session.add(Task("Finish this tutorial", str(date(2017,1,24)), 10,1))
#db.session.add(Task("Finish this book", str(date(2017,2,9)), 10,1))

db.session.commit()
