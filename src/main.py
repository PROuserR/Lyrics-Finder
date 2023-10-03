#   Basic Flask application that find lyrics based on user query or by
#   quick selecting a track from the Hot Tracks list.
from flask import Flask, request, render_template, send_from_directory
from helper_funcs import *
import os

app = Flask(__name__)


#   Rendering the favicon of the website using send_from_directory
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


#   Implementaion of basic routing using the functions above.
@app.route("/", methods=["GET", "POST"])
def index():
    #   If the HTTP request method is Post then try to get the lyrics and render its template,
    #   otherwise return an error html page.
    if request.method == "POST":
        lyrics = getLyrics(request.form["artist-input"], request.form["song-input"])
        if lyrics:
            return render_template(
                "lyrics.html",
                lyrics=lyrics,
                artist=request.form["artist-input"],
                title=request.form["song-input"],
            )
        else:
            return render_template("error.html")
    #   If the HTTP request method is not Post then get the hot tracks and render index html page
    else:
        hot_tracks = getHotTracks()
        return render_template("index.html", hot_tracks=hot_tracks)


if __name__ == "__main__":
    app.run(debug=True)
