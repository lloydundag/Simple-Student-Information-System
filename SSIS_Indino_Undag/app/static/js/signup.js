window.onload = function() {
    // Get the form element
    var form = document.getElementById("enrollform");

    // Get the image input
    var imageInput = form.querySelector("#image");

    // Check if the image input exists
    if(imageInput){
        // Create a new div element with id "wrapper"
        var wrapper = document.createElement("div");
        wrapper.id = "wrapper";

        // Create an img element
        var img = document.createElement("img");

        // Set the src, class and id attributes of the img element
        img.src = "/static/uploads/default.png";
        img.className = "user-image";
        img.id = "editpic";

        // Append the image input to the wrapper div
        wrapper.appendChild(imageInput);

        // Append the img element to the wrapper div
        wrapper.appendChild(img);

        // Get the second child of the form
        var formGroup = form.querySelector(".form-group");

        // Append the wrapper div as a child of the form-group div
        formGroup.appendChild(wrapper);

        wrapper.addEventListener("click", function() {
            imageInput.click();
          });
        
          imageInput.addEventListener("change", function() {
            if (this.files && this.files[0]) {
              var reader = new FileReader();
        
              reader.onload = function (e) {
                  editpic.src = e.target.result;
              }
        
              reader.readAsDataURL(this.files[0]);
            }
          });

    }
}
