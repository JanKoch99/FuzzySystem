# Gift Recommendation System - Setup and Usage Guide

## 🎁 Project Overview

This is a **Gift Recommendation System** that uses **Fuzzy Logic** to suggest personalized gifts based on:

- Your age, budget, and relationship with the recipient
- The recipient's personality, interests, and preferences
- The occasion and style

The system consists of:

- **Frontend**: React application (already provided)
- **Backend**: FastAPI server with fuzzy logic engine

---

## 📋 Prerequisites

Before running the application, make sure you have:

1. **Python 3.8 or higher** installed

   - Check: `python3 --version`
   - Download from: https://www.python.org/downloads/

2. **Node.js and npm** (for frontend)

   - Check: `node --version` and `npm --version`
   - Download from: https://nodejs.org/

3. **Git** (optional, for version control)

---

## 🚀 Backend Setup (FastAPI)

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create a Virtual Environment (Recommended)

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:

- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `scikit-fuzzy` - Fuzzy logic library
- `numpy` - Numerical computing
- `pydantic` - Data validation

### Step 4: Start the Backend Server

```bash
python main.py
```

Or alternatively:

```bash
uvicorn main:app --reload --port 4000
```

The backend server will start at: **http://localhost:4000**

You can check if it's running by visiting: http://localhost:4000 (you should see a JSON response)

---

## 🎨 Frontend Setup (React)

### Step 1: Navigate to Frontend Directory

Open a **new terminal** and navigate to the frontend directory:

```bash
cd frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

### Step 3: Start the Frontend Server

```bash
npm run dev
```

The frontend will start at: **http://localhost:5173**

---

## 🎯 How to Use the Application

1. **Open your browser** and go to: http://localhost:5173

2. **Start the journey**:

   - Click "Start Now" on the home page

3. **Enter Your Data**:

   - Move the sliders to indicate your age
   - Set your budget preference
   - Define how close you are to the recipient
   - Select the occasion

4. **Enter Recipient's Data**:

   - Choose their gender
   - Set their personality (introvert to extrovert)
   - Rate their technical, creative, managerial, and academic interests
   - Select their style preference

5. **Choose Between Gift Pairs**:

   - You'll see 5 rounds of gift comparisons
   - Click on the gift you prefer in each round
   - The system learns your preferences

6. **Get Final Recommendations**:
   - View your top 3 personalized gift recommendations
   - Each gift is scored by the fuzzy logic system

---

## 🔧 API Endpoints

The backend provides these endpoints:

### 1. Health Check

```
GET http://localhost:4000/
```

Returns server status

### 2. Generate Image Pairs

```
POST http://localhost:4000/api/generate-image-pairs
```

Generates 5 diverse gift pairs for comparison

### 3. Generate Final Recommendations

```
POST http://localhost:4000/api/generate-final-images
```

Generates 3 final gift recommendations based on selections

### 4. Get All Gifts

```
GET http://localhost:4000/api/gifts
```

Returns all available gifts (for debugging)

### 5. Get Specific Gift

```
GET http://localhost:4000/api/gifts/{gift_id}
```

Returns details of a specific gift

---

## 📁 Project Structure

```
FuzzySystem/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── fuzzy_logic.py       # Fuzzy logic engine
│   ├── models.py            # Pydantic data models
│   ├── requirements.txt     # Python dependencies
│   └── data/
│       └── gifts.json       # Gift database (30 gifts)
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # Main app component
│   │   ├── pages/           # Page components
│   │   ├── services/        # API service
│   │   └── ...
│   └── package.json         # Node dependencies
└── README.md                # This file
```

---

## 🧪 Testing the Backend

You can test the backend using curl or a tool like Postman:

### Test Image Pairs Generation:

```bash
curl -X POST http://localhost:4000/api/generate-image-pairs \
  -H "Content-Type: application/json" \
  -d '{
    "user": {
      "age": 25,
      "budget": 60,
      "relationship": 75,
      "occasion": "Birthday"
    },
    "other": {
      "gender": "Female",
      "personality": 65,
      "technical": 40,
      "creative": 80,
      "managerial": 50,
      "academic": 60,
      "style": "Modern"
    }
  }'
```

---

## ❗ Troubleshooting

### Backend won't start:

- Make sure virtual environment is activated
- Check if port 4000 is available
- Verify all dependencies are installed: `pip list`

### Frontend won't start:

- Make sure node_modules are installed: `npm install`
- Check if port 5173 is available
- Clear npm cache: `npm cache clean --force`

### CORS errors:

- Ensure backend is running on port 4000
- Check CORS settings in `backend/main.py`

### Import errors (scikit-fuzzy):

- Try installing with: `pip install scikit-fuzzy==0.4.2`
- On some systems, you may need: `pip install --upgrade numpy scipy`

---

## 🛑 Stopping the Application

### To stop the backend:

- Press `Ctrl + C` in the backend terminal
- Deactivate virtual environment: `deactivate`

### To stop the frontend:

- Press `Ctrl + C` in the frontend terminal

---

## 📚 Additional Resources

- FastAPI Documentation: https://fastapi.tiangolo.com/
- Scikit-Fuzzy Documentation: https://pythonhosted.org/scikit-fuzzy/
- React Documentation: https://react.dev/

---

## 🎓 Understanding Fuzzy Logic

For a detailed explanation of how the fuzzy logic system works, see:
**FUZZY_LOGIC_EXPLAINED.md**

---

## 👨‍💻 Development

### Adding New Gifts:

Edit `backend/data/gifts.json` and add a new gift object following this structure:

```json
{
  "id": "gift_XXX",
  "name": "Gift Name",
  "category": "Category",
  "description": "Description",
  "price_range": 50,
  "image_url": "image.jpg",
  "attributes": {
    "gender": "neutral",
    "personality": 50,
    "technical": 50,
    "creative": 50,
    "managerial": 50,
    "academic": 50,
    "style": "Modern",
    "occasions": ["Birthday", "Holiday"],
    "relationship_score": 50
  }
}
```

After adding gifts, restart the backend server.

---

## 🤝 Support

If you encounter any issues:

1. Check that both servers are running
2. Review the terminal logs for error messages
3. Verify all dependencies are installed
4. Ensure you're using compatible Python/Node versions

---

**Happy Gift Shopping! 🎁**
