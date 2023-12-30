// Function to generate a random color
function getRandomColor() {
    // Implement your logic for generating random colors
}

// Function to generate a random shape (for example, circle or rectangle)
function getRandomShape() {
    // Implement your logic for generating random shapes
}

// Function to create and append a random SVG element to the container
function createRandomSVG() {
    const svgContainer = document.getElementById('svgContainer');

    const svgElement = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svgElement.setAttribute('width', '100');
    svgElement.setAttribute('height', '100');
    svgElement.setAttribute('style', `fill: ${getRandomColor()}; position: relative;`);

    const shape = getRandomShape();
    // Customize shape attributes based on your preferences

    svgElement.appendChild(shape);
    svgContainer.appendChild(svgElement);
}

// Generate a random SVG on page load
createRandomSVG();
