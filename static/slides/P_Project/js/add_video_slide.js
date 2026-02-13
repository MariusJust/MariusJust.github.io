var slide = document.currentScript.getAttribute('slide_scene');
function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  console.log("load")
  return result;
}
frags = loadFile(`/static/slides/P_Project/video_slides/videos/${slide}.txt`)
document.write(`
<section 
	data-background-video="/static/slides/P_Project/video_slides/videos/${slide}.mp4" 
	data-background-size="contain"
	data-background-color="#101518" 
	id="vid" 
	type="videoslide"
>
 ${frags}
</section>`)
