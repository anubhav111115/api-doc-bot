const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const stringSimilarity = require("string-similarity");

const app = express();
const PORT = 3001;

app.use(cors());
app.use(bodyParser.json());

// Expanded API Responses Dictionary
const responses = {
    // API Basics
    "what is api": "API stands for Application Programming Interface. It allows different software applications to communicate with each other.",
    "types of api": "The main types of APIs are REST, SOAP, GraphQL, and gRPC.",
    "what is rest api": "REST API follows RESTful principles using HTTP methods like GET, POST, PUT, and DELETE.",
    "what is graphql": "GraphQL is a query language that lets clients request specific data, reducing over-fetching or under-fetching.",
    "what is openapi": "OpenAPI is a specification for building APIs, enabling automatic documentation and standardization.",
    "what is swagger": "Swagger is a set of tools for API documentation and testing, based on the OpenAPI specification.",
    "difference between rest and soap": "REST is lightweight and works with JSON/XML, whereas SOAP is heavier and uses XML with strict standards.",
    "what is an endpoint in api": "An API endpoint is a specific URL where an API can be accessed to perform a certain function.",
    "what is authentication in api": "API authentication ensures that only authorized users or applications can access API resources.",
    "difference between authorization and authentication": "Authentication verifies identity, while authorization controls access to resources.",

    // Command-related Questions
    "what is curl command": "cURL is a command-line tool used to transfer data with URLs, commonly used for API requests.",
    "curl command to send get request": "Use: `curl -X GET 'https://api.example.com/data'`",
    "curl command to send post request": "Use: `curl -X POST -H 'Content-Type: application/json' -d '{\"key\": \"value\"}' 'https://api.example.com/data'`",
    "postman vs curl": "Postman provides a GUI for API testing, whereas cURL is a command-line tool.",
    
    // Git Commands
    "how to clone a git repository": "Use: `git clone <repo-url>`",
    "how to check git status": "Use: `git status` to see changes in the working directory.",
    "git command to create a new branch": "Use: `git branch <branch-name>` to create a new branch.",
    "git command to switch branch": "Use: `git checkout <branch-name>` or `git switch <branch-name>`",
    "how to merge a branch in git": "Use: `git merge <branch-name>` while on the main branch.",
    
    // Linux Commands
    "how to check current directory in linux": "Use: `pwd` to print the current working directory.",
    "how to list files in a directory": "Use: `ls` to list files, `ls -la` for detailed view.",
    "how to change directory in linux": "Use: `cd <directory-name>` to change the directory.",
    "linux command to create a file": "Use: `touch filename.txt` to create a file.",
    "linux command to delete a file": "Use: `rm filename.txt` to delete a file.",
    
    // Docker Commands
    "what is docker": "Docker is a platform to develop, ship, and run applications inside lightweight containers.",
    "docker command to list running containers": "Use: `docker ps` to list running containers.",
    "docker command to start a container": "Use: `docker start <container-id>`",
    "docker command to stop a container": "Use: `docker stop <container-id>`",
    "docker command to remove a container": "Use: `docker rm <container-id>`",
    
    // Miscellaneous
    "what is json": "JSON (JavaScript Object Notation) is a lightweight data format used for APIs and data storage.",
    "what is xml": "XML (eXtensible Markup Language) is a structured document format used in APIs and configurations.",
    "difference between json and xml": "JSON is lighter and widely used in APIs, while XML is more structured with schemas.",
    "what is an api key": "An API key is a unique identifier used to authenticate and authorize API requests.",
    "how to secure an api": "Use authentication (API keys, OAuth), rate limiting, HTTPS, and input validation.",
};

// Function to find the best response using fuzzy matching
function findBestResponse(query) {
    const keys = Object.keys(responses);
    const matches = stringSimilarity.findBestMatch(query, keys);
    const bestMatch = matches.bestMatch;

    if (bestMatch.rating > 0.5) { 
        return responses[bestMatch.target];
    } else {
        return "I couldn't find an exact answer. Try rephrasing your question.";
    }
}

// API Endpoint
app.post("/ask", (req, res) => {
    const query = req.body.query.toLowerCase();
    console.log("User asked:", query);

    const answer = findBestResponse(query);
    console.log("Bot Answer:", answer);
    
    res.json({ answer });
});

// Start Server
app.listen(PORT, () => {
    console.log(`✅ Server running on http://localhost:${PORT}`);
});
