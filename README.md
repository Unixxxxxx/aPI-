<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     ANIMATED HEADER                          -->
<!-- ══════════════════════════════════════════════════════════════ -->

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=230&section=header&text=aPI-&fontSize=90&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=Python%20REST%20API%20%7C%20Flask%20%7C%20JSON%20%7C%20Docker%20%7C%20CI%2FCD&descAlignY=58&descSize=18"/>

</div>

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     TYPING ANIMATION                         -->
<!-- ══════════════════════════════════════════════════════════════ -->

<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=700&size=22&duration=2800&pause=900&color=00D9FF&center=true&vCenter=true&width=760&height=55&lines=🔌+RESTful+API+built+with+Python+%26+Flask;📡+GET+%7C+POST+%7C+PUT+%7C+DELETE+Endpoints;🔐+Secure+%7C+Token+Auth+%7C+JSON+Responses;🐳+Dockerized+%7C+GitHub+Actions+CI%2FCD;⚡+Fast.+Lightweight.+Production-Ready." alt="Typing SVG" />
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST](https://img.shields.io/badge/REST-API-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-00ffaa?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-00d9ff?style=for-the-badge)

<br/>

<!-- Animated tech icons -->
<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="60">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="60">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="60">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="60">
<img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2bc.gif" width="60">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="60">

</div>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     OVERVIEW                                  -->
<!-- ══════════════════════════════════════════════════════════════ -->

## <img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" width="30"/> &nbsp; Overview

<table>
<tr>
<td width="54%" valign="top">

```python
#!/usr/bin/env python3
# ══════════════════════════════════════════
#   aPI-  |  REST API by Sudhanshu Sharma
# ══════════════════════════════════════════

from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

PROJECT = {
    "name"      : "aPI-",
    "author"    : "Sudhanshu Sharma",
    "version"   : "1.0.0",
    "framework" : "Flask (Python)",
    "type"      : "RESTful API",
    "methods"   : ["GET", "POST", "PUT", "DELETE"],
    "auth"      : "Token / JWT Based",
    "features"  : [
        "Full CRUD operations",
        "JSON request & response",
        "Input validation",
        "Structured error handling",
        "Docker support",
        "GitHub Actions CI/CD",
    ],
    "status"    : "Active 🚀",
}

@app.route("/api/info")
def info():
    return jsonify(PROJECT), 200
```

</td>
<td width="46%" align="center" valign="top">

<br/>

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="340"/>

<br/><br/>

> 🔌 A lightweight **Python Flask REST API** implementing full CRUD operations with clean JSON responses, token-based auth, and proper HTTP status codes — built for learning and real-world deployment.

<br/>

[![View Repo](https://img.shields.io/badge/GitHub-View_Repo-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Unixxxxxx/aPI-)
[![Author](https://img.shields.io/badge/Author-Sudhanshu_Sharma-00d9ff?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Unixxxxxx)

</td>
</tr>
</table>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     FEATURES                                  -->
<!-- ══════════════════════════════════════════════════════════════ -->

## ✨ Features

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="750"/>
</div>

<br/>

<table>
<tr>
<td width="50%" valign="top">

```
✦  Full CRUD REST endpoints
✦  JSON request & response
✦  Token-based authentication
✦  Input validation & sanitisation
✦  Structured error messages
```

</td>
<td width="50%" valign="top">

```
✦  Proper HTTP status codes
✦  Modular Blueprint routing
✦  Environment config (.env)
✦  Docker + Docker Compose
✦  GitHub Actions CI/CD
```

</td>
</tr>
</table>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     PROJECT STRUCTURE                         -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🗂️ Project Structure

<img align="right" src="https://user-images.githubusercontent.com/74038190/229223156-0cbdaba9-3128-4d8e-8719-b6b4cf741b67.gif" width="260"/>

```bash
aPI-/
│
├── 📄 app.py                    # Flask app entry point
├── 📄 requirements.txt          # Python dependencies
├── 📄 Dockerfile                # Docker config
├── 📄 docker-compose.yml        # Multi-container setup
├── 📄 .env                      # Environment variables
├── 📄 README.md
│
├── 📂 routes/                   # Blueprint route modules
│   ├── __init__.py
│   ├── api.py                   # Core CRUD endpoints
│   └── auth.py                  # Auth endpoints
│
├── 📂 models/                   # Data models
│   └── models.py
│
├── 📂 utils/                    # Helper functions
│   └── helpers.py
│
├── 📂 tests/                    # Unit tests
│   └── test_api.py
│
└── 📂 .github/
    └── workflows/
        └── deploy.yml           # CI/CD pipeline
```

<br clear="right"/>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     API ENDPOINTS                             -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🔌 API Endpoints

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212750672-2f3f2b50-c84f-4ed8-a60a-849ae69ff9df.gif" width="500"/>
</div>

<br/>

**Base URL →** `http://localhost:5000/api`

```
┌──────────┬──────────────────────────┬────────────────────────────────────────┐
│  Method  │  Endpoint                │  Description                           │
├──────────┼──────────────────────────┼────────────────────────────────────────┤
│  GET     │  /api/                   │  Welcome & API info                    │
│  GET     │  /api/items              │  Retrieve all items                    │
│  GET     │  /api/items/<id>         │  Retrieve single item by ID            │
│  POST    │  /api/items              │  Create a new item                     │
│  PUT     │  /api/items/<id>         │  Update an existing item               │
│  DELETE  │  /api/items/<id>         │  Delete an item                        │
├──────────┼──────────────────────────┼────────────────────────────────────────┤
│  POST    │  /api/auth/register      │  Register a new user                   │
│  POST    │  /api/auth/login         │  Login & receive JWT token             │
│  GET     │  /api/auth/profile       │  Get current user (auth required)      │
└──────────┴──────────────────────────┴────────────────────────────────────────┘
```

### 📥 Request — `POST /api/items`

```json
{
  "name":        "Sample Item",
  "description": "A test item for the API",
  "category":    "test",
  "value":       42
}
```

### 📤 Response — `201 Created`

```json
{
  "status": "success",
  "data": {
    "id":          1,
    "name":        "Sample Item",
    "description": "A test item for the API",
    "category":    "test",
    "value":       42,
    "created_at":  "2026-03-02T10:30:00Z"
  }
}
```

### ❌ Error — `400 Bad Request`

```json
{
  "status":  "error",
  "message": "Field 'name' is required",
  "code":    400
}
```

### 🔐 Auth Header

```
Authorization: Bearer <your_token_here>
```

### HTTP Status Codes

<div align="center">

| Code | Status | Meaning |
|------|--------|---------|
| `200` | ✅ OK | Successful GET / PUT |
| `201` | ✅ Created | Successful POST |
| `204` | ✅ No Content | Successful DELETE |
| `400` | ❌ Bad Request | Validation failed |
| `401` | 🔐 Unauthorized | Token missing or invalid |
| `404` | 🔍 Not Found | Resource not found |
| `500` | 💥 Server Error | Internal error |

</div>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     QUICK START                               -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🚀 Quick Start

<img align="right" src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="280"/>

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Unixxxxxx/aPI-.git
cd aPI-
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

```bash
cp .env.example .env
```

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
PORT=5000
```

### 4️⃣ Run the API

```bash
python app.py
```

```
 * Running on  http://127.0.0.1:5000
 * Debug mode: ON
 ✅  REST API is live!
```

<br clear="right"/>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     DOCKER                                    -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🐳 Docker Deployment

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257463-4d082cb4-7483-4eaf-bc25-6dde2628aabd.gif" width="80"/>
</div>

<br/>

### Build & Run

```bash
docker build -t sudhanshu-api .
docker run -d -p 5000:5000 sudhanshu-api
```

### Docker Compose

```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-secret-key
    restart: always
```

```bash
docker-compose up -d
```

> ✅ Visit **`http://localhost:5000/api`**

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     TESTING                                   -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🧪 Testing

### cURL

```bash
# GET all items
curl -X GET http://localhost:5000/api/items

# POST new item
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "description": "Hello API"}'

# PUT update
curl -X PUT http://localhost:5000/api/items/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name": "Updated"}'

# DELETE
curl -X DELETE http://localhost:5000/api/items/1 \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Python requests

```python
import requests

BASE = "http://localhost:5000/api"

# GET all
print(requests.get(f"{BASE}/items").json())

# POST
r = requests.post(f"{BASE}/items", json={
    "name": "New Item",
    "description": "Via Python"
})
print(r.status_code)   # 201
```

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     TECH STACK                                -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     DEPENDENCIES                              -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 📦 Dependencies

```bash
pip install -r requirements.txt
```

| Package | Purpose |
|---------|---------|
| `flask` | Web framework & routing |
| `flask-cors` | Cross-origin request support |
| `flask-jwt-extended` | JWT token authentication |
| `python-dotenv` | Load `.env` variables |
| `requests` | HTTP client for testing |

---

<!-- ══════════════════════════════════════════════════════════════ -->
<!--                     AUTHOR                                    -->
<!-- ══════════════════════════════════════════════════════════════ -->

## 🙋 Author

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/235294019-40007353-6219-4ec5-b661-b3c35136dd0b.gif" width="80"/>

<br/><br/>

**Sudhanshu Sharma**

🛡️ Cyber Security Analyst &nbsp;|&nbsp; 💻 Full Stack Developer &nbsp;|&nbsp; 🐍 Python & Flask Engineer

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sudhanshu_Sharma-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sudhanshu-kumar-281a84204/)
[![Gmail](https://img.shields.io/badge/Gmail-Sudhanshuroyss208@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Sudhanshuroyss208@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Unixxxxxx-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Unixxxxxx)

<br/><br/>

> *"First, solve the problem. Then, write the code."* — John Johnson

</div>

---

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%"/>

<br/>

**⚡ Built with Python & Flask by Sudhanshu Sharma 🚀**

<br/>

![Flask](https://img.shields.io/badge/Built_with-Flask_%26_Python-000000?style=flat-square&logo=flask&logoColor=white)
&nbsp;
![REST](https://img.shields.io/badge/API-RESTful-FF6C37?style=flat-square&logo=postman&logoColor=white)
&nbsp;
![Stars](https://img.shields.io/github/stars/Unixxxxxx/aPI-?style=flat-square&color=ffb347&logo=github)
&nbsp;
![Updated](https://img.shields.io/badge/Updated-March_2026-00d9ff?style=flat-square)

<br/><br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=110&section=footer&animation=twinkling"/>

</div>
