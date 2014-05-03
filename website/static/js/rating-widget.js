createRatings = function () {
    "use-strict";

    var $rating = $('.rating-item');

    $rating.each(function(i, r) {
        var $r = $(r);
        var rating = parseInt($r.text());
        console.log(rating);
        $r.empty();

        var i;

        for (i = 0; i < rating; i++) {
            var el = $('<span></span>');
            el.addClass('rating-element rating-checked');
            $r.append(el);
        }

        for (; i < 5; i++) {
            var el = $('<span></span>');
            el.addClass('rating-element');
            $r.append(el);
        }
    });
};
