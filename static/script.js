function calc(){
  let size = document.getElementById("size").value;
  let type = document.getElementById("type").value;
  let cost = size * type;

  document.getElementById("result").innerText = "Estimated Cost: ₹" + cost;
}
document.querySelectorAll(".item img").forEach(img => {
  img.onclick = () => {
    let popup = document.createElement("div");
    popup.style.position = "fixed";
    popup.style.top = 0;
    popup.style.left = 0;
    popup.style.width = "100%";
    popup.style.height = "100%";
    popup.style.background = "rgba(0,0,0,0.9)";
    popup.innerHTML = `<img src="${img.src}" style="max-width:90%;margin:5% auto;display:block;">`;
    popup.onclick = () => popup.remove();
    document.body.appendChild(popup);
  }
});
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
  });
});

document.querySelectorAll(".hidden").forEach(el => observer.observe(el));
