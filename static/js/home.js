var last_slide_package = "p0"


function isMobileDevice() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}


function handleIntersection(entries) {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        // Element is visible, do something
        
      }
    });
}
  
const observer = new IntersectionObserver(handleIntersection, {
  root: null,
  rootMargin: '0px', 
  threshold: 0.0, 
});

const target = document.getElementById('master');
observer.observe(target);
  



  // function
function rent_now(_this){
  location.href = '/contact'
}


function animationCards(_id){
  elem = document.getElementById(_id);
  elem.classList.add(`anim-${_id}`);
}

function remove_anim(_id){
  elem.classList.remove(`anim-${_id}`)
}

/**
 * 
 * @param {Number} to 
 */
function arrow_to(to){
  const slide_package = document.getElementById('slide-package');
  const tS = slide_package.scrollLeft;
  const sW = slide_package.clientWidth;
  const nS = to == 1 ? tS + sW : tS - sW;

  slide_package.scrollTo({
    left: nS,
    behavior: 'smooth' 
  });
}