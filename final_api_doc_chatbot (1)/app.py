from flask import Flask, render_template, request, jsonify
import requests
import urllib3

app = Flask(__name__)

# Disable SSL warnings (Optional, clean console)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === Home Page ===
@app.route('/', methods=['GET', 'POST'])
def index():
    response_data = None
    if request.method == 'POST':
        api_key = request.form.get('api_key', '').strip()
        endpoint = request.form.get('endpoint', '').strip()

        headers = {}
        if api_key:
            headers['Authorization'] = f'Bearer {api_key}'

        try:
            # Try fetching API normally
            response = requests.get(endpoint, headers=headers, timeout=10)
            response.raise_for_status()
            response_data = response.json()
        except requests.exceptions.SSLError:
            # SSL error: try again with SSL verification disabled
            try:
                response = requests.get(endpoint, headers=headers, verify=False, timeout=10)
                response.raise_for_status()
                response_data = response.json()
            except Exception as e:
                response_data = {'error': str(e)}
        except Exception as e:
            response_data = {'error': str(e)}

    return render_template('index.html', response_data=response_data)

# === Chatbot Page ===
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# === Chatbot Communication ===
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    # Predefined simple bot responses
    answers = {
"what is api": "API stands for Application Programming Interface. It allows two applications to communicate.",
"what is rest api": "REST API follows REST principles for web communication, where communication happens over HTTP.",
"what is postman": "Postman is a popular API testing tool that helps developers test, develop, and manage APIs.",
"hello": "Hello! How can I assist you today?",
"who made you": "I was made by Krishna Sah & Anubhav Singh ❤️",
"what is flask": "Flask is a lightweight Python web framework used to build web applications.",
"what are the types of api": "The main types of APIs are: \n1. REST API \n2. SOAP API \n3. GraphQL API \n4. JSON-RPC and XML-RPC.",
"what is soap api": "SOAP (Simple Object Access Protocol) is a protocol for exchanging structured information using XML over a network.",
"what is graphql": "GraphQL is a query language for APIs that allows clients to request specific data from the server, making it flexible and efficient.",
"what is json rpc": "JSON-RPC is a remote procedure call (RPC) protocol encoded in JSON, allowing clients to call methods remotely.",
"what is api gateway": "An API Gateway is a server that acts as an API front-end, receiving API requests, aggregating the results, and sending the response back to the requester.",
"what is oauth": "OAuth is an open standard for access delegation commonly used for token-based authentication and authorization.",
"what is openapi": "OpenAPI is a specification for building APIs, describing the API structure, inputs, and outputs using a standard format like YAML or JSON.",
"what is the difference between rest and soap": "REST is stateless and uses HTTP methods, while SOAP is a protocol and uses XML for messaging. REST is more flexible, while SOAP is more rigid and secure.",
"what is api authentication": "API authentication ensures that the API request comes from a trusted source. Common methods include API keys, OAuth, and JWT (JSON Web Tokens).",
"what is api versioning": "API versioning is a way of managing changes to the API over time to ensure backward compatibility. It can be done using URL paths, query parameters, or HTTP headers.",
"what is webhooks": "Webhooks are user-defined HTTP callbacks that are triggered by specific events, allowing one system to notify another when an event occurs.",
"what is a rate limit in api": "Rate limiting is the practice of limiting the number of requests a client can make to an API in a certain period to prevent abuse and overuse of resources.",
"what is api throttling": "API throttling is the process of intentionally limiting the rate of requests a client can make to an API to ensure fair resource usage and protect from overload.",
"how do you test an api": "You can test an API using tools like Postman or by writing automated test scripts in programming languages like Python using libraries such as `requests` and `pytest`.",
"what is json": "JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.",
"what is xml": "XML (eXtensible Markup Language) is a markup language used to encode data in a format that is both human-readable and machine-readable.",
"what are the benefits of using api": "APIs enable modular and reusable components, allow for better integration between systems, and can save time and resources in development.",
"what is api documentation": "API documentation provides detailed information about the API, including the available endpoints, request methods, parameters, and examples of usage.",
"what is jsonwebtoken": "JSON Web Token (JWT) is an open standard for securely transmitting information between parties as a JSON object, used for authentication and authorization."
}

    for keyword in answers:
        if keyword in user_message:
            return jsonify({'reply': answers[keyword]})

    return jsonify({'reply': "Sorry, I don't understand that. Try asking about jokes, cat facts, dogs, SpaceX, userinfo or product info."})

# === Fake Local APIs for Testing ===
@app.route('/fakeapi/userinfo', methods=['GET'])
def user_info():
    return {
        "name": "John Doe",
        "email": "john@example.com",
        "status": "active"
    }

@app.route('/fakeapi/product', methods=['GET'])
def product_info():
    return {
        "product_name": "SuperWidget",
        "price": "$99",
        "availability": "In Stock"
    }

if __name__ == '__main__':
    app.run(debug=True)
