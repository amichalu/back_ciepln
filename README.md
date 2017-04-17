##### The backend api server for REACT-REDUX-FRONT front application. 

The technologies used so far:

* [caddy](https://caddyserver.com/) - as https and proxy server
* [uWSGI](https://uwsgi-docs.readthedocs.io/) - as http proxy for Flask app 
* [Flask](http://flask.pocoo.org/) - as api http lib
* [SQLAlchemy](http://www.sqlalchemy.org/) - as ORM
* [MariaDB](https://mariadb.org/) - as data layer


###### API description

url: https://solidity.kz/9001/ (use link with concrete api call below) 

e.g. **https://solidity.kz:9001/documents/number/0/20/asc**

###### 1) GET /documents/<string:order>/<int:page>/<int:count>/<string:dirOrder>

returns the documents:

  * ordered by: *<string:order>* ['number', 'date', 'netto', 'brutto', 'custname1', 'custnip', 'excise']
  * in asc or desc order: *<string:dirOrder>* ['asc','desc']
  * page nmb: *<int:page>*
  * records count: *<int:count>*

e.g. https://solidity.kz:9001/documents/number/0/20/asc

```json
{
  "documents": [
    {
      "brutto": "7023.4100", 
      "currency_label": "USD", 
      "custaccnmb": "868", 
      "custaddress1": "P.O. Box 702, 9120 Sagittis. Av.", 
      "custaddress2": "23862 Colombo", 
      "custname1": "Ut Odio Vel Ltd", 
      "custname2": "Justine Frye", 
      "custnip": "252-16-03-019", 
      "date": "2013-10-01", 
      "excise": "0.0000", 
      "id": 4357, 
      "location": "New York", 
      "netto": "5710.0900", 
      "number": " 858/09/2013", 
      "paymethod_name": "transfer", 
      "period_enddate": "2013-10-01", 
      "period_startdate": "2013-09-01", 
      "sellername1": "Future heat company ltd", 
      "subject_name": "delivery", 
      "type": -1
    }
  ]
}
```

###### 2) GET /documentarticles/<int:id>

returns articles for given document's <int:id>

e.g. https://solidity.kz:9001/documentarticles/4357


```json
{
  "articles": [
    {
      "artexcise": "0.0000", 
      "artname1": "Variable fee for transmission services", 
      "artprice": "7.45000", 
      "artsww": "35.30.Z", 
      "arttaxlabel": "23%", 
      "arttaxrate": "0.230", 
      "arttaxtype": 1, 
      "artunit": "$/GJ", 
      "bruttovalue": "1438.6700", 
      "created_at": "2013-10-01", 
      "document_id": 4357,
      "id": 22946, 
      "ispricenetto": 1, 
      "nettovalue": "1169.6500", 
      "quantity": "157.000000", 
      "updated_at": "2013-10-01"
    }
 ]
}
```

Next steps:

should be versioned like: GET /api/v1/documents/<string:order>/<int:page>/<int:count>/<string:dirOrder>


