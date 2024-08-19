# Inference Proxy Backend

Backend handling requests from user-facing clients and proxying them to the locally run inference server. 

## Description

This repository contains the backend implementation for handling requests from user-facing clients and forwarding them to a locally run inference server. The backend is built entirely in Python.

At this moment it uses one hardcoded inference server workflow.

## Features

- Handles client requests.
- Proxies requests to the inference server.
- Manages response handling and error checking.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
To start the backend server, run:

```bash
python app.py
```

Ensure that the local inference server is running and accessible by the backend.
