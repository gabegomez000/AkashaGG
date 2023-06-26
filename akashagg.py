from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/artifacts', methods=['GET', 'POST'])
def artifacts():
    if request.method == 'POST':
        add_selectbox = request.form.get('category')
        if add_selectbox == "Artifacts":
            reliquaryURL = "https://genshin-db-api.vercel.app/api/artifacts?query="
            reliquaryResponse = requests.get("https://genshin-db-api.vercel.app/api/artifacts?query=names&matchCategories=true").json()
            # Get the artifact options from the API response
            artifact_options = reliquaryResponse['artifacts']

            # Render the artifacts.html template with the artifact options
            return render_template('artifacts.html', artifact_options=artifact_options)

    return render_template('artifacts.html')


@app.route('/characters', methods=['GET', 'POST'])
def characters():
    if request.method == 'POST':
        add_selectbox = request.form.get('category')
        if add_selectbox == "Characters":
            archiveURL = "https://genshin-db-api.vercel.app/api/characters?query="
            archiveResponse = requests.get(archiveURL + "names&matchCategories=true").json()
            # Rest of the code for handling characters

    return render_template('characters.html')


if __name__ == '__main__':
    app.run(debug=True)
