class QueryController < ApplicationController
  def index
    @queries = Query.all
    @data = Datum.all
    # @latest_id = Query.order(:created_at desc, :limit => 1)
    # @latest_id = Query.find(:order => "created_at", :limit => 1)

  end
  def show
    # @query = Query.find(params[:id])
  end
  def new_form   ### I might not even need this
  end

  def create_row


    @query = Query.new
    @query.query = params[:query]
    @query.save

    if Datum.maximum(:id).class == NilClass
      @latest_id = '0'
    else
      @latest_id = Datum.maximum(:id).to_s
    end

    a = Query.maximum(:id).to_s
    # system('python python_old/web_scraper_5.py ' + params[:query] + " " + @latest_id)
    system('python python/web_scraper_5.py ' + params[:query] + ' ' + @latest_id + ' ' + a)
    # system('python python/web_scraper_5.py ' + params[:query] + ' 1')



    redirect_to("http://localhost:3000/")
  end
end