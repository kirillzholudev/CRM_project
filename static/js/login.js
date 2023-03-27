const label = document.querySelectorAll(".form-control label");
    
label.forEach((label) => {
  label.innerHTML = label.innerText
    .split("")
    .map(
      (letter, idx) =>
      `<span style="transition-delay:${idx * 4}ms">${letter}</span>`
)
   .join("");
});