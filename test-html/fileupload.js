if (window.File && window.FileReader && window.FileList && window.Blob) {
    function showFile() {
       var preview = document.getElementById('show-text');
       var file = document.querySelector('input[type=file]').files[0];
       var reader = new FileReader()

       var textFile = /text.*/;

       if (file.type.match(textFile)) {
          reader.onload = function (event) {
             preview.innerHTML = event.target.result;
          }
       } else {
          preview.innerHTML = "<span class='error'>It doesn't seem to be a text file!</span>";
       }
       reader.readAsText(file);
    }
 } else {
    alert("Your browser is too old to support HTML5 File API");
 }