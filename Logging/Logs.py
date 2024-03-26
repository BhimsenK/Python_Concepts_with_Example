import logging
logging.basicConfig(filename = "Log file/test_new.log" , level = logging.DEBUG ,format = '%(asctime)s %(message)s'  )

L1 = ['shree', 'bhimsen', 'sarthak', 'Bhimrao' ]


for i in L1:
    logging.info(f'Name : {i}')
