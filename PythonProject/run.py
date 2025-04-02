from app import app

app = app('DevelopmentConfig')

if __name__ == '__main__':
    app.run(debug=True)
