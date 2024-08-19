# Inference Proxy Backend

Backend handling requests from user-facing clients and proxying them to the locally run inference server. 

## Description

This repository contains the backend implementation for handling requests from user-facing clients and forwarding them to a locally run inference server. The backend is built entirely in Python.

At this moment it uses one hardcoded inference server workflow.

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

## Endpoints

### POST /roboflow-replace

This endpoint accepts an image, processes it using a specified workflow, and returns the modified image.

- **URL:** `/roboflow-replace`
- **Method:** `POST`
- **Query Parameters:**
  - `replace_from` (string): The string to be replaced in the image.
  - `replace_to` (string): The string to replace with in the image.
- **Request Body:**
  - Binary image data.
- **Responses:**
  - **Success (200):**
    - Returns the modified image in JPEG format.
  - **Client Error (400):**
    - Returns a JSON object indicating a missing image or keys.
    - Example:
      ```json
      {
          "error": "Missing image or keys"
      }
      ```

## Example Request

```bash
curl -X POST "http://<server_address>:<port>/roboflow-replace?replace_from=old_text&replace_to=new_text" \
     -H "Content-Type: image/jpeg" \
     --data-binary "@path_to_image_file.jpg"

Ensure that the local inference server is running and accessible by the backend.
