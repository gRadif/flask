from app import app, db
from flask import request, jsonify

from exceptions_app import resource_not_found
from .models import Ads
from flask.views import MethodView


class AdsView(MethodView):

    def get(self, id_: int):
        res = db.get_or_404(Ads, id_)
        return jsonify({"id": res.id,
                        "title": res.title,
                        "description": res.description,
                        "owner": res.owner,
                        "created_at": res.created_at,
                        "update_at": res.update_at})

    def post(self):
        valid_data = request.json
        new_ad = Ads(
            title=valid_data['title'],
            description=valid_data['description'],
            owner=valid_data['owner']
        )
        db.session.add(new_ad)
        db.session.commit()
        return jsonify({'id': new_ad.id})

    def delete(self, id_: int):
        db.session.query(Ads).filter(Ads.id == id_).delete(synchronize_session="fetch")
        db.session.commit()
        return jsonify({'status': 200})
