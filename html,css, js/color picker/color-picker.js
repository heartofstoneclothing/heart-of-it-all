// Array to store favorite colors
const colorList = [];

function addColor() {
  const redInput = document.getElementById('redInput');
  const greenInput = document.getElementById('greenInput');
  const blueInput = document.getElementById('blueInput');

  const red = parseInt(redInput.value);
  const green = parseInt(greenInput.value);
  const blue = parseInt(blueInput.value);

  if (isValidColorValue(red) && isValidColorValue(green) && isValidColorValue(blue)) {
    const color = `rgb(${red}, ${green}, ${blue})`;
    colorList.push(color);
    displayColorList();
  } else {
    alert('Please enter valid values for red, green, and blue (0-255).');
  }
}

function isValidColorValue(value) {
  return !isNaN(value) && value >= 0 && value <= 255;
}

function displayColorList() {
  const favoritesListContainer = document.getElementById('favoritesList');
  favoritesListContainer.innerHTML = '';

  colorList.forEach(color => {
    const listItem = document.createElement('li');

    // Create a colored box next to the color in the list
    const colorBox = document.createElement('div');
    colorBox.className = 'color-box';
    colorBox.style.backgroundColor = color;

    // Add the colored box and color text to the list item
    listItem.appendChild(colorBox);
    listItem.innerHTML += color;

    // Add the list item to the color list
    favoritesListContainer.appendChild(listItem);
  });
}

function downloadColorList() {
  const colorListText = colorList.join('\n');
  const blob = new Blob([colorListText], { type: 'text/plain' });

  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = 'colorList.txt';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
