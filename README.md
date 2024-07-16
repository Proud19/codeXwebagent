
# codeXwebagent

**Overview:**

codeXwebagent is a Python repository that implements a web agent designed to simulate user interactions on login pages of websites and generate comprehensive analytics reports as part of a 2-day codeX hackathon. This tool is crucial for optimizing website usability and enhancing the overall user experience by providing valuable insights into user behavior and interaction patterns.

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
  <img width="600" alt="Heatmap Image" src="https://github.com/Proud19/codeXwebagent/assets/69429112/d4ef4475-1976-44db-9031-6ff6fc3c785c">
</p>
