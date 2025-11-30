from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import os
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('logs/app.log', maxBytes=10485760, backupCount=5),
    ]
)
logger = logging.getLogger(__name__)

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'postgres'),
    'database': os.getenv('DB_NAME', 'mydb'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'port': os.getenv('DB_PORT', '5432')
}

def get_db_connection():
    """Veritabanı bağlantısı oluştur"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        logger.info("Veritabanı bağlantısı başarılı")
        return conn
    except Exception as e:
        logger.error(f"Veritabanı bağlantı hatası: {e}")
        raise

def init_db():
    """Veritabanı tablosunu oluştur"""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        logger.info("Veritabanı tablosu hazır")
    except Exception as e:
        logger.error(f"Veritabanı başlatma hatası: {e}")

@app.route('/')
def index():
    """Ana sayfa - mesajları listele"""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM messages ORDER BY created_at DESC')
        messages = cur.fetchall()
        cur.close()
        conn.close()
        logger.info(f"Ana sayfa yüklendi, {len(messages)} mesaj bulundu")
        return render_template('index.html', messages=messages)
    except Exception as e:
        logger.error(f"Ana sayfa hatası: {e}")
        return render_template('index.html', messages=[], error=str(e))

@app.route('/submit', methods=['POST'])
def submit():
    """Yeni mesaj kaydet"""
    try:
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        
        if not name or not message:
            logger.warning("Boş form gönderimi")
            return redirect(url_for('index'))
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO messages (name, message) VALUES (%s, %s)',
            (name, message)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        logger.info(f"Yeni mesaj kaydedildi: {name}")
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Mesaj kaydetme hatası: {e}")
        return redirect(url_for('index'))

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok', 'service': 'flask-app'}

if __name__ == '__main__':
    logger.info("Flask uygulaması başlatılıyor...")
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)

