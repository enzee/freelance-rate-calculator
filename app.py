from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Freelance Rate Calculator</title>
<h2>Freelance Rate Calculator</h2>
<form method=post>
  Monthly Expenses: <input type=number name=expenses required><br>
  Desired Monthly Income: <input type=number name=income required><br>
  Weekly Billable Hours: <input type=number name=hours required><br>
  <input type=submit value=Calculate>
</form>
{% if rate is not none %}
  <h3>Your target hourly rate: £{{ rate }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def calculate_rate():
    rate = None
    if request.method == 'POST':
        expenses = float(request.form['expenses'])
        income = float(request.form['income'])
        hours = float(request.form['hours'])
        monthly_total = expenses + income
        rate = round(monthly_total / (hours * 4), 2)
    return render_template_string(HTML, rate=rate)

if __name__ == '__main__':
    app.run(debug=True)
