from flask import Flask
FAI=Flask(__name__)

#FAI : flask application instance


@FAI.route('/StringResponse')
def StringResponse():
    return "This is my first flask project."


if __name__=='__main__':
    FAI.run(debug=True)


