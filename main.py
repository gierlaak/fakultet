from flask import Flask

app=Flask(__name__)

if __name__=="__main__":
    print("hello word")
    app.run(port=(8080))
