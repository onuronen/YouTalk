from youtube_transcript_api import YouTubeTranscriptApi
from fuzzywuzzy import fuzz


def detect_words(video_id, sentence):
    subtitles = YouTubeTranscriptApi.get_transcript(video_id)
    sentence = sentence.lower()

    #if the returned list is empty
    if not subtitles:
        return "Couldn't find the subtitles in video"

    first_priority_results = []
    second_priority_results = []

    for entry in subtitles:
        entry["text"] = entry["text"].lower()
        
        # convert to minute format
        entry["start"] = entry["start"] / 60

        # 2 decimal points is enough for our purpose
        entry["start"] = round(entry["start"], 2)

        #searching if the user inputted words exactly appears in the subtitles
        if sentence in entry["text"]:
            first_priority_results.append(entry["start"])
            
        #for the case if there is no exact match, then use string comparison, append results to 
        #list over certain threshold
        elif fuzz.ratio(sentence, entry["text"]) > 70:
            second_priority_results.append(entry["start"])


    result = []
    #if first priority result list is empty check the second one, display top 3 results
    if not first_priority_results:

        #check if second list is empty
        if len(second_priority_results) > 3:
            second_priority_results = second_priority_results[:3]
            result = second_priority_results

        elif len(second_priority_results) >= 1 and len(second_priority_results) < 3:
            result = second_priority_results

    #if first priority is not empty, only display first priority results
    else:
        result = first_priority_results

    # if both lists are empty return error message
    if not result:
        return "Couldn't find the words in the video"

    else:
        # takes top 3, if there are less number of elements, the list only contains them
        result = result[:3]
        result = ", ".join([str(i) for i in result])
        return "Here are the time(s)! " + result