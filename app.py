from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def route():
    return make_response(request)


@app.route("/<any>", methods=['GET', 'POST'])
def any(any):
    return make_response(request)


def make_response(req):
    headers = '\n'.join([": ".join(header) for header in req.headers.to_wsgi_list()])
    body = req.data.decode(encoding='utf-8')
    res = f"""# URL
{req.url}

# Headers
{headers}

# Body
{body}

# Referrer
{req.referrer}

# Remote Host
{req.remote_addr}

# UserAgent
{req.user_agent}
"""
    print(res)
    return res.replace("\n\n", "<p>").replace("\n", "<br>")


if __name__ == "__main__":
    print("⚡️⚡️⚡️ Flask launch! ⚡️⚡️⚡️")
    app.run(host='0.0.0.0', port=5000, debug=True)
