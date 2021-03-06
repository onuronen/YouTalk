url = "https://youtalkapp.herokuapp.com/"

document.getElementById('input').addEventListener("submit", function(e){
    e.preventDefault();

    var result = "Loading...";
    document.querySelector("#display_time").innerHTML = result

    var link = document.getElementById("video_link").value;
    var sentence = document.getElementById("words").value;
     
    if (link == null || sentence == null) {
        return;
    }
     
    console.log(link);
    console.log(sentence);

    var extract_video_id = link.split("v=");

    if (extract_video_id.length != 2) {
        console.log("invalid link");
        return;
    }

    var video_id = extract_video_id[1];

    if (!video_id) {
        return;
    }

    console.log(video_id);

    fetch(url + "index", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'video_id' : video_id,
            'input_sentence': sentence
        }
    }).then(response => response.json())
      .then(data => {
  
        result = data;
        document.querySelector("#display_time").innerHTML = result
    });
    

});
  

