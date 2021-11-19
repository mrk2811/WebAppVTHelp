$(function(){

  //Check image is selected
  $('input#attach-button').on("click", function(){
    //var like = $(this).val();
    var attachConfirmation = "Image is Attached";
    $(this).val(attachConfirmation);
  })

  //Update campus name in the heading when selecting campus
  $('img#ncr-image').on("click", function(){
    var headerCampusSelection = "National-CR Campus";
    $('div#campus-name').text(headerCampusSelection);
     var successMsg = $('<p class = "campus-selection-success">Campus Selected!</p>');
    $(successMsg).appendTo($(this).parent()).fadeOut('slow', function(){
      $(this).remove();
    })
  })

  $('div.sports-and-games-post button.author').click(function(){
      var place_id = $(this).attr('data-place-id');
      var ajax_url = $(this).attr('data-ajax-url');
       // Using the core $.ajax() method
    $.ajax({

        // The URL for the request
        url: ajax_url,

        // The data to send (will be converted to a query string)
        data: {
            place_id: place_id,
        },

        // Whether this is a POST or GET request
        type: "GET",

        // The type of data we expect back
        dataType : "json",

        headers: {'X-CSRFToken': csrftoken},

        context: this
    })
      // Code to run if the request succeeds (is done);
      // The response is passed to the function
      .done(function( json ) {
          //alert("request received successfully");
          if(json.success == 'success') {
               var successMsg = $('<p class = "author-name">author: json.author</p>');
               $(successMsg).appendTo($(this).parent()).fadeOut('slow', function(){
                    $(this).remove();
                })
          } else {
              alert("Error");
          }

      })
      // Code to run if the request fails; the raw request and
      // status codes are passed to the function
      .fail(function( xhr, status, errorThrown ) {
        alert( "Sorry, there was a problem!" );
        console.log( "Error: " + errorThrown );
      //  console.log( "Status: " + status );
      //  console.dir( xhr );
      })
      // Code to run regardless of success or failure;
      .always(function( xhr, status ) {
        alert( "The request is complete!" );
      });
  })

  $('div.sports-and-games-post form.edit-location').click(function(){
  var place_id = $(this).attr('data-place-id');
  var ajax_url = $(this).attr('action');
  var new_location = $('div.sports-and-games-post form.edit-location input.list-location-text').text();
   // Using the core $.ajax() method
    $.ajax({

        // The URL for the request
        url: ajax_url,

        // The data to send (will be converted to a query string)
        data: {
            place_id: place_id,
            new_location: new_location      //add location
        },

        // Whether this is a POST or GET request
        type: "POST",

        // The type of data we expect back
        dataType : "json",

        headers: {'X-CSRFToken': csrftoken},

        context: this
    })
  // Code to run if the request succeeds (is done);
  // The response is passed to the function
  .done(function( json ) {
      alert("request received successfully");
      if(json.success == 'success') {
          var location = $(this).siblings('h3#sports-and-games-post-title');
          var newlocation = json.new_location;
          $(location).text(newlocation);
      } else {
          alert("Error");
      }

  })
  // Code to run if the request fails; the raw request and
  // status codes are passed to the function
  .fail(function( xhr, status, errorThrown ) {
    alert( "Sorry, there was a problem!" );
    console.log( "Error: " + errorThrown );
  //  console.log( "Status: " + status );
  //  console.dir( xhr );
  })
  // Code to run regardless of success or failure;
  .always(function( xhr, status ) {
    alert( "The request is complete!" );
  });
})





    //adding new comments in details page
      $('input#add-new-comment').click(function(){
  var username = $(this).attr('data-username');
  //var comment_text = $("#comment-text").val();
  var comment_text = $(this).prev().attr("comment-text").val();
  var place = $(this).attr('data-place');
  var ajax_url = $(this).attr('data-ajax-url');
   // Using the core $.ajax() method
    $.ajax({

        // The URL for the request
        url: ajax_url,

        // The data to send (will be converted to a query string)
        data: {
            username: username,
            comment_text: comment_text,
            place: place//add location
        },

        // Whether this is a POST or GET request
        type: "POST",

        // The type of data we expect back
        dataType : "json",

        headers: {'X-CSRFToken': csrftoken},

        context: this
    })
  // Code to run if the request succeeds (is done);
  // The response is passed to the function
  .done(function( json ) {
      alert("request received successfully");
      if(json.success == 'success') {
         // var location = $(this).siblings('h3#sports-and-games-post-title');
         // var newlocation = json.new_location;
          //$(location).text(newlocation);
      } else {
          alert("Error");
      }

  })
  // Code to run if the request fails; the raw request and
  // status codes are passed to the function
  .fail(function( xhr, status, errorThrown ) {
    alert( "Sorry, there was a problem!" );
    console.log( "Error: " + errorThrown );
  //  console.log( "Status: " + status );
  //  console.dir( xhr );
  })
  // Code to run regardless of success or failure;
  .always(function( xhr, status ) {
    alert( "The request is complete!" );
  });
})










  //check queryString
  checkQueryString();
});

function checkQueryString() {
  var querystring = window.location.search;
  //console.log(querystring);
  var urlParams = new URLSearchParams(querystring);
  if(urlParams.has('search')) {
    var keyword = urlParams.get("search");
    if(keyword == 'sports') {
      //window.alert("you searched sports");
    } else {
      //window.alert("No search results found");
      //var term = $('h3.result-term').text();
      //console.log(term);
      var term = "no results found";
      $('h3.result-term').text(term);


    }
  }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');