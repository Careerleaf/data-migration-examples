import logging
import logging.config

import sys 
import yaml

from utils import get_config


configDict = yaml.load(open('logging-config.yml', 'r'))
logging.config.dictConfig(configDict)

import_logger = logging.getLogger('import_log')
logger  = logging.getLogger('console')







if __name__ == '__main__':
    config = get_config()
    #url = config.get('careerleaf', 'url')
    # key_secret = '{}/{}'.format(config.get('careerleaf', 'api_key'), config.get('careerleaf', 'api_secret'))
    
    command = sys.argv[1] if len(sys.argv)>1  else 'undefined'

    if command == 'employers':
    	from employers import importer
    	importer.run(config)
    if command == 'jobseekers-export':
    	from jobseekers_export import exporter
    	exporter.run(config)    	
    else:
    	sys.stderr.write('ERROR: unsupported command: %s\n' % command)    	

