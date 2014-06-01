# Create your views here.

from django.shortcuts import render_to_response, render
from book.models import Book, Chapter, Comment
from django.http import HttpResponse
from forms import BookForm, ChapterForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from book.forms import ChapterForm

from django.template import RequestContext
from django.contrib import messages

import logging

logr = logging.getLogger(__name__)


def books(request): 
    language = 'en-us'    
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    args = {}
    args.update(csrf(request))
    
    args['books'] = Book.objects.all()
    args['language'] = language
    args['session_language'] = session_language
        
    return render_to_response('books.html', args)


def book(request, book_id=1):
    a = Book.objects.get(id=book_id)
    
    if request.POST:
        form = CommentForm(request.POST, request.FILES)      
        if form.is_valid():
            c = form.save(commit=False)
            c.pub_date = timezone.now()
            c.book = a
            c.save()  
            form.save()
               
        messages.add_message(request, messages.SUCCESS, "Your Article was added!")
        return HttpResponseRedirect('/book/get/%s' % book_id) 
    else:
        CommentForm()

       
    args = {}
    args.update(csrf(request))
    
    args['books'] = Book.objects.all()
    args['book'] = a
    args ['chapters'] = Chapter.objects.filter(book_id=a)
    args['form'] = CommentForm  
        
    return render_to_response('book.html', args)  
 

def language(request, language='en-us'):
    response = HttpResponse('setting language to %s' % language)
    
    response.set_cookie('lang', language)
    
    request.session['lang'] = language
    
    return response


def like_article(request, book_id, chapter_id=1):
    if book_id:
        a = Book.objects.get(id=book_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
    books = Book.objects.filter(title__contains=search_text)
    

    return render_to_response ('ajax_search.html',
                             {'books': books})
                            

def search_chapters(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    
 
    chapters = Chapter.objects.filter(chaptertitle__contains=search_text)
    
    return render_to_response('chapter_search.html', {'chapters': chapters} )

def add_comment(request, book_id, chapter_id=1):
    a = Book.objects.get(id=book_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.book = a
            c.save()
            
            messages.success(request, "Your Comment was added")
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    
    args['book'] = a
    args['form'] = f
    
    return render_to_response('add_comment.html', args)    


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    
    book_id = c.book.id
    
    c.delete()
    
    messages.add_message(request,
                         settings.DELETE_MESSAGE,
                         "Your comment was deleted")
    
    return HttpResponseRedirect('/book/get/%s' % book_id)
    
def paginate_content(str_obj, split_string=None, part=1):
    splitted_string = str_obj.split(split_string) 
    paginator = {
        'pages': len(splitted_string),
        'pages_range': range(len(splitted_string)),
        'number_pages': range(1, (len(splitted_string)+1)),
        'content': splitted_string[part],
        'has_next': range(len(splitted_string)) < int(len(splitted_string)),
    }

    return paginator

def pageview(request, book_id, chapter_id):
   
    a = Book.objects.get(id=book_id)
    chapters = Chapter.objects.filter(book_id=a)
    form = CommentForm   
    
    
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
    except Chapter.DoesNotExist:
        messages.add_message(request, messages.SUCCESS, "Error Page")
        

    if request.method == 'GET' and request.GET.has_key('part'):
        
        part = int(request.GET['part'])
        part = part - 1
     
    else:
        part = 0
        
    split_string = '----split here----'
    paginator = paginate_content(chapter.text, split_string, part)
    current_page = int((part)+1)
    pages = range(int((part)+1))
    next_page = int(part + 1)
    previous_page = int(part - 1)
    
    args = {}
    args.update(csrf(request))
    args['form'] = CommentForm   
    
    return render_to_response('chapter.html',
                              {'book': book,
                               'chapters': chapters,
                               'chapter': chapter, 
                               'form' : form,
                               'paginator': paginator,
                               'next_page': next_page,
                               'previous_page': previous_page,
                               'current_page': current_page, 
                               'pages': pages,
                               })
                           
def count_words(str_obj, num, max_length, chapter_id=1):
    import re
    re_words = re.compile(r'&.*?;|<.*?>|(\w[\w-]*)', re.U|re.S)
    chapter = Chapter.objects.get(pk=chapter_id)
    wordlength = re_words.get(chapter)
    wordcount = max_length(wordlength)
    return render_to_response('chapter.html',
                              {'wordcount': wordcount, 
                              }) 
    
    