from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return render_template('index.html', error='Division by zero is not allowed.')
            result = num1 / num2
        else:
            return render_template('index.html', error='Invalid operation.')

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', error='Invalid input. Please enter numeric values.')


if __name__ == '__main__':
    app.run(debug=True)
