document.addEventListener('DOMContentLoaded', function () {
  const baubleContainer = document.querySelector('.bauble-container');

  // Create a 15x15 grid of baubles
  for (let i = 0; i < 15; i++) {
    for (let j = 0; j < 15; j++) {
      const bauble = document.createElement('div');
      bauble.classList.add('bauble');
      baubleContainer.appendChild(bauble);

      bauble.addEventListener('click', function () {
        const newColor = getRandomColor();
        bauble.style.backgroundColor = newColor;
      });

      bauble.addEventListener('mouseover', function () {
        const hoverColor = getRandomColor();
        bauble.style.backgroundColor = hoverColor;
        bauble.style.transform = 'scale(1.7)';
        snapNearbyBaubles(baubleContainer, bauble);
      });

      bauble.addEventListener('mouseout', function () {
        bauble.style.transform = 'scale(0.1)';
        resetOtherBaubles(baubleContainer);
      });
    }
  }

  // Helper function to create a random color
  function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  function snapNearbyBaubles(container, targetBauble) {
    container.childNodes.forEach((bauble) => {
      if (bauble !== targetBauble) {
        const distance = calculateDistance(targetBauble, bauble);
        if (distance < 50) {
          const scale = 0.8; // Adjust as needed
          bauble.style.transform = `scale(${scale})`;
        }
      }
    });

    const deltaX = centerX2 - centerX1;
    const deltaY = centerY2 - centerY1;

    return Math.sqrt(deltaX ** 2 + deltaY ** 2);
  }


  function resetOtherBaubles(container) {
    container.childNodes.forEach((bauble) => {
      bauble.style.transform = 'scale(1.5)';
    });
  }
});