# Cancer Biomarker Identification Project

This project aims to identify cancer biomarkers using a Python backend (Flask API) and a React frontend, incorporating machine learning capabilities for predictions.

## Table of Contents
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Setting Up the Backend (Python and Flask)](#2-setting-up-the-backend-python-and-flask)
  - [3. Setting Up the Frontend (React)](#3-setting-up-the-frontend-react)

## Project Description

This project provides an interface for identifying potential cancer biomarkers. It uses a Python backend powered by Flask, where the machine learning models are hosted, and a React frontend that allows users to interact with the model and view results.

## Prerequisites

- **Node.js and npm** (for frontend)
- **Python 3 and pip** (for backend)
- `virtualenv` (recommended for managing Python dependencies)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine and navigate into the project directory:

```bash
    git clone https://github.com/AnishMane/Cancer-Associated-Biomarker-Identification.git
    cd Cancer-Associated-Biomarker-Identification
```

### 2. Setting Up the Backend (Python and Flask)

```bash
    cd backend
    python -m venv venv   # (or `python3 -m venv venv` for Mac)
    venv/Scripts/activate  # (or `source venv\bin\activate` for Mac)
    pip install -r requirements.txt
```

### 3. Setting Up the Frontend (React)

```bash
    cd frontend
    npm install
    npm start
```