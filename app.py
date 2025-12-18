from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/edad', methods=['GET', 'POST'])
def edad():
    if request.method == 'POST':
        print(request.form)
        age = int(request.form['age'])

        return render_template(
            'result.html',
            age=age
        )

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)