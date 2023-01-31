$(function () {
    $(".btn-delete").click(function(){
        var id = $(this).attr('data-id');
        if(confirm("Are your sure?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });
            
            $.ajax({url: url,
                method: 'post',
                data: {id:id}, 
                success: function(result){
                   console.log(result);
                   if(result.success) {
                        alert(result.message);
                       location.reload()
                   } else {
                       alert(result.message);
                   } 
                }});
        }
    });        

    
        
        
});


const wrapper = document.getElementById("wrapper");
const imageInput = document.getElementById("image");
const editpic = document.getElementById("editpic");

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
