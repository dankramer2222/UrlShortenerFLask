import random
import string
from flask import Flask, render_template , redirect , request

app = Flask(__name__)

ShortUrl ={ }
def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars)for _ in range (length))
    return short_url



@app.route("/" , methods=["GET","POST"])
def index():
    if request.method=="POST":
        long_url = request.form['long_url']
        short_url=generate_short_url()
        while short_url in ShortUrl:
            short_url =generate_short_url()
        ShortUrl[short_url]=long_url
        return f"ShortUrl:  +{request.url_root}{short_url}"
    return render_template("index.html")

@app.route("/short_url")
def redirected_url (short_url):
    long_url=ShortUrl.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Url nof found", 404

if __name__ == "__main__":
    app.run(debug=True)

