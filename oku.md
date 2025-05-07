### Deneme:
- Tarayıcıdan şu URL'yi ziyaret et: http://localhost:5000/?name={{7*7}}
Web sayfasında şu yazıyı görürsün: Merhaba 49

Bu, Jinja2 template engine’in kullanıcı girdisini şablon gibi işlediğini gösterir.
Kötü niyetli biri bunun yerine şunu da deneyebilir:
- http://localhost:5000/?name={{config.items()}}

