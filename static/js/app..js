// navbar behavior

window.addEventListener("scroll",function(){
    var nav = document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 40);
    
});


/*


// scroll animation
 
const skills = document.querySelectorAll('.skill');

const observer = new IntersectionObserver(entries =>{
    entries.forEach(entry =>{
        entry.target.classList.toggle("show", entry.isIntersecting);
        
    })
})

skills.forEach(skill =>{
    observer.observe(skill)
})

*/