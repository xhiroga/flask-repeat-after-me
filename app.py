from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello1():
    print(request.headers)
    print(request.full_path)
    return request.full_path + "<br>" + "<br>".join([": ".join(header) for header in request.headers.to_wsgi_list()])

@app.route("/<any>")
def any(any):
    print(request.headers)
    print(request.full_path)
    return request.full_path + "<br>" + "<br>".join([": ".join(header) for header in request.headers.to_wsgi_list()])

if __name__ == "__main__":
    print("⚡️⚡️⚡️ Flask launch! ⚡️⚡️⚡️")
    app.run(host='0.0.0.0', port=5000, debug=True)