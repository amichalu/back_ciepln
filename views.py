""" Views - main apis definition """
from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, desc, asc
from models import Document, DocumentArticle

APP = Flask(__name__)


@APP.route('/documentarticles/<int:id>',methods=['GET'])
def documentarticles_index(id):
    if request.method == 'GET':
        session = SESS()
        try:
            articles = session.query(DocumentArticle).filter(DocumentArticle.document_id == id).order_by(asc('id'))
        except:
            session.rollback()
            raise
        session.close()
        return jsonify(articles=[article.serialize for article in articles])

@APP.route('/documents/', methods=['GET'], defaults={'count': 10, 'order': 'number', 'page': 0, 'dir': 'asc'})
@APP.route('/documents/<string:order>/<int:page>/<int:count>/<string:dirOrder>', methods=['GET'])
def documents_index(count, order, page, dirOrder):
    """ document main route """
    if request.method == 'GET':

        order_by_dict = {
            'number': Document.number,
            'date': Document.date,
            'netto': Document.netto,
            'brutto': Document.brutto,
            'custname1': Document.custname1,
            'custnip': Document.custnip,
            'excise': Document.excise}

        order_by = Document.number
        order_by = order_by_dict[order]
        if order_by is None:
            order_by = 'number'

        dir_dict = {'asc': 'asc', 'desc': 'desc'}
        diro = dir_dict[dirOrder]

        session = SESS()
        try:
            if diro == 'desc':
                documents = session \
                    .query(Document) \
                    .order_by(desc(order_by))[page*count:(page+1)*count]
            else:
                documents = session \
                    .query(Document) \
                    .order_by(asc(order_by))[page*count:(page+1)*count]
            # session.commit()
        except:
            session.rollback()
            raise
        session.close()
        return jsonify(documents=[document.serialize for document in documents])


if __name__ == '__main__':

    ENGINE = create_engine("mysql+pymysql://venice:pass1@localhost/venice?charset=utf8")
    SESS = sessionmaker(bind=ENGINE)

    APP.debug = True
    APP.run(host='localhost', port=5000)
