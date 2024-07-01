from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import json

# Load the NLP model
nlp = spacy.load("en_core_web_md")

# Load FAQs from the JSON file
with open("../Database/faqs.json", "r") as f:
    faqs_data = json.load(f)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to find the best answer based on user input
def find_answer(user_input):
    doc = nlp(user_input.lower())

    # Check for greetings and farewells
    for token in doc:
        if token.lemma_ in faqs_data["greetings"]:
            return "Hello! How can I assist you today?"
        elif token.lemma_ in faqs_data["farewells"]:
            return "Goodbye! Have a great day!"

    # Find the most similar FAQ
    user_input_doc = nlp(user_input.lower())
    best_match = None
    highest_similarity = 0.0
    for question, answer in faqs_data["faqs"].items():
        question_doc = nlp(question)
        similarity = user_input_doc.similarity(question_doc)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = answer

    if highest_similarity > 0.6:  # Threshold for similarity
        return best_match
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Route for handling POST requests from frontend
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = find_answer(user_input)
    return jsonify({"response": response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
