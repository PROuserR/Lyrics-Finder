//  This function will fetch the song and artist name, and then will submit them
//  to the form in order to get the lyrics
const searchHotTrack = async (e) => {
    const artist_input = document.getElementById('artist-input')
    const song_input = document.getElementById('song-input')
    const search_btn = document.getElementById('search-btn')

    song_input.value = e.target.nextElementSibling.innerText
    artist_input.value = e.target.nextElementSibling.nextElementSibling.innerText

    search_btn.click()
}