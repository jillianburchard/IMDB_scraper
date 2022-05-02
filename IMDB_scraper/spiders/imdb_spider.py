
import scrapy
#import pandas as pd

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'

    start_urls = ['https://www.imdb.com/title/tt0264464/']

    def parse(self, response):
        cast_crew = start_urls[0] +  "fullcredits"
        
        yield scrapy.Request(cast_crew, callback= self.parse_full_credits)

    def parse_full_credits(self, response):

        actor_path = [a.attrib["href"] for a in response.css("td.primary_photo a")]
        prefix = "https://www.imdb.com/"
        actor_urls = [prefix + suffix for suffix in actor_path] #clicking on actor headshot to go to actor page

        for info in actor_urls: #not sure if this is needed 
            yield scrapy.Request(info, callback = self.parse_actor_page)
            
            #in notes how were you able to do just Request, is scrapy.Request ok for these?

    def paarse_actor_page(self, response):
        
        actor_name = response.css("span.itemprop::text").get()    

        for i in response.css('div.filmo-head-actor'):

            movie_name = i.css("div.filmo-row::text").getall()

            yield{
                "actor": actor_name,
                "movie" : movie_name
            }
    
    #df.groupby('movie').size().reset_index(name='Number of Shared Actors')
    #print(df)

       



