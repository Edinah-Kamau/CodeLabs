# Massive Dataset Translation Project

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
       - [Question 1:](#Generating en-xx.xlxs Files)
       - [Question 2:](#Working with Files) 
- [Contributing](#contributing)


## Introduction

The Massive Dataset Translation Project is a Python 3-based solution designed for handling and processing a massive dataset containing language translations. This project provides a structured and organized approach to address the assessment questions while demonstrating best practices in Python development, file management, and documentation.

## Prerequisites
Before you get started, make sure you have the following requirements in place:

Python 3.8+ installed on your system.
[Optional] A virtual environment tool like virtualenv or conda.
Access to the MASSIVE Dataset mentioned in the Data File provided.
A properly configured Python development environment, including the installation of the required packages listed in requirements.txt.

## Installation

Follow these steps to set up the project:

### 1. Clone the Repository:

Open your terminal and navigate to the directory where you want to store the project. Then, run the following command to clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-project.git

### 2.Navigate to the Project Directory:

Change your working directory to the project folder:

bash
Copy code
cd your-project

### 3.Create and Activate a Virtual Environment:

To isolate your project's dependencies, consider creating a virtual environment. Run these commands:

bash
Copy code
virtualenv venv
source venv/bin/activate

### 4.Install Dependencies:

Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt

## Usage

## Question 1: Generating en-xx.xlsx Files
To generate en-xx.xlsx files for all languages based on the MASSIVE Dataset, follow these steps:

### 1.Navigate to the Project Directory:

Ensure you are in the project directory where the Python scripts are located.

### 2.Run the Question 1 Script:

Execute the script for Question 1:

bash
Copy code
python question1_script.py
This script will process the dataset and generate en-xx.xlsx files for all languages where English is the pivot language.

### Question 2: Working with Files
In this section, you'll perform various tasks related to working with files as outlined in the assessment questions.

Run the Question 2 Script:
Execute the script for Question 2:

bash
Copy code
python question2_script.py
This script will perform the following tasks:

Generate separate JSONL files for 'test,' 'train,' and 'dev' datasets for English, Swahili, and German.
Create one large JSON file containing translations from English (en) to other languages (xx) for the 'train' dataset with 'id' and 'utt.'
The JSON structure will be pretty printed for readability.


## Uploading Files
After running the scripts, you can upload the generated files to your Google Drive Backup Folder and commit any changes to your GitHub repository.

### 1.Google Drive Backup Folder:

Manually upload the generated files to your Google Drive Backup Folder.

### 2.GitHub Repository:

Commit and push all changes to the GitHub repository to keep your code and generated files versioned.

## Contributing
If you'd like to contribute code to the project, follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and thoroughly test them.
Submit a Pull Request (PR) with a clear description of your changes and their significance.
This project aims to provide a comprehensive solution for handling massive translation datasets while maintaining code quality and documentation standards. Your contributions are welcome and greatly appreciated!
