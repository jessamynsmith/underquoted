$(document).ready(function () {

  $("#search").on('click', function (event) {
    gtag('event', 'purchase_attempt', {
      'event_action': 'search',
      'event_label': $("#search_text").val()
    });
  });

});
