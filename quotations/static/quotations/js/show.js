$(document).ready(function () {
  gtag('event', 'page_view');

  gtag('event', 'purchase', {
    'purchase_type': 'single',
    'article_price': '5'
  });

  $("#search").on('click', function (event) {
    gtag('event', 'search', {
      'search_term': $("#search_text").val()
    });
  });
});
