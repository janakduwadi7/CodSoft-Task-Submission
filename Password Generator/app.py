from flask import Flask,render_template,request
import string
import random
app=Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api/generatedpw",methods=['POST'])
def generatedpw():
    data=request.form
    len=int(data.get("length",8))
    include_upper='upper' in data
    include_lower='lower' in data
    include_digits='digits' in data
    include_special='speccharacters' in data

    char_pool=""

    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: Please select character set,No character set selected to generate the password."

    password = ''.join(random.choices(char_pool, k=len))

    return render_template("result.html", password=password)
  

if __name__=="__main__":
    app.run(debug=True)