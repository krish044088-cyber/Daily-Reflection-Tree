# Daily Reflection Decision Tree
## Overview
This project implements a deterministic decision tree to evaluate daily productivity based on user inputs.
## Part A: Deterministic Decision Tree
The system follows a rule-based approach:
- If the goal is completed:
  - Hours >= 5 → Highly Productive Day
  - Hours < 5 → Moderately Productive Day
- If the goal is not completed:
  - Distraction → Improve Focus
  - Low Energy → Fix Sleep Routine
  - Lack of Planning → Plan Tomorrow Better
The output is fully deterministic, meaning the same input always produces the same output.
## Part B: AI Agent (Optional)
A simple AI-based assistant interacts with the user and provides suggestions based on their responses.
## Approach
- Designed a structured decision tree using if-else conditions
- Ensured no randomness in output
- Focused on clarity and logical flow
## Handling AI Hallucination
- Avoided vague and open-ended responses
- Restricted outputs to predefined categories
- Verified all logic manually
- Ensured consistent and explainable outputs
## Tech Used
- Python (basic control structures)
