// Does a Bad Security Gag

function passwordAlert() {

        alert("Login: admin | Password: toor")
        alert("Oops, you weren't supposed to see that")
    }
    

function webPageLogin() {
        do {
            var login = prompt("Enter Login: ")
            if (login!="admin") {
                alert("Incorrect Login!")
            }
        }
        while (login != "admin")
    
        
        do {
            var password = prompt("Enter Password: ")
            if (password != "toor") {
                alert("Incorrect Password!")
            }
        }
        while (password!="toor")


    }



passwordAlert()
webPageLogin()

alert("Welcome User")

// This is How to Get audio to play on click

script>
    function learnmore() {
      const audio=document.getElementById("playsound")
      audio.play()
      alert('Work in progress. Come back soon!')
    }
</script>

  <button type="button" class="btn btn-outline-secondary" style="top: 113%; left: 46.2%; right: auto; position: absolute;" onclick=learnmore() id="playbutton">Learn More</button>

  <audio controls hidden id="playsound">
    <source src="trombone.mp3" type="audio/mp3">
  </audio>