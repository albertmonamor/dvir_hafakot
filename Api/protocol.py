from  flask import Flask, render_template, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy
import binascii, os


# /* db:name
get_random_key: callable = lambda: binascii.b2a_hex(os.urandom(5)).decode()
FILE_NAME_DB = "dvir_hafakot"

# /* first configuration db:save file, config:flask
app = Flask("dvir_hafakot", template_folder="tmp", static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{FILE_NAME_DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = binascii.hexlify(os.urandom(25)).decode()
DBase: SQLAlchemy = SQLAlchemy(app)


IMG_EQUIP_TEXTS = {
    1:{"t":"ליין אריי", "d":"הגברה ליין ארי, מורכב מ2 סטים או סט בודד", "s":["התקנה", "פירוק והובלה"]},
    2:{"t":"ציליה צבעונית", "d":"ציליה צבעונית למסיבות טבע, צבעים מדהימים לבחירה", "s":["ציליה שמנת 10/10", "ציליה צבעונית 10/10", "התקנה", "פירוק והובלה"]},
    3:{"t":"פינות ישיבה", "d":"פינות ישיבה מפנקות כולל מזרונים וכריות", "s":["מחצלת בפינת הישיבה", "פירוק התקנה והובלה"]},
    4:{"t":"ליין אריי", "d":"סטים על גבי מנוף מותאם לאירוע שלכם", "s":["פירוק התקנה והובלה", "גנרטור כולל דלק"]},
    5:{"t":"פרוטקים 500", "d":"פרוטקים 500 וואט, עוצמתיים כולל פונקציות להתאמה לאירוע", "s":["פירוק התקנה והובלה", "סטנדים מותאמים"]},
    6:{"t":"תפאורת במה 5/3", "d":"תאורת במה, מגיע עם ציוד שתבחרו בהתאמה ", "s":["פירוק התקנה והובלה"]},
    7:{"t":"סטים של 3", "d":"סטים של 3 , בכל זוג יש באפר ורמקול. גנרטור עם 10% הנחה"},
    8:{"t":"סטים של 7", "d":"סטים של 7 , בכל זוג יש באפר ורמקול. גנרטור עם 60% הנחה"},
    9:{"t":"", "d":""}
}

EQUIP_DEAL_PACKAGE = {
    1:{"n":"גואה",
       "d":"חבילת אירוע הצגה בשבילכם",
       "w":["2 סטים ליין ארי", "ציליה ענקית","טפטפות", "הובלה פירוק והתקנה"],
       "p":3500},
    2:{"n":"קרחנה",
       "d":"חבילת אירוע משוגעת בשבילכם",
       "w":["פינות ישיבה 10 ספסלים זוגיים","מזרונים וכריות","ציליה שמנת ופופים","מחצלאות","הגברה ותאורה", "גנרטור עם דלק", "פירוק והובלה"],
       "p":3300}

}