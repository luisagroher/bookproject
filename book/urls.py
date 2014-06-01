from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    
    # general urls
    url(r'^language/(?P<language>[a-z\-]+)$', 'book.views.language'),
    
    # book urls
    url(r'^$', 'book.views.books', name="books"),
    url(r'^get/(?P<book_id>\d+)$', 'book.views.book', name='book'),    
    url(r'^get/page/(?P<book_id>\d+)/(?P<chapter_id>\d+)$', 'book.views.pageview', name='pageview'),

    # interactive urls
    url(r'^search/$', 'book.views.search_titles', name="title"),
    url(r'^like/(?P<book_id>\d+)$', 'book.views.like_article', name='like'),
    url(r'^like/page/(?P<book_id>\d+)/(?P<chapter_id>\d+)$', 'book.views.like_article', name='likearticle'),  
    url(r'^add_comment/(?P<book_id>\d+)$', 'book.views.add_comment', name='comment'),
    url(r'^add_comment/page/(?P<book_id>\d+)/(?P<chapter_id>\d+)$', 'book.views.add_comment', name='addcomment'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', 'book.views.delete_comment'),

)
