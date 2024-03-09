from flask import Flask, render_template, request, jsonify
import pyshorteners

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    if 'url' in data:
        url = data['url']
        try:
            short_url = pyshorteners.Shortener().tinyurl.short(url)
            print(short_url)
            return jsonify({'shortened_url': short_url}), 200
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'URL parameter missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
