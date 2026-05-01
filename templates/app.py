from flask import Flask, render_template, Response

app = Flask(__name__)

# --- GOOGLE İÇİN ÖZEL AYARLAR ---

@app.route('/robots.txt')
def robots():
    # Google botuna "İçeri gir, her yeri tara" komutu veriyoruz.
    content = "User-agent: *\nAllow: /\nSitemap: https://elite-service.onrender.com/sitemap.xml"
    return Response(content, mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap():
    # Google'ın sitendeki sayfaları kolayca bulması için yol haritası.
    content = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url><loc>https://elite-service.onrender.com/</loc><priority>1.0</priority></url>
        <url><loc>https://elite-service.onrender.com/booking</loc><priority>0.8</priority></url>
    </urlset>"""
    return Response(content, mimetype='application/xml')

# --- SAYFA ROTALARI ---

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

if __name__ == "__main__":
    app.run(debug=True)
