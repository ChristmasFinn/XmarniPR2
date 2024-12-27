import os
from flask import Flask, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

# HTML-шаблон для відображення
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Days to Weekend</title>
</head>
<body>
    <h1>Кількість днів до наступної суботи:</h1>
    <h2>{{ days_left }} днів</h2>
</body>
</html>
"""

@app.route('/')
def days_to_weekend():
    today = datetime.today()
    # Знаходимо наступну суботу
    next_saturday = today + timedelta((5 - today.weekday()) % 7)
    days_left = (next_saturday - today).days
    return render_template_string(html_template, days_left=days_left)
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
if __name__ == '__main__':
    app.run(debug=True)

