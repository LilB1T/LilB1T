from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("faisalgym.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/about")
def about():
    team_members = [
    {"name": "Faisal Bhau", "role": "CEO & Founder", "image": "faisalbhau.png"},
    {"name": "Syed Hasan Washa", "role": "Chief Technology Officer", "image":"hasan.JPG"},
    {"name": "Abdul Hadi", "role": "Head of Marketing", "image": "meme.png"}
]
    return render_template("aboutus.html", team_members=team_members)

@app.route("/membership")
def membership():
    # Define the membership plans
    plans = [
        {
            "name": "Basic",
            "price": "$0/month",
            "description": "For individuals getting started.",
            "features": [
                "✔ Access to all basic modules",
                "✔ Community Support",
                "✘ Premium Content"
            ],
            "button_text": "Sign Up",
            "button_link": "#"
        },
        {
            "name": "Pro",
            "price": "$19/month",
            "description": "For professionals and small teams.",
            "features": [
                "✔ Access to all features",
                "✔ Email Support",
                "✔ Premium Content"
            ],
            "button_text": "Get Started",
            "button_link": "#"
        },
        {
            "name": "Premium",
            "price": "$49/month",
            "description": "For businesses and enterprises.",
            "features": [
                "✔ All Pro features",
                "✔ Dedicated Account Manager",
                "✔ Priority Support"
            ],
            "button_text": "Upgrade Now",
            "button_link": "#"
        }
    ]

    # Pass the plans to the template
    return render_template("membership.html", plans=plans)

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404


if __name__ == "__main__":
    app.run(debug=True)
