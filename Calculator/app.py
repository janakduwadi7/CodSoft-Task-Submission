from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    
    try:
        data=request.form
        num1=float(data.get("num1",0))
        num2=float(data.get("num2",0))
        operation=data.get("operation")

        if operation=="add":
            result=num1+num2
            operation_sign="+"
        elif operation=="subtract":
            result=num1-num2
            operation_sign="-"
        elif operation=="multiply":
            result=num1*num2
            operation_sign="*"
        elif operation=="divide":
            if num2!=0:
                result=num1/num2
                operation_sign="/"
            else:
                return render_template("calculator.html", error="Cannot divide by zero!")
        else:
            result = None
            operation_sign = "Invalid"

        return render_template('index.html', result=result, num1=num1, num2=num2, operation_sign=operation_sign)

    except ValueError:
        render_template('index.html',error="Invalid input. Please enter valid numbers!")


if __name__=="__main__":
    app.run(debug=True)