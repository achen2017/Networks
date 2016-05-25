Rails.application.routes.draw do
  get('/', { :controller => 'query', :action => 'index' })
  get('/start_query', { :controller => 'query', :action => 'create_row'})

end
