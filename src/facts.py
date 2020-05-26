import logging
import sys
sys.path.append('../lib')

import cat_fact



''''
Main function to get selected facts
facts are selected (A,C,E...) and Updated in a service.
'''

logger = logging.getLogger(__name__)
logging.basicConfig(filename='facts.log', level=logging.DEBUG,filemode='w', 
            format='%(name)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    fact_Obj=cat_fact.CatParse()
    fact_Obj.set_conn_params("https://cat-fact.herokuapp.com/facts")
    facts_selected_data=fact_Obj.get_data()
    logging.debug('%s  Cat Facts selected ' ,facts_selected_data)
    fact_Obj.post_server(facts_selected_data)
