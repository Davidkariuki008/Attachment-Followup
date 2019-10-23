// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("navbar").style.padding = "30px 10px";
    document.getElementById("logo").style.fontSize = "25px";
    document.getElementById("navbar").style.backgroundColor = "#03bafc";
    // document.getElementById("logo").style.color = "#000000";
    // document.getElementById("link-home").style.color = "#000000";
    // document.getElementById("link-login").style.color = "#000000";
    // document.getElementById("link-signup").style.color = "#000000";
    // document.getElementById("link-user").style.color = "#000000";
  } else {
    document.getElementById("navbar").style.padding = "30px 10px";
    document.getElementById("logo").style.fontSize = "35px";
    document.getElementById("navbar").style.backgroundColor = "#002147";
    document.getElementById("logo").style.color = "#ffffff";
    document.getElementById("link-home").style.color = "#ffffff";
    document.getElementById("link-login").style.color = "#ffffff";
    document.getElementById("link-signup").style.color = "#ffffff";
    document.getElementById("link-user").style.color = "#ffffff";
  }
}

// post job modal
$("#exampleModal").on("show.bs.modal", function(event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var recipient = button.data("whatever"); // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this);
  modal.find(".modal-title").text("New message to " + recipient);
  modal.find(".modal-body input").val(recipient);
});

function myFunction() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  ul = document.getElementsByClassName("card");
  title = ul.getElementsByClassName("header");
  for (i = 0; i < title.length; i++) {
    a = title[i].getElementsById("location")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      title[i].style.display = "";
    } else {
      title[i].style.display = "none";
    }
  }
}
