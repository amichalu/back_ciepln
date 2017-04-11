""" Models definition """
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DECIMAL

BASE = declarative_base()

class Document(BASE):
    """ Document mapping """
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    number = Column(String)
    type = Column(Integer)
    date = Column(Date)
    sellername1 = Column(String)

    custname1 = Column(String)
    custname2 = Column(String)
    custnip = Column(String)
    custaddress1 = Column(String)
    custaddress2 = Column(String)
    custaccnmb = Column(String)
    location = Column(String)

    brutto = Column(DECIMAL(14, 3))
    netto = Column(DECIMAL(14, 3))
    excise = Column(DECIMAL(14, 3))

    currency_id = Column(Integer, ForeignKey('currency.id'))
    currency = relationship("Currency", lazy='joined')

    paymethod_id = Column(Integer, ForeignKey('paymethod.id'))
    paymethod = relationship("Paymethod", lazy='joined')

    period_id = Column(Integer, ForeignKey('period.id'))
    period = relationship("Period", lazy='joined')

    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship("Subject", lazy='joined')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id':self.id,
            'number' : self.number,
            'type' : self.type,
            'date' : self.date.strftime("%Y-%m-%d"),
            'sellername1' : self.sellername1,
            'currency_label' : self.currency.label,
            'paymethod_name' : self.paymethod.name,
            'period_startdate' : self.period.startdate.strftime("%Y-%m-%d") if self.period.startdate != None else '',
            'period_enddate' : self.period.enddate.strftime("%Y-%m-%d") if self.period.enddate != None else '',
            'custnip': self.custnip,
            'custname1': self.custname1,
            'custname2': self.custname2,
            'brutto' : self.brutto.to_eng_string(),
            'netto' : self.netto.to_eng_string(),
            'excise' : self.excise.to_eng_string(),
            'custaddress1' : self.custaddress1,
            'custaddress2' : self.custaddress2,
            'custaccnmb' : self.custaccnmb,
            'subject_name' : self.subject.name,
            'location' : self.location
        }

    def __repr__(self):
        return "<Document id:{}, number:{}, date:{}, brutto: {}>".format(self.id, self.number, self.date, self.brutto)

class Currency(BASE):
    """ Currency mapping """
    __tablename__ = "currency"

    label = Column(String)
    created_at = Column(String)
    updated_at = Column(String)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Currency (id: {}, label: {}>".format(self.id, self.label)

class Paymethod(BASE):
    """ Paymethod mapping """
    __tablename__ = "paymethod"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    def __repr__(self):
        return "<Paymethod (id: {}, name: {}>".format(self.id, self.label)

class Customer(BASE):
    """ Customer mapping """
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name1 = Column(String)
    name2 = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    nip = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    def __repr__(self):
        return "<Customer (id: {}, name1: {}, nip: {}>".format(self.id, self.name1, self.nip)
    
class Subject(BASE):
    """ Subject mapping """
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(String)
    updated_at = Column(String)

    def __repr__(self):
        return "<Subject (id: {}, name: {}>".format(self.id, self.name)

class Period(BASE):
    """ Period """
    __tablename__ = "period"

    id = Column(Integer, primary_key=True)
    startdate = Column(Date)
    enddate = Column(Date)
    last = Column(Integer)
    active = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)

    def __repr__(self):
        return "<Period (id: {}, startdate: {}, enddate: {}, last: {}, active: {}>".format(self.id,
            self.startdate, self.enddate, self.last, self.active)

#    for row in SESSION.query(Document).limit(30).all():
#        print row

class DocumentArticle(BASE):
    """ Document's articles """
    __tablename__ = "documentarticle"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer)
    artname1 = Column(String)
    artprice = Column(DECIMAL(13, 5))
    ispricenetto = Column(Integer)
    arttaxrate = Column(DECIMAL(6, 3))
    arttaxtype = Column(Integer)
    arttaxlabel = Column(String)
    artexcise = Column(DECIMAL(13, 3))
    artunit = Column(String)
    artsww = Column(String)
    quantity = Column(DECIMAL(13, 6))
    bruttovalue = Column(DECIMAL(13, 4))
    nettovalue = Column(DECIMAL(13, 4))

    created_at = Column(String)
    updated_at = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'document_id': self.document_id,
            'artname1': self.artname1,
            'artprice': self.artprice.to_eng_string(),
            'ispricenetto': self.ispricenetto,
            'arttaxrate': self.arttaxrate.to_eng_string(),
            'arttaxtype': self.arttaxtype,
            'arttaxlabel': self.arttaxlabel,
            'artexcise': self.artexcise.to_eng_string(),
            'artunit': self.artunit,
            'artsww': self.artsww,
            'quantity': self.quantity.to_eng_string(),
            'bruttovalue': self.bruttovalue.to_eng_string(),
            'nettovalue': self.nettovalue.to_eng_string(),
            'created_at' : self.created_at.strftime("%Y-%m-%d"),
            'updated_at' : self.updated_at.strftime("%Y-%m-%d")
        }

    def __repr__(self):
        return "<DocumentArticle (id: {}, document_id: {}, artname1: {}, bruttovalue: {}>".format(self.id,
            self.document_id, self.bruttovalue, self.bruttovalue)

class Taxrate(BASE):
    """ Taxrate """

    __tablename__ = "taxrate"

    id = Column(Integer, primary_key=True)

    rate = Column(DECIMAL(14, 3))
    type = Column(Integer)
    label = Column(String)

    created_at = Column(String)
    updated_at = Column(String)
