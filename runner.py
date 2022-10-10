from app import app
from app.views import AdsView

ads_view = AdsView.as_view('ads')
app.add_url_rule("/create/", view_func=ads_view, methods=["POST"])
app.add_url_rule("/<id_>", view_func=ads_view, methods=["GET", "DELETE"])

if __name__ == '__main__':
    app.run()