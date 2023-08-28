import random
from time import sleep

from Api.protocol import  *

@app.errorhandler(400)
def error_400(e):
    return "fuck You bitch. "

@app.errorhandler(404)
def error_404(e):
    sleep(10)
    return "are you scan me?:"+str(random.randint(223, 2333323)), 404

@app.route('/', methods=["GET"])
@app.route('/home', methods=["GET"])
def home():
    return render_template("home.html",
                           amplification=render_template("/texts/amplification.txt"),
                           production=render_template("/texts/production.txt"),
                           img_text=IMG_EQUIP_TEXTS)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=80, debug=True)