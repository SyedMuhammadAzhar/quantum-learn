# QuantumLearn

An interactive quantum computing education platform designed to make quantum mechanics accessible through hands-on visualizations and real quantum circuit simulations. Built with modern web technologies and powered by Qiskit, this platform provides an engaging learning experience for students, educators, and quantum computing enthusiasts.

## Features

### Interactive Learning Experience
- **Step-by-Step Lessons**: Comprehensive lessons on quantum computing fundamentals including superposition and entanglement
- **Real Quantum Simulations**: Authentic quantum circuit simulations powered by Qiskit's quantum computing framework
- **Visual Demonstrations**: Interactive visualizations including quantum coin flips and Bell state measurements
- **Live Statistics**: Real-time probability tracking and measurement statistics with visual charts

### User Experience
- **Dark Mode Support**: Seamless theme switching with persistent user preferences
- **AI-Powered Assistant**: Integrated chat assistant using Groq API for instant help and explanations
- **Interactive Quizzes**: Knowledge assessment with immediate feedback and detailed explanations
- **Comprehensive FAQ**: Common questions answered with beginner-friendly language

### Advanced Features
- **Bell State Demonstrations**: Interactive Alice & Bob entanglement experiments with space-themed visualizations
- **Batch Measurements**: Run multiple quantum measurements (1x, 10x, 100x) to observe probability convergence
- **Animated Visualizations**: GSAP-powered animations showing quantum particle behavior and entanglement correlations

## Tech Stack

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

## Prerequisites

- Node.js (v16 or higher)
- Python (v3.9 or higher)
- npm or yarn package manager
- pip (Python package manager)

## Getting Started

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

## Running Both Servers

For full functionality, run both backend and frontend simultaneously:

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

## Project Structure

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

## Configuration

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

## Learning Features Overview

### Quantum Superposition
- Single and multi-coin quantum demonstrations
- Real quantum circuit execution with Qiskit simulator
- Visual representation of quantum state superposition
- Probability tracking showing convergence to theoretical values

### Quantum Entanglement
- Interactive Alice & Bob measurement scenarios
- All four Bell states (Φ⁺, Ψ⁺, Φ⁻, Ψ⁻) with live switching
- Space-themed visualization with Earth and Mars locations
- Instant correlation demonstrations across distance
- Real-time measurement statistics and pattern analysis

### Educational Tools
- Progressive lesson structure with clear explanations
- Interactive quizzes with instant feedback
- Detailed FAQs covering common quantum mechanics questions
- Code examples and visual analogies for complex concepts

## Troubleshooting

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

## Learn More

### Quantum Computing Resources
- [Qiskit Documentation](https://qiskit.org/documentation/) - IBM's quantum computing framework
- [Qiskit Textbook](https://qiskit.org/textbook/) - Free online quantum computing course

### Framework Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Svelte Documentation](https://svelte.dev/) - Reactive JavaScript framework
- [Vite Documentation](https://vitejs.dev/) - Next generation frontend tooling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Authors

**Core Contributors:**
- **Syed Muhammad Azhar** - [@SyedMuhammadAzhar](https://github.com/SyedMuhammadAzhar)
- **Zahid Ali** - [@zaahidali](https://github.com/zaahidali)
- **Kalsoom Athar** - [@Kalsoom-Athar](https://github.com/Kalsoom-Athar)

## Acknowledgments

Built with passion for quantum education. Special thanks to the Qiskit community and all contributors who helped make quantum computing more accessible.

---

**Happy Quantum Learning!**
