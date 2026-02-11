# Import create_app function from 'app' package
# This file serves as the entry point for running the Flask application.
# It creates and instance of the Flask app using the factory function and starts the development server.
# This is possible because 'app' has a __init__.py file that defines the create_app function, allowing us to import it directly.
from app import create_app

# We call the "factory" function to create an instance of the Flask application.
app = create_app()

# This block checks if the script(run.py) is being run directly (as the main program), if so it starts the Flask development server with debug mode enabled. 
# This allows for easier debugging and automatic reloading of the server when the code changes.
if __name__ == '__main__':
    app.run(debug=True)