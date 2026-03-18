# HackerOne Scope Extractor

A Python tool to extract the structured scope of a HackerOne bug bounty program.

## Features

- Fetch all assets eligible for bounty for a given program.
- Print results in the console.
- Optionally save results to a text file.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/0xshii/scope.git
cd scope
```

2. Install dependencies:
```bash
pip install requests 
```

## Usage

```bash
python scope_pr.py [program_handle]
```
Example:
```bash
python scope_pr.py tiktok
```
- Save output to a file

```bash
python scope_pr.py [program_handle] -o output.txt
```
