const icon = document.querySelector('.logo-wrapper img');
document.addEventListener('mousemove', (event) => {
  const mouseX = event.clientX;
  const mouseY = event.clientY;
  const iconX = icon.offsetLeft + (icon.clientWidth / 2);
  const iconY = icon.offsetTop + (icon.clientHeight / 2);
  const diffX = mouseX - iconX;
  const diffY = mouseY - iconY;
  const distance = Math.sqrt(diffX * diffX + diffY * diffY);
  if (distance < 50) {
    const translateX = diffX * 0.2;
    const translateY = diffY * 0.2;
    icon.style.transform = `translate(${translateX}px, ${translateY}px) scale(1.2)`;
  } else {
    icon.style.transform = '';
  }
});
