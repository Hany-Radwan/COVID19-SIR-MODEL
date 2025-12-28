# COVID-19 SIR Epidemic Model

This project implements a COVID-19–specific SIR (Susceptible–Infected–Recovered) epidemiological model using Python and object-oriented programming (OOP).

The project is developed by the Code-Crew team as part of the Informatics course at Deggendorf Institute of Technology (DIT).

The model is designed to simulate the spread of COVID-19 within a closed population. It represents disease dynamics using three compartments: Susceptible (S), Infected (I), and Recovered (R). The infection rate (beta) and recovery rate (gamma) parameters can be adjusted to reflect different COVID-19 transmission and recovery scenarios.

The implementation follows the classical SIR model with the following assumptions: fixed total population, homogeneous mixing of individuals, no births or deaths, and immunity after recovery. The system is solved numerically using the Euler method with a fixed daily time step.

Project structure:
- sir_model.py – Core COVID-19 SIR model logic

Example usage (described conceptually):
The user initializes the SIRModel class with population size, initial infected individuals, infection rate, and recovery rate, then runs the simulation for a specified number of days to obtain S, I, and R time series.

This model is intended for educational purposes, understanding COVID-19 spread dynamics, and supporting health informatics coursework.

Authors:
Code-Crew Team – Deggendorf Institute of Technology
