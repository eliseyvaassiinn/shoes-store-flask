from flask import Flask

from app.controllers.task_controller import ShoeController


def create_app():
    app = Flask(__name__, template_folder="views/templates")
    app.secret_key = "shoes-catalog-secret-key"

    controller = ShoeController()

    @app.route("/", methods=["GET"])
    def index():
        return controller.index()

    @app.route("/shoes", methods=["POST"])
    def store():
        return controller.store()

    @app.route("/shoes/<int:shoe_id>/delete", methods=["POST"])
    def delete(shoe_id):
        return controller.delete(shoe_id)

    return app