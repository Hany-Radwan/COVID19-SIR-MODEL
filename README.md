# COVID-19 SIR Epidemic Model

This project implements a COVID-19–specific SIR (Susceptible–Infected–Recovered) epidemiological model using Python and object-oriented programming (OOP).

The project is developed by the Code-Crew team as part of the Informatics course at Deggendorf Institute of Technology (DIT).

The model is designed to simulate the spread of COVID-19 within a closed population. It represents disease dynamics using three compartments: Susceptible (S), Infected (I), and Recovered (R). The infection rate (beta) and recovery rate (gamma) parameters can be adjusted to reflect different COVID-19 transmission and recovery scenarios.

The implementation follows the classical SIR model with the following assumptions: fixed total population, homogeneous mixing of individuals, no births or deaths, and immunity after recovery. The system is solved numerically using the Euler method with a fixed daily time step.

Project structure:
- sir_model.py – Core COVID-19 SIR model logic
  

## 📋 User Manual: How to Run the Simulator

Follow these simple steps to run the application on your local machine.

### 1. Prerequisites

Ensure you have Python installed. You can verify this by opening your terminal and typing:

```bash
python --version
```

### 2. Installation
   
Download the project files, open your terminal in the project folder, and install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Running the Application

To start the interactive simulator, run the following command in your terminal:

```bash
streamlit run app.py
```

### 4. Using the Simulator

Once the application launches in your web browser (usually at ``` http://localhost:8501 ``` ):

#### Sidebar Settings:

Use the sliders on the left to adjust the Infection Rate ($\beta$) and Recovery Rate ($\gamma$).

#### Population:

Input a custom population size (e.g., 10,000).

#### Visualization: 

Observe how the Red Curve (Infected) changes shape.

Try setting Beta to 0.9 to simulate a high-speed outbreak (like Omicron).

Try lowering Beta to 0.2 to see "Flattening the Curve".


## 🏗️ Project Architecture
The project follows a modular Object-Oriented Design (OOP) to separate the mathematical logic from the user interface

``` sir_model.py ``` (The Logic Layer):

Contains the ``` SIRModel ``` class.

Implements the Euler Method algorithm to solve the differential equations.

Handles state management (updating S, I, R values daily).

Note: This file is not run directly; it is imported by the main application.

``` app.py ``` (The Presentation Layer):

Built with Streamlit.

Handles user inputs (sliders for Beta/Gamma).

Visualizes the simulation results using Plotly.

``` test_sir.py ``` (Quality Assurance):

Contains unit tests to verify the mathematical accuracy of the model (e.g., ensuring population is conserved).



### Author:
### Pharmacist: Hany Z. Radwan – Deggendorf Institute of Technology
