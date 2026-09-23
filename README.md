# AI Training Lab – Day 2

## Overview

Day 2 focuses on the fundamentals of **reasoning and acting in AI agents**.

The main concepts covered in Day 2 are:

- ReAct (Reasoning + Acting)
- Chain-of-Thought (CoT)
- Self-Consistency
- Tool usage in AI agents
- Comparing different prompting approaches

The practical tasks demonstrate how an AI model can solve problems using different reasoning approaches and how an agent can interact with external tools.

---

## Day 2 Tasks

### 1. ReAct – Course Fee Scenario

The first task demonstrates the **ReAct cycle** using course fee calculations.

The agent checks course fees using tools and then uses a calculator tool to compare two scholarship options.

The scenario compares:

- CS101 + AI202 with a 10% scholarship
- CS101 + AI202 + DS303 with a 25% scholarship

The agent uses:

- `get_course_fee()`
- `calculate()`

The result shows which option has the lower cost and the difference between the two options.

---

### 2. Chain-of-Thought Comparison

The second task compares answers generated:

- Without Chain-of-Thought
- With Chain-of-Thought

Different reasoning questions are used to observe how step-by-step reasoning affects the response.

---

### 3. Self-Consistency

The third task demonstrates **Self-Consistency**.

The same question is given to the model multiple times with a higher temperature.

The generated answers are collected and the most common answer is selected using majority voting.

---

# Library Scenario Task

## Task Title

**Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct on a Scenario of Your Own**

## Scenario

For the self-selected scenario, a **Library Management System** is used.

The user asks:

> Is AI Fundamentals available? If I borrow it for 7 days and return it 2 days late, how much late fine will I pay?

The library contains information about:

| Book | Available Copies | Fine Per Day |
|------|------------------|--------------|
| AI Fundamentals | 3 | ₹5 |
| Python Programming | 2 | ₹4 |
| Database Systems | 0 | ₹6 |

---

## Approaches Compared

### Direct Prompting

The question is directly given to the AI model without connecting it to library tools.

This demonstrates how the model responds without access to the actual library data.

File:

```text
direct_prompt.py
