from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True

db = SQLAlchemy(app)


@app.route("/getauthorname", methods=['GET'])
def getauthorname(authorname):
    # filter using by name
    user = models.Records.query.filter_by(name=authorname).all()

    output = {
        'id': user.id,
        'date': user.date,
        'number_of_likes': user.number_of_likes,
        'number_of_reply': user.number_of_reply,
        'comment': user.comment
    }
    return output, 200


@app.route('/getdate', methods=['GET'])
def getdate(fromdate, todate):
    # filter using by date range
    user = models.Records.query.filter_by(models.Records.date >= fromdate, models.Records.date <= todate).all

    output = {
        'id': user.id,
        'name': user.name,
        'number_of_likes': user.number_of_likes,
        'number_of_reply': user.number_of_reply,
        'comment': user.comment
    }
    return output, 200


@app.route('/getlike', methods=['GET'])
def getlike(fromlike, tolike, fromreply, toreply):
    # filter using by like and reply
    user = models.Records.query.filter_by(models.Records.like >= fromlike, models.Records.number_of_likes <= tolike,
                                          models.Records.number_of_reply >= fromreply,
                                          models.Records.number_of_reply >= toreply).all

    output = {
        'id': user.id,
        'name': user.name,
        'date': user.date,
        'comment': user.comment
    }
    return output, 200


@app.route('/getallresult', methods=['GET'])
def getallresult(name, fromdate, todate, fromlike, tolike, fromreply, toreply):
    # filter using by all area
    user = models.Records.query.filter_by(models.Records.date >= fromdate, models.Records.date <= todate,
                                          models.Records.like >= fromlike, models.Records.number_of_likes <= tolike,
                                          models.Records.number_of_reply >= fromreply,
                                          models.Records.number_of_reply >= toreply, name=name).all

    output = {
        'id': user.id,
        'name': user.name,
        'user': user.date,
        'number_of_likes': user.number_of_likes,
        'number_of_reply': user.number_of_reply,
        'comment': user.comment
    }
    return output, 200


@app.route('/getauthornamecomment', methods=['GET'])
def getauthornamecomment(name):
    try:
        user = models.Records.query.filter_by(name=name).all()

        output = {
            'comment': user.comment
        }
        return output, 200

    except Exception as e:
        return "Could not find any information"

if __name__ == '__main__':
    app.run(debug=True)
