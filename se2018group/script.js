console.log("Hey")
$(document).ready(function() {
  console.log($(".vTop.hLeft.pam").size());
  var people = {};
  $(".vTop.hLeft.pam").each(function(elem) {
    var imgSrc = $(this).find("img").attr("src").split("/")[2];
    var name = $(this).find(".fsl.fwb.fcb").find("a").text();
    console.log(imgSrc + " " + name);
    people[name] = imgSrc;
  });

  console.log("Done", people);
  var json = JSON.stringify(people);
  var blob = new Blob([json], { type: "application/json" });
  saveAs(blob, "people.json");
});
