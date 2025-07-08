from flask import Flask, render_template, request, jsonify
from langdetect import detect, lang_detect_exception
import pycountry
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
import time
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///language_history.db'
app.config['CACHE_TYPE'] = 'SimpleCache'  # Using Flask's built-in caching
db = SQLAlchemy(app)
@app.context_processor
def template_globals():
    def get_language_name(code):
        try:
            language = pycountry.languages.get(alpha_2=code)
            return language.name if language else code
        except Exception:
            return code
    return {'get_language_name': get_language_name}
# Simple cache decorator
def cache_result(ttl=60):  # 1 minute default TTL
    cache = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < ttl:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result
        return wrapper
    return decorator

class DetectionHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000), nullable=False)
    detected_language = db.Column(db.String(10), nullable=False)
    confidence = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def get_language_name(code):
    try:
        language = pycountry.languages.get(alpha_2=code)
        return language.name if language else code
    except Exception:
        return code

@app.route('/')
def index():
    history = DetectionHistory.query.order_by(DetectionHistory.timestamp.desc()).limit(5).all()
    return render_template('index.html', recent_history=history)

@app.route('/detect', methods=['POST'])
@cache_result(ttl=300)  # Cache for 5 minutes
def detect_language():
    text = request.json.get('text')
    
    if not text or len(text.strip()) < 3:
        return jsonify({
            'error': 'Please enter at least 3 characters'
        }), 400
        
    try:
        language_code = detect(text)
        language_name = get_language_name(language_code)
        
        detection = DetectionHistory(
            text=text[:2000],
            detected_language=language_code,
            confidence=None
        )
        db.session.add(detection)
        db.session.commit()
        
        return jsonify({
            'language': language_code,
            'language_name': language_name,
            'text': text[:200]
        })
        
    except lang_detect_exception.LangDetectException:
        return jsonify({
            'error': 'Unable to detect language'
        }), 400
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/history')
def history():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    history = DetectionHistory.query.order_by(
        DetectionHistory.timestamp.desc()
    ).paginate(page, per_page, False)
    
    return render_template('history.html', history=history)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)