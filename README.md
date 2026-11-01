# SOC Investigation Lab: SSH Authentication Analysis

## Overview

This project demonstrates a beginner-level Security Operations Center (SOC) investigation using simulated Linux SSH authentication logs and Python.

The goal is to identify repeated failed login attempts, analyze authentication activity by source IP address, and flag IP addresses associated with both failed and successful login events.

## Objectives

- Analyze authentication logs.
- Detect failed SSH login attempts.
- Extract and count source IP addresses.
- Identify successful authentication events.
- Flag suspicious authentication patterns.
- Document findings in an incident report.

## Tools and Technologies

- Python 3.14
- Linux (Ubuntu on WSL)
- Regular expressions
- Git and GitHub
- Markdown

## Project Structure

```text
SOC-Investigation-Lab/
├── logs/
│   └── auth.log
├── scripts/
│   └── analyze_logs.py
├── reports/
│   └── incident-report.md
└── README.md
```

## How to Run

From the project directory, execute:

```bash
python3 scripts/analyze_logs.py
```

The script reports the total log entries, failed login attempts, failure counts by source IP, successful login events, and suspicious IP alerts.

## Sample Findings

The simulated dataset contains:

- 10 authentication log entries.
- 8 failed login attempts.
- 5 failed attempts from `185.220.101.45`.
- 3 failed attempts from `45.33.32.156`.
- A successful login to the `backup` account from `185.220.101.45` after the failed attempts.

The script flags `185.220.101.45` for further investigation.

## Investigation Limitations

The logs are simulated and do not represent a real security incident. A matching source IP across failed and successful authentication events is a detection lead, not proof of compromise. The current detection logic does not yet enforce chronological ordering or a configurable failure threshold.

## Deliverables

- Python authentication log analyzer.
- Simulated SSH authentication dataset.
- Preliminary incident investigation report.

## Future Improvements

- Add a configurable failed-login threshold.
- Verify that failed attempts occurred before successful authentication.
- Export findings to a structured report.
- Add automated tests for detection logic.
- Expand the investigation with additional log sources.

## Disclaimer

This project is for educational purposes and demonstrates basic security monitoring and incident investigation techniques using synthetic data.
