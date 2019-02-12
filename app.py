from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return make_response(request)

@app.route("/<any>", methods=['GET', 'POST'])
def any(any):
    return make_response(request)

def make_response(request_obj):
    res = request_obj.url + "\t" + "\n".join([": ".join(header) for header in request_obj.headers.to_wsgi_list()]) + "\t" + request_obj.data.decode(encoding='utf-8')
    print(res)
    return res.replace("\t", "<p>").replace("\n", "<br>")

if __name__ == "__main__":
    print("⚡️⚡️⚡️ Flask launch! ⚡️⚡️⚡️")
    app.run(host='0.0.0.0', port=5000, debug=True)