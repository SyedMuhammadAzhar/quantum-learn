# QuantumLearn 🚀

An interactive quantum computing education platform built with Svelte and FastAPI. Learn quantum computing concepts through hands-on visualizations and real quantum circuit simulations powered by Qiskit.

## 🌟 Features

- **Interactive Lessons**: Step-by-step lessons on quantum computing fundamentals
- **Quantum Simulations**: Real quantum circuit simulations using Qiskit
- **Visual Learning**: Interactive coin flip demonstrations showing quantum superposition
- **Dark Mode**: Toggle between light and dark themes for comfortable learning
- **AI Assistant**: Built-in chat assistant powered by Groq API for real-time help
- **Quizzes & FAQs**: Test your knowledge and get answers to common questions

## 🛠️ Tech Stack

**Frontend:**
- Svelte 5.43.5
- Vite 7.2.2
- Chart.js for visualizations
- GSAP for animations

**Backend:**
- FastAPI 0.104.1
- Qiskit 1.0.2 (Quantum computing framework)
- Qiskit Aer 0.13.3 (Quantum circuit simulator)
- Uvicorn (ASGI server)

## 📋 Prerequisites

- **Node.js** (v16 or higher)
- **Python** (v3.9 or higher)
- **npm** or **yarn**
- **pip** (Python package manager)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SyedMuhammadAzhar/quantum-learn.git
cd quantum-learn
```

### 2. Backend Setup

Navigate to the backend directory and set up the Python environment:

```bash
cd backend
```

**Create a virtual environment:**

```bash
python -m venv venv
```

**Activate the virtual environment:**

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- **Windows (Command Prompt):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Start the backend server:**

```bash
python main.py
```

The API will be available at:
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs (Interactive Swagger documentation)

### 3. Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

**Install dependencies:**

```bash
npm install
```

**Start the development server:**

```bash
npm run dev
```

The app will be available at http://localhost:5173

## 🎯 Running Both Servers

You need both the backend and frontend running simultaneously:

**Terminal 1 - Backend:**
```bash
cd backend
.\venv\Scripts\Activate.ps1  # Windows PowerShell
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

Then open your browser to http://localhost:5173

## 📁 Project Structure

```
quantum-learn/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── quantum_service.py      # Quantum circuit simulation logic
│   ├── requirements.txt        # Python dependencies
│   └── venv/                   # Python virtual environment
├── frontend/
│   ├── src/
│   │   ├── components/         # Svelte components
│   │   │   ├── layout/         # Layout components (LandingPage, LessonLayout)
│   │   │   ├── lessons/        # Lesson-specific components (Quiz, FAQ, StepContent)
│   │   │   ├── quantum/        # Quantum visualizations (CoinFlip, MultiCoinFlip)
│   │   │   └── ui/             # Reusable UI components (Button, Card, ThemeToggle)
│   │   ├── services/           # API and external service integrations
│   │   ├── stores/             # Svelte stores for state management
│   │   ├── styles/             # Global CSS and theme definitions
│   │   ├── App.svelte          # Root application component
│   │   └── main.js             # Application entry point
│   ├── public/                 # Static assets
│   ├── package.json            # Node.js dependencies
│   └── vite.config.js          # Vite configuration
└── README.md                   # This file
```

## 🔧 Configuration

### Backend Configuration

The backend runs on port **8000** by default. To change this, modify `main.py`:

```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Change port here
```

### Frontend Configuration

The frontend expects the backend at `http://localhost:8000`. If you change the backend port, update the API base URL in `frontend/src/services/api.js`.

### CORS Settings

The backend allows requests from the following origins (configured in `main.py`):
- http://localhost:5173
- http://localhost:5174
- http://localhost:3000
- http://127.0.0.1:5173

Add more origins if needed.

## 🎨 Features Overview

### Quantum Coin Flip
- Single and double coin demonstrations
- Real quantum circuit simulation
- Visual representation of superposition
- Statistics tracking with probability convergence

### Lessons
- **Superposition**: Learn about quantum states and superposition
- Interactive step-by-step content
- Code examples and visual analogies
- Quizzes to test understanding

### Dark Mode
- Toggle between light and dark themes
- Persistent theme preference (saved in localStorage)
- All components optimized for both themes

## 🐛 Troubleshooting

### Backend won't start (Port 8000 already in use)

Find and kill the process using port 8000:

**Windows:**
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -i :8000
kill -9 <PID>
```

### Frontend can't connect to backend

1. Verify the backend is running at http://localhost:8000/docs
2. Check browser console for CORS errors
3. Ensure the frontend API service is pointing to the correct backend URL

### Python dependencies fail to install

Make sure you're using Python 3.9 or higher:
```bash
python --version
```

If using Windows and you get script execution errors, enable script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📚 Learn More

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Svelte Documentation](https://svelte.dev/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Authors

- Syed Muhammad Azhar - [@SyedMuhammadAzhar](https://github.com/SyedMuhammadAzhar)

---

**Happy Quantum Learning! 🎓✨**
