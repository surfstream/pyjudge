$(document).ready(function()
  {
    $("section").append("<div>");  // Push the comment button to a new line
    console.log("adding .. editor div");
    var $div = $("<div>");
    $div.attr("class", "ace_btn");
    //$div.attr("id", "editor");
    var htmlstr = "<button class=\"btn btn-success\" style=\"font-family: 'Glyphicons Halflings'\">" +
                  "Practice <span class=\"glyphicon glyphicon-comment\"></span></button>";
    $div.html(htmlstr);
    $("section").append($div);

  }
);


$(document).ready(function()
 {


  $("div.ace_btn").click(function()
  {
     // hide the button
     $(this).slideUp();

     var parentElem = $(this).parent();
     var unique_str = parentElem.attr("data-unique");

     // create the new facebook comment div if it's not there already
     if($(this).next().attr("class") == "ace-editor")
     {
       console.log("div already exists");
     }
     else
     {
       var $div = $("<div>");
	   $div.attr("id", "editor");
       $div.attr("class", "ace-editor");
       $div.attr("data-href", "https://pybook.rocks/book#/" + unique_str);
       $div.attr("data-numposts", "3");

       // Add this div
       $(this).after($div);
       console.log(unique_str);

       (function(d, s, id) {
       	
       	/*var ace_node = d.getElementById(id);
        //var fb_script_node = d.getElementById(id);
        if (ace_node)
        {
			var editor = ace_node.edit("editor");
			editor.setTheme("ace/theme/twilight");
			editor.getSession().setMode("ace/mode/python");
			editor.setValue("the new text here");
			editor.getSession().setTabSize(4);
			editor.getSession().setUseWrapMode(true);
			return;
        }
        /*var js, fjs = d.getElementsByTagName(s)[0];
        js = d.createElement(s); js.id = id;
        js.src = "https://cdn.jsdelivr.net/ace/1.2.4/min/ace.js";
        fjs.parentNode.insertBefore(js, fjs);
		ace_node = d.getElementById(id);*/
		var editor = ace.edit("editor");
		editor.setTheme("ace/theme/twilight");
		editor.getSession().setMode("ace/mode/python");
		editor.setValue("the new text here");
		editor.getSession().setTabSize(4);
		editor.getSession().setUseWrapMode(true);
		editor.$blockScrolling="Infinity"
       }(document, 'script', 'ace-jssdk'));
		//$("section").append($div);
     }
  }
  );
 }
);




