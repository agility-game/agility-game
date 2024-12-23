# server/src/agility_game/utils/app_utils.py
import logging
from apiflask import APIFlask
from flask import jsonify
from ..config import DevelopmentConfig as Config  # DevelopmentConfig | ProductionConfig


def create_app(config=Config):
    """Create and configure the Flask application"""
    app = APIFlask(
        __name__,
        static_url_path="/static",
        static_folder="../static",
        template_folder="../templates",
    )

    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Load configuration
    app.config.from_object(config)

    @app.route("/")
    def home():
        return jsonify(
            {"message": "Welcome to the Agility Game Server!", "status": "healthy"}
        )

    @app.route("/health")
    def health_check():
        return jsonify(
            {"status": "ok", "environment": app.config.get("ENV", "Not Set")}
        )

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=3000)

    return app
