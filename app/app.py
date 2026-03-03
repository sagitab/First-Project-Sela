import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    try:
        response = requests.get("https://www.ynet.co.il/Integration/StoryRss2.xml")
        data = ET.fromstring(response.content)
        items = data.findall(".//item")

        # Extract titles
        titles = []
        for item in items:
            title = item.find("title").text
            titles.append(title)

        # Render HTML template with titles
        return render_template('index.html', titles=titles)
        
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)