// 🌦 Hover-pop-up voor klimaatboxen (index.html)
const boxes = document.querySelectorAll('.klimaat-box');
const popup = document.getElementById('popup');
let activeBox = null;

if (boxes.length > 0 && popup) {
  boxes.forEach(box => {
    box.addEventListener('mouseenter', () => {
      if (activeBox !== box) {
        activeBox = box;
        popup.innerHTML = box.getAttribute('data-fulltext');
        popup.style.display = 'block';
      }
    });

    box.addEventListener('mouseleave', () => {
      if (activeBox === box) {
        popup.style.display = 'none';
        popup.innerHTML = '';
        activeBox = null;
      }
    });
  });
}
