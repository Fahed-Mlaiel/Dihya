"""
Utilitaires SEO pour l'application Dihya Coding.
Inclut : génération de balises meta, sitemap, robots.txt, et bonnes pratiques SEO.
"""

from flask import Blueprint, Response, jsonify, url_for, current_app

def generate_meta_tags(title, description, keywords=None):
    """
    Génère des balises meta SEO pour une page.
    Args:
        title (str): Titre de la page
        description (str): Description de la page
        keywords (list, optionnel): Liste de mots-clés
    Returns:
        str: HTML des balises meta
    """
    meta = [
        f'<title>{title}</title>',
        f'<meta name="description" content="{description}">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{description}">'
    ]
    if keywords:
        meta.append(f'<meta name="keywords" content="{",".join(keywords)}">')
    return "\n".join(meta)

def generate_robots_txt(allow_all=True):
    """
    Génère le contenu du fichier robots.txt.
    Args:
        allow_all (bool): Autoriser tous les robots ou non
    Returns:
        str: Contenu robots.txt
    """
    if allow_all:
        return "User-agent: *\nDisallow:"
    else:
        return "User-agent: *\nDisallow: /"

def generate_sitemap(urls):
    """
    Génère un sitemap XML à partir d'une liste d'URLs.
    Args:
        urls (list): Liste d'URLs absolues
    Returns:
        str: Sitemap XML
    """
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        xml.append(f"  <url><loc>{url}</loc></url>")
    xml.append('</urlset>')
    return "\n".join(xml)

# Exemple de blueprint pour servir robots.txt et sitemap.xml
seo = Blueprint('seo', __name__)

@seo.route('/robots.txt')
def robots_txt():
    """
    Sert le fichier robots.txt pour le SEO.
    """
    content = generate_robots_txt()
    return Response(content, mimetype='text/plain')

@seo.route('/sitemap.xml')
def sitemap_xml():
    """
    Sert le sitemap.xml pour le SEO.
    """
    # Exemple statique, à adapter pour générer dynamiquement selon les routes
    base_url = current_app.config.get("BASE_URL", "http://localhost:5000")
    urls = [
        f"{base_url}/",
        f"{base_url}/api/info",
        f"{base_url}/api/health"
    ]
    content = generate_sitemap(urls)
    return Response(content, mimetype='application/xml')