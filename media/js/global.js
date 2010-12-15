$(document).ready(function() {

    //$('#grid').masonry({ columnWidth: 200 });

    initializeGrid();

});


function initializeGrid() {
	$("#grid-slider").slider({
		value: 50,
		max: 100,
		min: 10,
		slide: function(event, ui) {
			$("ul#grid li").css("font-size", ui.value + "px");
		}
	});
	$("ul#grid li img").each(function() {
		var width = $(this).width() / 100 + "em";
		var height = $(this).height() / 100 + "em";
		$(this).css("width", width);
		$(this).css("height", height);
	});
}
