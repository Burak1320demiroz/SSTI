from flask import Flask, request, render_template_string, escape

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get("name", "Ziyaretçi")

    # Kullanıcı girdisini escape ederek SSTI'yi engelliyoruz , escape fonksiyonu bu tehlikeli karakterleri güvenli hâle getirir.
    
    safe_name = escape(name)
    template = f"Merhaba {safe_name}"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
