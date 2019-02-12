from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return make_response(request)

@app.route("/<any>", methods=['GET', 'POST'])
def any(any):
    return make_response(request)

def make_response(req):
    res = req.url + "\n\n" + "\n".join([": ".join(header) for header in req.headers.to_wsgi_list()]) + "\n\n" + req.data.decode(encoding='utf-8')
    print(res)
    return res.replace("\n\n", "<p>").replace("\n", "<br>")

if __name__ == "__main__":
    print("⚡️⚡️⚡️ Flask launch! ⚡️⚡️⚡️")
    app.run(host='0.0.0.0', port=5000, debug=True)