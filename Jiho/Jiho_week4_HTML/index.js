// <!-- jQuery fadeOut()-->
// <script> 여기 내용 가져옴 </script>
$(document).ready(function(){
		  $("#thanos").click(function(){
		    $("#ironman").fadeToggle();
		    $("#hulk").fadeToggle("slow");
		    $("#groot").fadeToggle(3000);
		  });
		});