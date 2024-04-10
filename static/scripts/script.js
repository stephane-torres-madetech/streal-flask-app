/* Each card has a different text result between the two emojis.

need to know the targeted radio group/card.

we have a loop index.

can i get the id/group from a group from the event target?*/

function getCheckedValue(radioGroup) {
  return (radioGroup.value = "hot");
}

function setOpinionStyle(radioGroupName, elementID) {
  const radioGroup = document.getElementsByName(radioGroupName);
  const element = document.getElementById(elementID);

  if (radioGroup.value == "hot") {
    element.textContent = "HOT";
    element.style.color = "red";
    element.style.fontSize = "2rem";
    element.style.fontWeight = "bold";
  }

  if (radioGroup.textContent == "not") {
    element.textContent = "not" + " \u2639";
    element.style.color = "blue";
    element.style.fontSize = "1.25rem";
    element.style.fontWeight = "normal";
  }
}

const radioInputs = document.getElementsByTagName("input");
console.log(radioInputs);

const radio = document.getElementsByName("hot_or_not");
console.log(radio);
/* radioGroup.forEach((option) => {
    option.addEventListener("click", () => {
      if (option.checked) {
        resultText.textContent = `${option.value}`;
      }
      setOpinionStyle();
    });
  }); */
