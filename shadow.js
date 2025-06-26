let shadowTarget = document.getElementById("shadow-root");
let shadow = shadowTarget.attachShadow({ mode: "open" });

let shadowButton = document.createElement("button");
let shadowParagraph = document.createElement("p");
let shadowStyles = document.createElement("style");
shadowStyles.innerHTML = `
  p {
    color: purple !important;
    font-weight: bold !important;
  }
`;
shadowButton.type = "button";
shadowButton.id = "thisIsTheShadowButtonId"
shadowButton.innerHTML = "Click Shadow";
shadowParagraph.innerHTML = "This purple section is the shadow root";
shadow.appendChild(shadowStyles);
shadow.appendChild(shadowButton);
shadow.appendChild(shadowParagraph);
