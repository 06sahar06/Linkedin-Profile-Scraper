import streamlit as st
import http.client
import json
import urllib.parse

def fully_encode_url(url):
    replacements = {
        '://': '%3A%2F%2F',
        '/': '%2F',
        ':': '%3A',
        '?': '%3F',
        '=': '%3D',
        '&': '%26',
        ' ': '%20'
    }
    for char, encoded in replacements.items():
        url = url.replace(char, encoded)

    return url

url=st.text_input("insérer le lien du profil sur Linkedin")
encoded_url = fully_encode_url(url)
conn = http.client.HTTPSConnection("linkedin-profile-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c059fa686amsh0b754c0d1df531bp1dfe28jsn38cf71372399",
    'x-rapidapi-host': "linkedin-profile-data.p.rapidapi.com"
}

conn.request("GET", f"/linkedin-data?url={encoded_url}", headers=headers)
res = conn.getresponse()
data = res.read()
parsed_data = json.loads(data.decode("utf-8"))
st.write(json.dumps(parsed_data, indent=4))

