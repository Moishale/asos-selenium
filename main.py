import time
from ClothoWeb.clothoweb import ClothoWeb

with ClothoWeb() as bot:
    bot.land_first_page()
    bot.select_product_to_search(input('Enter Product: '))
    bot.report_results()
    
