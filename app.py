from flask import Flask, render_template, jsonify
from flask_cors import CORS
from datetime import datetime
import os
from models import db, Order, Certification, init_db

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///aga.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        init_db()

    # CORS for APIs (optional)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # ---- Front-end routes ----
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/pricing")
    def pricing():
        return render_template("pricing.html")

    @app.route("/lookup")
    def lookup_page():
        return render_template("lookup.html")

    @app.route("/order-status")
    def order_status_page():
        return render_template("order-status.html")

    @app.route("/submit")
    def submit_page():
        return render_template("submit.html")

    @app.route("/specials")
    def specials_page():
        return render_template("specials.html")

    # ---- Minimal APIs ----
    @app.get("/api/health")
    def health():
        return jsonify({"ok": True, "time": datetime.utcnow().isoformat()})

    @app.get("/api/order-status/<order_id>")
    def api_order_status(order_id):
        o = Order.query.filter((Order.id == order_id) | (Order.external_id == order_id)).first()
        if not o:
            return jsonify({"error": "Not found"}), 404
        return jsonify(o.to_dict())

    @app.get("/api/lookup/<cert_number>")
    def api_lookup(cert_number):
        c = Certification.query.filter_by(cert_number=str(cert_number)).first()
        if not c:
            return jsonify({"error": "Not found"}), 404
        return jsonify(c.to_dict())

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "10000")), debug=True)
