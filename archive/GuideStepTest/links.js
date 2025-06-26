console.log("links.js loaded an executing at " + (new Date()).toString());

const links = [
  { uri:"./page-one.html"                    ,label:"one" },
  { uri:"./page-two.html"                    ,label:"two" },
  { uri:"./page-three.html"                   ,label:"three" },
  ];
document.write("<p>");
for (var i = 0; i < links.length; i++) {
  if (i > 0) {
    document.write(" | ");
  }
  document.write("<a href=\"" + links[i].uri + "\">" + links[i].label + "</a>");
}
document.write("</p>");
