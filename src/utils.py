from youtube_transcript_api import YouTubeTranscriptApi

def detect_words(video_id, sentence):
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)

    #if the returned list is empty
    if not subtitles:
        return "Couldn't find the subtitles in video"

    results = []
    for entry in subtitles:
        if sentence in entry["text"]:
            results.append(entry["start"] / 100)


    if not results:
        return "Couldn't find the words in the video"
    else:
        return results