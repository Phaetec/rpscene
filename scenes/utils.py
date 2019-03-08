from django.utils.html import strip_tags
from urllib.parse import urlparse, urlunparse


def build_spotify_widget(spotify_url):
    structured_url = urlparse(strip_tags(spotify_url))
    structured_url = structured_url._replace(query="")
    structured_url = structured_url._replace(path="/embed" + structured_url.path)
    spotify_embed_url = urlunparse(structured_url)
    html = """
    <iframe src="{}" 
    width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" style="min-height:380px;">
    </iframe>
    """.format(spotify_embed_url)
    return html
