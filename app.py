# Import libraries
from flask import Flask, redirect, url_for, request, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route("/add", methods=["POST", "GET"])
def add_transaction():
    if request.method == "POST":
        transaction = {
            'id': transactions[-1]['id'] + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))
    return render_template("form.html")

# Update operation
@app.route("/edit/<int:transaction_id>", methods=["POST", "GET"])
def edit_transaction(transaction_id):
    transaction = None
    for t in transactions:
        if t['id'] == transaction_id:
            transaction = t
            break
    if request.method == "POST":
        transaction['date'] = request.form['date']
        transaction['amount'] = float(request.form['amount'])
        return redirect(url_for('get_transactions'))
    return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    transaction = None
    for t in transactions:
        if t['id'] == transaction_id:
            transaction = t
            break
    transactions.remove(transaction)
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)