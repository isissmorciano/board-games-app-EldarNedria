import os
from flask import Flask

#  Factory function to create and configure the Flask application
def create_app():
    # Create the Flask application instance, specifying that configuration files are located in the instance folder which is outside the version control and can hold sensitive data
    app = Flask(__name__, instance_relative_config=True)
    # Set default configuration values for the application
    app.config.from_mapping(
        # secret key for session management
        SECRET_KEY='dev',
        # path to the SQLite database file located in the instance folder
        DATABASE=os.path.join(app.instance_path, 'board_games.sqlite'),
    )

    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Initialize the database
    from . import db
    db.init_app(app)

    # Register the main blueprint in the application (for it to be available in the app)
    from . import main
    app.register_blueprint(main.bp)

    return app