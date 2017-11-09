$(document).ready(function () {
  gtag('event', 'page_view');

  var result = gtag('event', 'purchase_attempt', {
    'event_label': 'single',
    'purchase_type': 'single',
    'article_price': '5'
  });
  console.log(result);

  var result = gtag('event', 'purchase', {
    'purchase_type': 'single',
    'article_price': '5'
  });
  console.log(result);

  $("#search").on('click', function (event) {
    gtag('event', 'search', {
      'search_term': $("#search_text").val()
    });
  });
});
