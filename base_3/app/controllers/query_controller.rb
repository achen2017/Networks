class QueryController < ApplicationController
  def index
    @queries = Query.all
    # @latest_id = Query.order(:created_at desc, :limit => 1)
    # @latest_id = Query.find(:order => "created_at", :limit => 1)

  end
  def show
    # @query = Query.find(params[:id])
  end
  def new_form   ### I might not even need this
  end

  def create_row



    # @query = Query.new
    @latest_id = Query.maximum(:id)
    @latest_id = @latest_id.to_s
    # system('python python_old/web_scraper_5.py ' + params[:query] + " " + @latest_id)
    system('python python/web_scraper_5.py ' + params[:query] + ' ' + @latest_id)
    # system('python python/web_scraper_5.py ' + params[:query] + ' 1')







    redirect_to("http://localhost:3000/")
  end
end