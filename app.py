import io
import os
from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from card_reader.pipeline.layout_prediction_pipeline import LayoutPredictionPipeline
from card_reader.logger import logger

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
  def __init__(self, filename) -> None:
    predictor = LayoutPredictionPipeline()
    predictor.get_card(image=Image.open(filename))
    self.bios = predictor.predict()

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
  if request.method == 'POST':
    file = request.files['file']
    if file is None or file.filename == '':
      return jsonify({'error': 'no file'})
    if not allowed_file(file.filename):
      return jsonify({'error': 'format not supported'})
    
    try:
      result = ClientApp(file).bios
      return jsonify(result)
    except Exception as e:
      logger.error(e)
      return jsonify({'error': 'Error in the application'})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)