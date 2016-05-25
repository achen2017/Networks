class QueryController < ApplicationController
  def index
    @queries = Query.all
  end
  def show
    # @query = Query.find(params[:id])
  end
  def new_form   ### I might not even need this
  end

  def create_row
    @query = Query.new
    @query.name = params[:query]
    # @query.query_id = params[:id]
    # @output = Output.new


    # @query = Query.new
    # system('python python/web_scraper_5.py ' + params[:query])


    ### this is another idea, where I create a table in the controller, and then reference it in python
    # @query_info = InfoGroup.new




    # system('python python/web_scraper_5.py ' + params[:query] + ' 24')
    # @query.query = params[:query]
    @query.save



    redirect_to("http://localhost:3000/")
  end
end
