from tempmon import app as application

if __name__ == "__main__":
    application.run("0.0.0.0", port=80, threaded=True, debug=True)
    