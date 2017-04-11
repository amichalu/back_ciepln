""" Tests of models """
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from models import Document

ENGINE = create_engine("mysql+pymysql://venice:pass1@localhost/venice?charset=utf8")
SES = sessionmaker(bind=ENGINE)()
#SES = SESS()

for row in SES.query(Document).order_by(desc('number')).limit(10):
    #s = unicode(your_object).encode('utf8')
    # print repr(row).encode('utf-8')
    print repr(row)
