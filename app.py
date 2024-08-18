from flask import Flask, request, jsonify, send_file
import io
import os
from PIL import Image
from inference_sdk import InferenceHTTPClient
import base64
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ROBOFLOW_INFERENCE_API_KEY = os.getenv('ROBOFLOW_INFERENCE_API_KEY')
ROBOFLOW_INFERENCE_API_URL = "http://127.0.0.1:9001"
ROBOFLOW_WORKSPACE_NAME="test-7zrcx"
ROBOFLOW_WORKFLOW_ID="sam2-inpaiting-api"

client = InferenceHTTPClient(
    api_url=ROBOFLOW_INFERENCE_API_URL,
    api_key=ROBOFLOW_INFERENCE_API_KEY
)

@app.route('/roboflow-replace', methods=['POST'])
def post_image():
    replace_from = request.args.get('replace_from')
    replace_to = request.args.get('replace_to')
    image_file = request.data

    if not image_file or not replace_from or not replace_to:
        return jsonify({"error": "Missing image or keys"}), 400

    img_byte_arr = io.BytesIO(image_file)
    image = Image.open(img_byte_arr)

    result = client.run_workflow(
        workspace_name=ROBOFLOW_WORKSPACE_NAME,
        workflow_id=ROBOFLOW_WORKFLOW_ID,
        images={
            "image": image,
        },
        parameters={
            "replace_from": [replace_from],
            "replace_to": replace_to,
        }
    )

    inpaint_image_base64 = result[0]['inpaint_model_image']
    image_bytes_data = base64.b64decode(inpaint_image_base64)
    inpaint_img_byte_arr = io.BytesIO(image_bytes_data)
    inpaint_img_byte_arr.seek(0)

    return send_file(inpaint_img_byte_arr, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)