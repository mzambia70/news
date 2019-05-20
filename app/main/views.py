# taking the temp and searches,then loads it
from flask import render_template, request, redirect, url_for
from . import main  # importing app instance
from  app.requests import get_news, search_news, process_news
from .models import review
from .forms import ReviewForm
Review = review.Review

#view
@main.route('/')
def index():
  '''
  view root page function that returns the  index page and its data
  '''
  # Getting pupolar news
  sources = get_sources('business')
  # print(popular_news)
  sports_sources = get_sources('sports')
  technology_sources = get_sources('technology')
  entertainment_sources = get_sources('entertainment')
  title = "NEWS HIGHLIGHTER"

  if search_news:
    return redirect(url_for('search', news_name=search_news))
  else:
    return render_template('index.html', title = title, sources = sources, sports_sources = sports_sources,technology_sources = technology_sourcse,entertainment_sources = entertainment_sources )


@main.route('/search/<news_name>')
def search(news_name):
  '''
  View function to display the search results
  '''
  news_name_list = news_name.split(" ")
  news_name_format = "+".join(news_name_list)
  searched_news = search_news(news_name_format)
  title = f'search results for {news_name}'
  return render_template('search.html', news = searched_news)


@main.route('/sources/<id>')
def news(id):
  '''
  view news page function that returns the news details page and its data
  '''
  news = get_news(id)
  title = f'news highlighter'
   # reviews = Review.get_reviews(news.id)
  return render_template('news.html', title = title,news = news,reviews = reviews)

@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
  form = ReviewForm()
  news = get_news(id)

  if form.validate_on_submit():
    title = form.title.data
    review = form.review.data
    new_review = Review(news.id, title,news.poster,review)
    new_review.save_review()
    return redirect(url_for('news', id = news.id ))

  title = f'{news.title} review'
  return render_template('new_review.html', title = title, review_form=form, news=news)