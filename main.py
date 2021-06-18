import scrapy

class TalDaSpider(scrapy.Spider):  
    name = "TalDaSpider"
    start_urls = [
    "https://repositorio.utfpr.edu.br/jspui/handle/1/20556",
    "https://repositorio.utfpr.edu.br/jspui/handle/1/20557",
    "https://repositorio.utfpr.edu.br/jspui/handle/1/20558"
    ]
    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8"
    }
   

    def parse(self, response):     
        titulo = response.css(".metadataFieldValue.dc_title::text").get()  
        autores = response.css(".author::text").get()
        orientadores = response.css(".advisor::text").get()
        data = response.css(".metadataFieldValue.dc_date_issued::text").get()  
        resumo = response.css(".metadataFieldValue.dc_description_resumo::text").get()
        
        palavras_chave = response.css(".subject::text").getall()
        palavras = []
        for i in palavras_chave:
            palavras.append(i)

        yield {
            "titulo": titulo,
            "autores": autores, 
            "orientadores": orientadores,
            "palavras-chave":palavras,
            "data": data,
            "resumo":resumo,
        }
