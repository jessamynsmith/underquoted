$(document).ready(function () {
  gtag('event', 'page_view');

  gtag('event', 'purchase_attempt', {
    'event_label': 'single',
    'event_action': '5'
  });

  $("#search").on('click', function (event) {
    gtag('event', 'search', {
      'search_term': $("#search_text").val()
    });
  });
});
