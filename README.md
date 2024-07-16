
# codeXwebagent

**Overview:**

codeXwebagent is a Python repository that implements a web agent designed to simulate user interactions on login pages of websites and generate comprehensive analytics reports as part of a 2-day codeX hackathon. This tool is crucial for optimizing website usability and enhancing the overall user experience by providing valuable insights into user behavior and interaction patterns.

[![Logo](https://github.com/user-attachments/assets/8f107289-3f03-4aa4-923b-4844f462d352)]([https://www.example.com](https://codexchallenge.com/))

## Key Features

- **Simulation of User Interactions:** The agent replicates real-user behavior on websites, including clicks, scrolls, and pauses.
- **Analytics and Reporting:** It generates a heatmap to visualize user engagement and navigation flows.
- **Optimization Insights:** Helps developers and UX/UI teams identify areas for improvement on websites based on simulated user journeys.
- **Conversion Rate Enhancement:** Aims to increase conversion rates by refining user interfaces and optimizing user pathways.

## Usage

When this service is run, it first collects information about the personality and the login credentials of the user you are trying to log in as, as well as the login website. Here we use a simple GUI for it.

<p align="center">
  <img width="450" alt="Screenshot of GUI" src="https://github.com/Proud19/codeXwebagent/assets/69429112/6c5c19e8-570f-493c-a565-d7ddf53392e1">
  <img width="450" alt="Screenshot of GUI" src="https://github.com/Proud19/codeXwebagent/assets/69429112/f0f5c73c-6454-4d0b-8e99-2b676e79e719">
</p>

When given this information, the backend creates an agent whose task is to log in to the given website. Here is a short demo:

[![Demo Video](https://img.youtube.com/vi/d575137d-e2d0-4f0d-9274-64b78623783a/0.jpg)](https://github.com/Proud19/codeXwebagent/assets/69429112/d575137d-e2d0-4f0d-9274-64b78623783a)

Alongside automatic login, the system also tracks various actions that the agent is making and creates a heatmap to show the agent's activity.

<p align="center">
  <img width="600" alt="Heatmap Image" src="https://github.com/user-attachments/assets/a8f7401e-98e1-4855-915e-97c84c85ccd4">
</p>

## Technical Details

### System Architecture

The codeXwebagent system is composed of several components that work together to simulate user interactions, collect interaction data, and generate analytics reports. Below is a detailed architecture diagram and description of each component.

<p align="center">
  <img width="600" alt="codeXwebagent_system_architecture" src="https://github.com/user-attachments/assets/ad4cfefc-ae83-4c06-aa98-bc48e281a5e2">
</p>


1. **User Info Collection:**
   - **GUI Interface:** A simple GUI collects user information, including login credentials and target website URL.
   - **User Info App:** The `runUserInfoApp` function handles user input and triggers the login simulation.

2. **Web Interaction Simulation:**
   - **Selenium WebDriver:** Automates the web browser to simulate user actions such as clicks, scrolls, and form submissions.
   - **ActionChains:** Used to create complex user interaction sequences, making the simulation more realistic.

3. **AI-Driven Element Selection:**
   - **OpenAI Integration:** Utilizes the OpenAI API to analyze the HTML content of login pages and generate appropriate selectors for form fields.
   - **ChatGPT:** Generates code snippets for interaction based on the page's HTML content.

4. **Interaction Tracking:**
   - **InteractionTracker:** A custom module that tracks user interactions (clicks, movements) and stores the data.
   - **Heatmap.js:** A JavaScript library injected into the page to visualize interaction data as a heatmap.

5. **Data Visualization:**
   - **Heatmap Generation:** Interaction data is processed and displayed as a heatmap, highlighting areas of high user engagement.
