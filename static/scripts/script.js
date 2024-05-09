function setOpinionStyle(radioGroupName, elementID) {
  const radioGroup = document.getElementsByName(radioGroupName);
  const element = document.getElementById(elementID);

  radioGroup.forEach((option) => {
    if (option.value == "hot" && option.checked) {
      element.textContent = "HOT";
      element.style.color = "red";
      element.style.fontSize = "2rem";
      element.style.fontWeight = "bold";
    }

    if (option.value == "not" && option.checked) {
      element.textContent = "not" + " \u2639";
      element.style.color = "blue";
      element.style.fontSize = "1.25rem";
      element.style.fontWeight = "normal";
    }
  });
}

function filterOver30(arr) {
  console.log(arr);
  const result = arr.filter((person) => person.age > 30);
  console.log(result);
  createNewSpan(result);
}

const result = document.getElementById("result");
function createNewSpan(arr) {
  arr.forEach((person) => {
    const info = document.createElement("span");
    info.innerText = person.name + ", " + person.age;
    result.appendChild(info)
  });
}

const dialog = document.getElementById('dialog')
function openModal(){
  dialog.showModal()
}

function closeModal(){
  dialog.close()
}
