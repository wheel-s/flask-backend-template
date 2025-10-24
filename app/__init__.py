from flask import Flask, jsonify
from app.config import Config
from app.routes.auth import auth_bp
from app.routes.students import student_bp
from app.routes.courses import course_bp
from app.routes.grades import grade_bp
from app.extensions import db, jwt, migrate

import pymysql 


pymysql.install_as_MySQLdb()




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from app import models
    migrate.init_app(app, db)
    jwt.init_app(app)
   

    app.register_blueprint(auth_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(course_bp)
    app.register_blueprint(grade_bp)



    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Resourcce not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error":"Internal servr error"}, 500)
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error":"Bad request"}), 400
    @app.errorhandler(403)
    def no_auth():
        return jsonify({"error":"NOt authourized"})


  

    return app
