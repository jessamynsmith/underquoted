$(document).ready(function() {
  gtag('event', 'page_view');

  $("#search").on('click', function(event) {
    gtag('event', 'search', {
      'search_term': $("#search_text").val()
    });
  });
});
