from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():

    Episode.query.delete()
    Guest.query.delete()
    Appearance.query.delete()

    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Tracey Ullman", occupation="television actress")

    db.session.add_all([ep1, ep2, g1, g2])
    db.session.commit()

    a1 = Appearance(rating=4, episode_id=ep1.id, guest_id=g1.id)
    a2 = Appearance(rating=5, episode_id=ep2.id, guest_id=g2.id)

    db.session.add_all([a1, a2])
    db.session.commit()

    print("Database seeded")
