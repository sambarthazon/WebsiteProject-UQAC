from website import create_app

# Create an app
if __name__ == "__main__":
    app = create_app()
    app.run(host = "0.0.0.0", port = 7007, debug=True) # Run the app with host '0.0.0.0' and port 7007