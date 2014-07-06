markov-py
=========

I realised a couple days ago that I had never actually written a Markov chain text generator from scratch, so I figured I'd go ahead and do that. I had fun! I love reading the text it produces.
It's not totally efficient. I tried not to let it be too terrible, but there's still obviously a lot of work to be done if I wanted to use this for any really large datasets and large values of n. I think the biggest speed improvement I could make would be caching indices (or actual values) of "relevant" n-grams for each (n-1)-gram, because I'm doing a linear search for possibilities on each pass.

It was just a project I coded up to prove that I could do it. Nothing fancy here.