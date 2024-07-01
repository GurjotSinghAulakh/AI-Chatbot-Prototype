### Step-by-Step Guide to Run and Test the E-commerce Chatbot

---

#### Step 1: Extract the Zip File

1. Extract the zip file:
   - Locate the zip file you received.
   - Extract the contents of the zip file to a directory of your choice.

---

#### Step 2: Set Up the Python Environment

2. Navigate to the project directory:
   - Open a terminal or command prompt.
   - Change the directory to the location where you extracted the zip file.
     ```bash
     cd path/to/extracted/directory
     ```

3. Create and activate a virtual environment:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On macOS and Linux:
       ```bash
       source venv/bin/activate
       ```
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```

4. Install the dependencies:
   - Ensure you have a `requirements.txt` file in the project directory with the following content:
     ```
     Flask==2.1.1
     Flask-Cors==3.0.10
     spacy==3.2.3
     ```
   - Install the dependencies listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

5. Download the spaCy model:
   - Download the `en_core_web_md` model for spaCy:
     ```bash
     python -m spacy download en_core_web_md
     ```

---

#### Step 3: Verify the Backend Setup

6. Ensure you have the following files in the project directory:
   - `app.py`
   - `faqs.json`

---

#### Step 4: Set Up the Frontend

7. Ensure you have the following frontend files:
   - `index.html`
   - `styles.css`
   - `script.js`

---

#### Step 5: Run the Backend Server

8. Start the Flask server:
   ```bash
   cd backend
   python app.py
   ```
   or
   ```bash
   cd backend
   python3 app.py
   ```

   The server should start running at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

#### Step 6: Test the Chatbot

9. Open the `index.html` file in your web browser.

10. Interact with the chatbot:
    - Type a message in the input field and press Enter or click the send button.
    - The chatbot should respond to your queries based on the predefined FAQs in `faqs.json`.

---

### E-commerce Chatbot images

##### Title: E-commerce Chatbot
![Image 1](/E-commerce%20Chatbot%20Images/chatbot.png "E-commerce Chatbot")

##### Title: Greetings
![Image 2](/E-commerce%20Chatbot%20Images/greetings.png "Greetings")

##### Title: Conversation
![Image 3](/E-commerce%20Chatbot%20Images/conversation.png "Conversation")

##### Title: Fallback Response
![Image 4](/E-commerce%20Chatbot%20Images/fallback-response.png "Fallback Response")

##### Title: Farewell
![Image 5](/E-commerce%20Chatbot%20Images/farewells.png "Farewell")

### Contact Information for Assistance

If you encounter any issues or need further assistance, please feel free to contact:

- **Name**: Gurjot Singh Aulakh
- **Email**: [gurjot.singh.aulakh28@gmail.com](mailto:gurjot.singh.aulakh28@gmail.com)
- **Phone**: +47 973 87 540

---
