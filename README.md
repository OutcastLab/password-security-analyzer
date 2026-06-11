# Password Security Analyzer

A lightweight Python-based desktop application that evaluates password strength and helps users generate more secure passwords.

## Overview

This project was developed to demonstrate fundamental cybersecurity principles related to authentication security and password hygiene. It provides a simple graphical interface to analyze passwords and offer actionable security feedback.

## Features

- Password strength evaluation (Weak / Medium / Strong)
- Security scoring system based on multiple factors
- Detection of common and insecure passwords
- Identification of weak patterns (e.g., repeated characters)
- Secure password generator
- Simple and user-friendly GUI built with Tkinter

## Security Criteria

The analyzer evaluates passwords based on:
- Length requirements
- Uppercase and lowercase character usage
- Numeric inclusion
- Special character usage
- Common password blacklist
- Repeated character patterns

## Technologies Used

- Python 3
- Tkinter (GUI)
- Regular Expressions (re module)
- Random and String libraries

## Usage

Run the application using:

```bash
python password_analyzer.py
