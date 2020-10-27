$(".modal .cancel").on("click", function() {
	$(this).parents(".modal").removeClass("is-active is-clipped");
});

$(".modal .reset").on("click", function() {
	let form = $(this).parents("form");

	form.find(".input").each(function() {
		$(this).val("");
		$(this).removeClass("is-danger");
		$(this).addClass("is-primary");
	});

	form.find(".help.is-danger").each(function() {
		$(this).remove();
	});
});

// Home
$("#add-student-button").on("click", function(ev) {
	$("#add-student").addClass("is-active is-clipped");
});

$("#student-search").on("input", function(ev) {
	$(".student-level").hide();

	$(".student-level > div").each(function(i) {
		if ($(this).find(".heading").text().trim() === "Name") {
			console.log("yea")
			let name = $(this).find(".is-size-4");

			if (name.text().trim().startsWith($("#student-search").val())) {
				$(this).parent().show();
			}
		}
	});
});

// Student
$("#delete-student-button").on("click", function() {
	$("#delete-student").addClass("is-active is-clipped");
});

$(".delete-subject-button").on("click", function() {
	let url = $(this).attr("url-target");
	let modal = $("#delete-subject");
	let deleteBtn = modal.find("a.is-danger");
	deleteBtn.attr("href",
		url);
	modal.addClass("is-active is-clipped");
});