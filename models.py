from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(255), unique=True, index=True)  # placeholder for future Stripe/session IDs
    email = db.Column(db.String(255), index=True)
    quantity = db.Column(db.Integer, default=1)
    service_type = db.Column(db.String(32), default="standard")
    status = db.Column(db.String(32), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "external_id": self.external_id,
            "email": self.email,
            "quantity": self.quantity,
            "service_type": self.service_type,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
        }

class Certification(db.Model):
    __tablename__ = "certifications"
    id = db.Column(db.Integer, primary_key=True)
    cert_number = db.Column(db.String(64), unique=True, index=True, nullable=False)
    player = db.Column(db.String(255))
    set_name = db.Column(db.String(255))
    year = db.Column(db.String(16))
    grade = db.Column(db.String(16))
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "cert_number": self.cert_number,
            "player": self.player,
            "set_name": self.set_name,
            "year": self.year,
            "grade": self.grade,
            "notes": self.notes,
            "created_at": self.created_at.isoformat(),
        }

def init_db():
    db.create_all()
