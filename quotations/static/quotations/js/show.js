$(document).ready(function() {
  gtag('event', 'loaded');

  $("#search").on('click', function(event) {
    gtag('event', 'search', {
      'search_term': $("#search_text").val()
    });
  });
});
