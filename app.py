import os

from flask import Flask, request
from werkzeug.routing import Rule

app = Flask(__name__)
app.url_map.add(Rule('/', defaults={'any': ''},endpoint='index'))
app.url_map.add(Rule('/<path:any>', endpoint='any'))

@app.endpoint('index')
@app.endpoint('any')
def route(any):
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
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000), debug=True)
