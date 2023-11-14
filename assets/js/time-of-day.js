function displayGreeting() {
    var currentTime = new Date().getHours();
    var minutes = new Date().getMinutes()
    var greeting;
    if(minutes < 10){
      minutes = 10 +minutes
    }

    if (currentTime >= 0 && currentTime < 12) {
 
      greeting = "Good Morning! The Time Is " + currentTime + ':' + minutes +'AM';
      } else if (currentTime >= 12 && currentTime < 18) {
          greeting = "Good Afternoon! The Time Is " + currentTime + ':' + minutes +'PM';
      } else {
          greeting = "Good Evening! The Time Is " + currentTime + ':' + minutes +'PM';
      }

    // Display the greeting in an element with the id "greeting"
    document.getElementById("time").innerText = greeting;
}
window.onload = displayGreeting;

function toggleDropdown() {
    var dropdown = document.getElementById("myDropdown");
    dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
  }

  // Close the dropdown if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropdown-btn')) {
      var dropdown = document.getElementById("myDropdown");
      if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
      }
    }
  }