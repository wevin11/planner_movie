from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Add this line to import CORS
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # This line enables CORS for all routes


app = Flask(__name__)

# Replace with your email details
SENDER_EMAIL = "keving6033@gmail.com"
SENDER_PASSWORD = "jsqx vjin bpbr ffkj"  # Use an app-specific password for Gmail
RECIPIENT_EMAIL = "kgonz112@outlook.com"  # Your email to receive the details

@app.route('/')
def home():
    return render_template('index.html')  # This will serve the welcome page

@app.route('/movie-date')
def movie_date():
    return render_template('movie_date_planner.html')  # Serve the movie date selection page

@app.route('/test')
def test():
    return 'Test route is working!'

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')  # Ensure you have this HTML file


@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    movie_date = data.get('date')

    # Debugging: Print out the received movie date
    print(f"Received movie date: {movie_date}")

    if not movie_date:
        return jsonify({"error": "Invalid date provided"}), 400

    # Create the email content
    subject = "Movie Date Confirmation"
    body = f"You have a movie date planned for: {movie_date}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print("Test email sent successfully")
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
