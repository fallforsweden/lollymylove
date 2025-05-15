# Grievance Portal 💌

This is a simple web-based grievance submission form built using Python (Flask) and HTML.

## 🛠 How to Run

1. Install dependencies:
```
pip install flask
```

2. Run the Flask app:
```
python app.py
```

3. Open `index.html` in your browser and submit your form.

Grievances will be saved to `grievances.db` locally using SQLite.

## 🔌 Make it Online

Use [ngrok](https://ngrok.com/) to make your local Flask server public:

```
ngrok http 5000
```

Use the ngrok URL in your HTML form instead of `localhost`.

