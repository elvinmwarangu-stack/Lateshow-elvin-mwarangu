from flask import request, jsonify
from flask_migrate import Migrate
from config import create_app, db
from models import Episode, Guest, Appearance

app = create_app()
migrate = Migrate(app, db)

@app.route("/")
def home():
    return {"message": "Late Show API is running"}


@app.route("/episodes")
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict() for e in episodes])

@app.route("/episodes/<int:id>")
def get_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "episode_id": a.episode_id,
                "guest_id": a.guest_id,
                "guest": a.guest.to_dict()
            }
            for a in episode.appearances
        ]
    })

@app.route("/guests")
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])

@app.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()

    try:
        appearance = Appearance(
            rating=data["rating"],
            episode_id=data["episode_id"],
            guest_id=data["guest_id"]
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == "__main__":
    app.run(debug=True)
